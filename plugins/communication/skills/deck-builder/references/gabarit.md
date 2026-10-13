---
type: "Specification"
description: "Contrat du gabarit deck.html du skill deck-builder : zones fixes et dimensions, configuration, balisage d'une slide et des treize mises en page, emplacement de visuel, classes utilitaires, navigation, impression, et constats du script check_deck.py."
status: "stable"
tags: ["presentation", "html", "communication"]
created: 2026-10-13
---

# Gabarit

Le gabarit `assets/deck.html` est un fichier HTML autonome. Le CSS et le script sont inclus. Il n'a aucune dépendance et n'utilise pas le réseau. Il impose la structure et laisse le contenu libre. Le CSS et le script ne se modifient pas. Si une règle gêne, le contenu change.

## Ce que le gabarit impose

| Élément | Valeur | Pourquoi |
|---|---|---|
| Format | 1280 × 720 pixels, mis à l'échelle de la fenêtre | Un format fixe garde les proportions sur tout écran et à l'impression. |
| Marges latérales | 48 px | Les marges sont identiques sur toutes les slides. Rien ne bouge au défilement. |
| Zone d'en-tête | 128 px : une ligne de 24 px pour l'indicateur de section et les boutons de cadre, puis 72 px pour le titre | Le titre commence au même point sur chaque slide. |
| Titre | 28 px, deux lignes au plus. Le gabarit coupe le surplus. | Un titre de trois lignes est un paragraphe. La coupe rend le dépassement visible au contrôle. |
| Zone de corps | Le reste de la hauteur. Le débordement est interdit. | Un contenu qui déborde est un contenu à réduire, pas une zone à agrandir. |
| Pied | 40 px : source à gauche, pied de deck au centre, numéro à droite | La source est au même endroit sur chaque slide. |
| Indicateur de section, boutons de cadre, pied | Générés par le script depuis les attributs de la slide | L'auteur ne peut pas les déplacer ni les styler autrement. |
| Palette | Variables CSS et classes `f-*`, `s-*` | Aucune couleur hors palette. |
| Police | Police système sans empattement | Aucune police à charger. Le rendu est identique partout. |

## Configuration

Un bloc JSON en tête de fichier.

```html
<script type="application/json" id="deck-config">
{
  "lang": "fr",
  "footer": "Comité d'investissement · 13 octobre 2026",
  "sourceLabel": "Source",
  "frames": { "A": "Diagnostic", "B": "Dispositif", "C": "Trajectoire" }
}
</script>
```

- `lang` : la langue du deck. Écris-la aussi dans `<html lang>`.
- `footer` : le texte au centre du pied de chaque slide. Vide si inutile.
- `sourceLabel` : le mot qui précède la source dans le pied.
- `frames` : les boutons de cadre, clé et libellé. Objet vide quand le deck n'utilise pas de cadre. Un seul jeu par deck.

## Écrire une slide

Une slide est une `section` dans `main.deck`. L'auteur écrit les attributs, le titre et le corps. Le script génère le reste.

```html
<section class="slide" data-layout="chart-insights" data-section="01 Diagnostic › ARR" data-frame="A"
         data-source="Comptabilité analytique, ARR au 30 juin">
  <h1>Entre 2024 et 2026, l'attrition a repris 2,2 M€ sur les 4,7 M€ gagnés</h1>
  <figure>…</figure>
  <ul class="insights">…</ul>
</section>
```

| Attribut | Obligatoire | Contenu |
|---|---|---|
| `data-layout` | Oui | Une des treize mises en page. |
| `data-section` | Oui, sauf `cover` et `divider` | L'indicateur de section, de la forme `01 Diagnostic › ARR`. |
| `data-source` | Oui dès que la slide montre une `figure` ou un `table` | La source de la preuve, telle que le pied l'affiche. |
| `data-frame` | Non | La clé du bouton de cadre actif, déclarée dans `frames`. |

Le `h1` est le titre d'action. Il est identique au titre du squelette, caractère pour caractère. Une slide a un seul `h1`. Tout ce qui suit le `h1` forme le corps.

