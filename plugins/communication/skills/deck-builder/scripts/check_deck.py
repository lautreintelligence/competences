#!/usr/bin/env python3
"""Contrôle la structure d'un deck HTML produit avec le gabarit deck-builder.

Usage : check_deck.py deck.html [storyline.md]

Le script imprime une ligne par constat : E pour une erreur, W pour un
avertissement. Il renvoie le code 1 si une erreur existe. Avec storyline.md,
il compare les titres d'action du squelette aux h1 du deck, dans l'ordre.
Le script utilise la bibliothèque standard seule. Il vérifie la structure.
La relecture vérifie le sens.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

LAYOUTS = {"cover", "exec-summary", "divider", "statement", "chart-insights", "image", "panels-2",
           "panels-3", "panels-4", "table", "combo-table", "framework", "timeline"}
BARE = {"cover", "divider"}
VOID = {"meta", "link", "br", "img", "hr", "input", "col", "wbr", "path", "rect", "circle",
        "line", "polyline", "polygon", "use", "stop"}
COLOR_OK = {"#fff", "#ffffff", "white", "none", "currentcolor", "transparent"}
COLOR_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b|\brgba?\(|\bhsla?\(")


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent, self.children, self.texts = tag, dict(attrs), parent, [], []

    def text(self):
        return " ".join(self.texts + [c.text() for c in self.children])

    def find(self, pred, out=None):
        out = [] if out is None else out
        for c in self.children:
            if pred(c):
                out.append(c)
            c.find(pred, out)
        return out

    def classes(self):
        return set((self.attrs.get("class") or "").split())


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", [], None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.texts.append(data)


def norm(s):
    s = re.sub(r"\s+", " ", s or "").strip().replace("...", "…")
    return s.strip(" «»\"")


def skeleton_titles(md):
    """Titres d'action de la première table dont un en-tête contient « titre »."""
    col, titles, in_table = None, [], False
    for line in md.splitlines():
        if not line.strip().startswith("|"):
            if in_table:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if col is None:
            hits = [i for i, c in enumerate(cells) if "titre" in c.lower()]
            if hits:
                col, in_table = hits[0], True
            continue
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        if col < len(cells):
            titles.append(norm(cells[col]))
    return titles


def hard_colors(svg):
    """Couleurs en dur dans un svg : attributs fill/stroke/style et balises style."""
    found = set()
    for n in [svg] + svg.find(lambda n: True):
        for key in ("fill", "stroke", "style", "stop-color"):
            v = n.attrs.get(key)
            if v and v.strip().lower() not in COLOR_OK:
                for m in COLOR_RE.findall(v):
                    if m.lower() not in COLOR_OK:
                        found.add(m)
        if n.tag == "style":
            found.update(m for m in COLOR_RE.findall(n.text()) if m.lower() not in COLOR_OK)
    return found


def check(html, storyline=None):
    E, W = [], []
    t = Tree()
    t.feed(html)
    cfg = {}
    for sc in t.root.find(lambda n: n.tag == "script" and n.attrs.get("id") == "deck-config"):
        try:
            cfg = json.loads(sc.text())
        except json.JSONDecodeError as e:
            E.append(f"deck-config : JSON invalide ({e})")
    frames = cfg.get("frames") or {}
    slides = t.root.find(lambda n: n.tag == "section" and "slide" in n.classes())
    if not slides:
        return ['aucune <section class="slide"> trouvée'], W
    titles, first_content = [], None
    for i, s in enumerate(slides, 1):
        tag = f"slide {i}"
        layout = s.attrs.get("data-layout", "")
        h1s = [c for c in s.children if c.tag == "h1"]
        title = norm(h1s[0].text()) if h1s else ""
        titles.append(title)
        if "data-example" in s.attrs:
            E.append(f"{tag} : exemple du gabarit non supprimé (data-example)")
        if len(h1s) != 1:
            E.append(f"{tag} : {len(h1s)} <h1>, il en faut exactement un")
        elif not title:
            E.append(f"{tag} : titre vide")
        if layout not in LAYOUTS:
            E.append(f"{tag} : data-layout « {layout} » inconnu ; valeurs : {', '.join(sorted(LAYOUTS))}")
        figs = s.find(lambda n: n.tag == "figure")
        tables = s.find(lambda n: n.tag == "table")
        if layout not in BARE:
            if first_content is None:
                first_content = (i, layout)
            if not s.attrs.get("data-section", "").strip():
                E.append(f"{tag} : data-section absent (indicateur de section)")
            if len(title) > 160:
                E.append(f"{tag} : titre de {len(title)} caractères, dépasse deux lignes")
            elif len(title) > 120:
                W.append(f"{tag} : titre de {len(title)} caractères, vérifier le débordement (touche L dans le deck)")
            if title.endswith("?") and layout != "statement":
                W.append(f"{tag} : un titre d'action affirme, il ne questionne pas")
            if layout != "statement" and not [c for c in s.children if c.tag not in {"h1", "script"}]:
                E.append(f"{tag} : corps vide, le titre n'a aucune preuve")
            if (figs or tables) and not s.attrs.get("data-source", "").strip():
                E.append(f"{tag} : data-source absent sur une slide qui montre des données")
        frame = s.attrs.get("data-frame")
        if frame and frame not in frames:
            E.append(f"{tag} : data-frame « {frame} » absent de deck-config.frames")
        if re.search(r"\{\{|\bTODO\b|lorem ipsum", s.text(), re.I):
            E.append(f"{tag} : texte de remplissage ({{{{, TODO ou lorem ipsum)")
        for fig in figs:
            if not fig.find(lambda n: n.tag in {"svg", "img", "table"}):
                E.append(f"{tag} : emplacement de visuel vide (figure sans svg, img ni table)")
            for svg in fig.find(lambda n: n.tag == "svg"):
                if "viewbox" not in svg.attrs:
                    E.append(f"{tag} : svg sans viewBox, il ne se mettra pas à l'échelle")
                colors = hard_colors(svg)
                if colors:
                    W.append(f"{tag} : couleurs en dur dans le svg ({', '.join(sorted(colors)[:4])}), utiliser les classes f-* et s-*")
        if layout == "exec-summary":
            blocks = {n.attrs.get("data-block") for n in s.find(lambda n: "data-block" in n.attrs)}
            if blocks != {"situation", "complication", "resolution"}:
                E.append(f"{tag} : exec-summary exige trois blocs data-block situation, complication, resolution")
        if layout.startswith("panels-"):
            want, got = int(layout[-1]), len([c for c in s.children if "panel" in c.classes()])
            if got != want:
                E.append(f"{tag} : {layout} attend {want} div.panel, trouvé {got}")
        if layout == "chart-insights" and (len(figs) != 1 or not s.find(lambda n: "insights" in n.classes())):
            E.append(f"{tag} : chart-insights exige une figure et une ul.insights")
        if layout in {"table", "combo-table"} and not tables:
            E.append(f"{tag} : {layout} sans <table>")
        if layout == "combo-table" and not s.find(lambda n: "data-bar" in n.attrs or "data-level" in n.attrs):
            E.append(f"{tag} : combo-table sans cellule data-bar ni data-level")
        if layout == "framework" and not s.find(lambda n: "box" in n.classes()):
            E.append(f"{tag} : framework sans div.box")
        if layout == "image" and len(figs) != 1:
            E.append(f"{tag} : image exige une figure et une seule")
        if layout == "timeline":
            steps = [li for ol in s.find(lambda n: n.tag == "ol" and "timeline" in n.classes()) for li in ol.children if li.tag == "li"]
            if not 3 <= len(steps) <= 7:
                E.append(f"{tag} : timeline exige une ol.timeline de trois à sept étapes, trouvé {len(steps)}")
    if first_content and first_content[1] != "exec-summary":
        W.append(f"slide {first_content[0]} : la première slide de contenu n'est pas un résumé exécutif, justifier par le genre du deck")
    for i in range(len(titles) - 1):
        a, b = titles[i], titles[i + 1]
        if a.endswith("…") and not b.startswith("…"):
            E.append(f"slide {i + 1} : titre terminé par « … » sans suite « … » en slide {i + 2}")
        if b.startswith("…") and not a.endswith("…"):
            E.append(f"slide {i + 2} : titre commençant par « … » sans amorce en slide {i + 1}")
    if storyline is not None:
        sk = skeleton_titles(storyline)
        if not sk:
            E.append("storyline : aucune table de squelette avec une colonne « Titre d'action »")
        else:
            if len(sk) != len(titles):
                E.append(f"storyline : {len(sk)} slides au squelette, {len(titles)} dans le deck")
            for i, (a, b) in enumerate(zip(sk, titles), 1):
                if a != b:
                    E.append(f"slide {i} : titre différent du squelette\n    squelette : {a}\n    deck      : {b}")
    return E, W


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    html = Path(argv[1]).read_text(encoding="utf-8")
    story = Path(argv[2]).read_text(encoding="utf-8") if len(argv) > 2 else None
    E, W = check(html, story)
    for e in E:
        print("E", e)
    for w in W:
        print("W", w)
    print(f"{len(E)} erreur(s), {len(W)} avertissement(s)")
    return 1 if E else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