## Les treize mises en page

### `cover`

Couverture. Pas d'en-tête. Le corps est centré verticalement.

```html
<section class="slide" data-layout="cover">
  <p class="kicker">Nordis · Customer Success</p>
  <h1>Enrayer l'attrition : investir 2 M€ dans une équipe Customer Success</h1>
  <p class="subtitle">Décision demandée au comité d'investissement</p>
  <p class="meta">13 octobre 2026 · Direction Clients</p>
</section>
```

### `exec-summary`

Résumé exécutif. Trois blocs obligatoires : `situation`, `complication`, `resolution`. Le gabarit met le bloc de résolution en avant.

```html
<section class="slide" data-layout="exec-summary" data-section="Résumé exécutif">
  <h1>Investir 2 M€ sur deux ans dans six Customer Success Managers retient 1,5 M€ d'ARR par an</h1>
  <div data-block="situation"><h2>Situation</h2><p>…</p></div>
  <div data-block="complication"><h2>Complication</h2><p>…</p></div>
  <div data-block="resolution"><h2>Résolution</h2><p>…</p><ul><li>…</li></ul></div>
</section>
```

### `divider`

Intercalaire de section. Pas d'en-tête.

```html
<section class="slide" data-layout="divider">
  <p class="kicker">01</p>
  <h1>Diagnostic : d'où vient l'attrition</h1>
  <p class="subtitle">Trajectoire de l'ARR, segments touchés, causes</p>
</section>
```

### `statement`

Slide-affirmation : une phrase en grand, centrée, avec l'indicateur de section. Pour un message seul, une citation avec `p.cite`, une question dans une formation, ou l'objectif d'une formation. Le corps peut être vide.

```html
<section class="slide" data-layout="statement" data-section="01 Le problème" data-source="Entretien du 2 septembre 2026">
  <h1>« J'ai lu deux pages et j'ai appelé pour savoir ce qui avait été décidé. »</h1>
  <p class="cite">Responsable de programme, destinataire du compte rendu n° 3</p>
</section>
```

### `chart-insights`

Preuve à gauche (7/12), enseignements à droite (5/12). Une `figure` et une `ul.insights` de deux à quatre éléments. La `figure` contient un SVG, une image ou un tableau.

```html
<section class="slide" data-layout="chart-insights" data-section="…" data-source="…">
  <h1>…</h1>
  <figure><svg viewBox="0 0 677 512">…</svg></figure>
  <ul class="insights">
    <li data-tone="pos"><b>4,7 M€ gagnés</b>Les ventes nouvelles tiennent le plan à 3,9 M€.</li>
    <li data-tone="neg"><b>2,2 M€ perdus</b>L'attrition a doublé en volume.</li>
  </ul>
</section>
```

### `image`

Une preuve sur toute la largeur du corps : capture, photo, document, schéma. Une seule `figure`, avec une `figcaption` facultative.

```html
<section class="slide" data-layout="image" data-section="01 Le problème" data-source="Compte rendu n° 3, corpus anonymisé, juin 2026">
  <h1>Le compte rendu n° 3 place la seule décision de la réunion en avant-dernier paragraphe de la page 2</h1>
  <figure><img src="cr3.png" alt="Page 2 du compte rendu n° 3, décision entourée"><figcaption>Décision entourée en bleu.</figcaption></figure>
</section>
```

### `panels-2`, `panels-3`, `panels-4`

Deux, trois ou quatre panneaux verticaux autonomes. Chaque panneau est une `div.panel` avec un `h2`, puis un contenu : `figure`, liste, paragraphe ou chiffre clé.

```html
<section class="slide" data-layout="panels-3" data-section="…" data-source="…">
  <h1>…</h1>
  <div class="panel"><h2>Churn annuel par segment</h2><figure><svg viewBox="0 0 379 464">…</svg></figure></div>
  <div class="panel"><h2>Contact avant le départ</h2><p class="kpi">68 %<small>des clients perdus sans échange depuis six mois</small></p></div>
  <div class="panel"><h2>Motifs déclarés</h2><ul><li>…</li></ul></div>
</section>
```

### `table`

Un tableau structuré. En-têtes groupés par `colspan` et `rowspan`. Nombres en `class="num"`. Ligne mise en avant en `tr.on`. Total en `tr.total`. Légende facultative en `ul.legend`.

```html
<section class="slide" data-layout="table" data-section="…" data-source="…">
  <h1>…</h1>
  <table>
    <thead>
      <tr><th rowspan="2">Option</th><th colspan="2">Coût sur deux ans</th><th rowspan="2">Retour</th></tr>
      <tr><th class="num">Total</th><th class="num">Par an</th></tr>
    </thead>
    <tbody>
      <tr class="on"><td>Équipe de six CSM</td><td class="num">2,0 M€</td><td class="num">1,0 M€</td><td>20 mois</td></tr>
      <tr><td>Automatisation seule</td><td class="num">0,6 M€</td><td class="num">0,3 M€</td><td>24 mois</td></tr>
    </tbody>
  </table>
</section>
```

### `combo-table`

Un tableau dont des cellules portent une micro-visualisation. `data-bar` (valeur de 0 à 1) donne une micro-barre derrière le texte. `data-level` (entier de 0 à 5) donne des points pleins et vides.

```html
<tr><td>Altaver</td><td class="num">620 K€</td><td data-bar="0.26">26 %</td><td data-level="5"></td><td>Visite sous 15 jours</td></tr>
```

### `framework`

Schéma. Un flux horizontal `div.flow` de `div.box` reliées par des chevrons, ou une grille `div.boxes.cols-3`. La boîte active porte `class="box on"`. Une étiquette `span.tag` ouvre une boîte.

```html
<section class="slide" data-layout="framework" data-section="…" data-frame="B" data-source="…">
  <h1>…</h1>
  <div class="flow">
    <div class="box"><span class="tag">1 · Détecter</span><h3>Score de risque</h3><ul><li>…</li></ul></div>
    <div class="box on"><span class="tag">2 · Intervenir</span><h3>Plan sous 10 jours</h3><ul><li>…</li></ul></div>
    <div class="box"><span class="tag">3 · Développer</span><h3>Expansion</h3><ul><li>…</li></ul></div>
  </div>
</section>
```

### `timeline`

Chronologie horizontale de trois à sept étapes. Une `ol.timeline`. Chaque `li` porte un `time`, un `b` et une ligne. L'étape courante porte `class="on"`.

```html
<section class="slide" data-layout="timeline" data-section="02 Plan" data-source="Direction Clients, plan de déploiement au 30 septembre 2026">
  <h1>Le dispositif couvre les 196 comptes en six mois, avec un pilote sur 40 comptes dès novembre 2026</h1>
  <ol class="timeline">
    <li class="on"><time>Novembre 2026</time><b>Pilote</b>40 comptes, deux CSM en interne.</li>
    <li><time>Janvier 2027</time><b>Recrutements</b>Quatre CSM, vivier qualifié.</li>
    <li><time>Mars 2027</time><b>Couverture complète</b>196 comptes, revue trimestrielle.</li>
    <li><time>Septembre 2027</time><b>Premier bilan</b>Churn trimestriel sous 3 %.</li>
  </ol>
</section>
```

## Emplacement de visuel

Une `figure` contient un seul visuel : un `svg` avec `viewBox`, une `img`, ou un `table`. Une `figcaption` facultative porte une précision : unité, périmètre, élément pointé. Le gabarit met le SVG ou l'image à l'échelle de l'emplacement. Dimensions de l'emplacement, en pixels, pour choisir le `viewBox` :

| Mise en page | Emplacement |
|---|---|
| `chart-insights` | 677 × 512 |
| `image` | 1184 × 512 |
| `panels-2` | 580 × 464 |
| `panels-3` | 379 × 464 |
| `panels-4` | 278 × 464 |

La production du visuel est traitée dans `visuels.md`. Le fichier `assets/exemple.html` montre les treize mises en page remplies.

## Classes utilitaires

| Classe ou attribut | Usage |
|---|---|
| `ul.insights > li[data-tone]` | Enseignement à côté d'une preuve. `data-tone` prend `pos`, `neg`, `s1` à `s4`, `forecast`, `accent`. |
| `div.panel > h2` | Titre d'un panneau. |
| `p.kpi > small` | Chiffre clé et sa phrase. |
| `ul.legend > li[data-tone]` | Légende de couleurs sous un tableau. |
| `td.num`, `th.num` | Colonne numérique, alignée à droite. |
| `tr.on`, `tr.total` | Ligne mise en avant, ligne de total. |
| `div.flow`, `div.boxes.cols-N`, `div.box`, `div.box.on`, `span.tag` | Schéma. |
| `ol.timeline > li[.on]`, `time`, `b` | Chronologie. |
| `p.kicker`, `p.subtitle`, `p.meta`, `p.cite` | Couverture, intercalaire, slide-affirmation. |
| `p.note` | Note en petit. À utiliser avec retenue. |
| `f-*`, `s-*` | Couleurs de la palette dans un SVG (`visuels.md`). |

## Navigation, contrôle, impression

- Flèches, espace, Page suivante et précédente, Début, Fin. L'ancre `#n` ouvre la slide `n`.
- Touche `L`, ou `?lint` dans l'adresse. Le gabarit liste trois défauts : les titres de plus de deux lignes, les corps qui débordent, les emplacements de visuel vides. Il entoure chaque défaut en rouge. La fonction `deckLint()` renvoie la même liste depuis la console.
- Impression : Ctrl ou Cmd + P, une slide par page au format 1280 × 720. Le résultat est un PDF.

## Contrôle statique

```bash
python3 scripts/check_deck.py deck.html storyline.md
```

Le script lit le HTML sans navigateur. Il imprime un constat par ligne : `E` pour une erreur, `W` pour un avertissement. Il renvoie le code 1 si une erreur existe. Le deuxième argument est facultatif. Avec lui, le script compare les titres du squelette aux `h1` du deck, dans l'ordre.

Erreurs :

- section avec `data-example` ;
- nombre de `h1` différent de un, ou titre vide ;
- `data-layout` inconnu ;
- `data-section` absent hors `cover` et `divider` ;
- titre de plus de 160 caractères ;
- corps vide, hors `statement` ;
- `data-source` absent sur une slide avec `figure` ou `table` ;
- `data-frame` absent de la configuration ;
- texte de remplissage : `{{`, `TODO`, `lorem ipsum` ;
- `figure` sans `svg`, `img` ni `table` ; `svg` sans `viewBox` ;
- `exec-summary` sans ses trois blocs ;
- `panels-N` sans N panneaux ;
- `chart-insights` sans figure ou sans enseignements ;
- `image` sans figure unique ;
- `table` ou `combo-table` sans tableau ;
- `combo-table` sans cellule `data-bar` ni `data-level` ;
- `framework` sans boîte ;
- `timeline` hors de trois à sept étapes ;
- titre terminé par « … » sans suite, ou commençant par « … » sans amorce ;
- titres différents du squelette, ou nombre de slides différent.

Avertissements :

- titre de plus de 120 caractères ;
- titre terminé par un point d'interrogation, hors `statement` ;
- première slide de contenu qui n'est pas `exec-summary` ;
- couleurs en dur dans un SVG.

Un avertissement conservé se justifie en une ligne à la livraison.

## Ce qu'il ne faut pas faire

- Modifier le CSS ou le script du gabarit, y compris pour gagner de la place.
- Positionner un élément par un style en ligne. La grille place tout.
- Ajouter une police, une couleur, une ombre, une icône.
- Laisser un visuel sans `viewBox`, ou avec `width` et `height` fixes.
- Écrire un titre différent du titre du squelette. Le squelette change d'abord.
