---
name: ui-to-spec
description: "Système d'analyse UI/UX pour reproduction fidèle d'interfaces. Browse autonomement les sites web via playwright-cli pour capturer et analyser les interfaces, ou accepte des screenshots fournis. Décompose toute interface (web, mobile, desktop) en spécification technique complète selon un Framework Universel à 6 dimensions. Utiliser ce skill quand : (1) l'utilisateur donne une URL à analyser, (2) l'utilisateur fournit un screenshot d'interface, (3) l'utilisateur veut reproduire ou cloner une interface existante, (4) l'utilisateur demande un benchmark UI/UX, (5) l'utilisateur a besoin de spécifications techniques depuis un visuel ou une URL, (6) l'utilisateur veut décomposer un design en composants implémentables. Triggers : 'analyse cette interface', 'analyse ce site', 'benchmark UI', 'reproduire ce design', 'spécifications depuis screenshot', '/ui-to-spec'."
license: Apache-2.0
metadata:
  version: "0.1.0"
  author: "AIEN"
  tags: ["ui", "design", "specification"]
---

# UI to Spec

Moteur d'analyse UI transformant une interface (URL ou screenshot) en spécification technique complète, exploitable par un développeur pour reproduction fidèle.

**Prerequis.** Le mode browsing autonome appelle le binaire `playwright-cli`, qui doit etre installe sur la machine. Sans lui, seul le mode screenshot fonctionne.

## Workflow

### 1. Acquérir l'interface

Deux modes d'acquisition — choisir automatiquement selon l'input utilisateur :

#### Mode A : Browsing autonome (URL fournie)

Utiliser le skill `playwright-cli` pour naviguer et capturer l'interface.

**Séquence d'acquisition :**

```bash
# 1. Ouvrir le navigateur et naviguer
playwright-cli open <URL>

# 2. Capturer le snapshot (structure DOM + refs éléments)
playwright-cli snapshot

# 3. Prendre un screenshot visuel
playwright-cli screenshot

# 4. Si page longue, scroller et capturer plusieurs zones
playwright-cli eval "window.scrollBy(0, 800)"
playwright-cli screenshot
playwright-cli snapshot

# 5. Explorer les états interactifs visibles
playwright-cli hover e<ref>      # hover sur éléments clés
playwright-cli screenshot        # capturer l'état hover
playwright-cli click e<ref>      # ouvrir dropdowns, modals
playwright-cli screenshot        # capturer l'état ouvert

# 6. Tester le responsive si pertinent
playwright-cli eval "document.documentElement.style.width='768px'"
playwright-cli screenshot
playwright-cli eval "document.documentElement.style.width='375px'"
playwright-cli screenshot

# 7. Extraire les styles computés via JS
playwright-cli eval "JSON.stringify(window.getComputedStyle(document.querySelector('<selector>')))"

# 8. Fermer
playwright-cli close
```

**Avantages du browsing** : Accès au DOM réel, styles computés, états interactifs (hover, focus, open), responsive, et données structurées.

#### Mode B : Screenshot fourni

Si l'utilisateur fournit une image/screenshot, analyser directement le visuel sans browsing.

#### Mode C : Hybride

L'utilisateur fournit une URL + un screenshot de référence. Browser le site ET comparer avec le screenshot pour une analyse plus complète.

### 2. Paramétrer l'analyse

- **interface_type** : `web_responsive` | `mobile_app` | `desktop_app` (défaut : web_responsive)
- **framework** : `react` | `vue` | `angular` | `vanilla` | `auto-detect` (défaut : auto-detect)
- **fidelity_level** : `pixel_perfect` | `high_fidelity` | `conceptual` (défaut : high_fidelity)
- **developer_expertise** : `senior` | `intermediate` | `junior` (défaut : intermediate)

Si paramètres non fournis, utiliser les défauts. En mode browsing, tenter de détecter le framework via le DOM :

```bash
# Détecter le framework automatiquement
playwright-cli eval "!!document.querySelector('[data-reactroot], #__next') ? 'react/next' : !!document.querySelector('[data-v-], #app[data-v-]') ? 'vue' : !!document.querySelector('app-root, [ng-version]') ? 'angular' : 'vanilla'"
```

### 3. Analyser selon les 4 phases

1. **Inventaire** : Lister exhaustivement tous les éléments visibles (snapshot DOM en mode browsing, observation visuelle en mode screenshot)
2. **Classification** : Classer chaque élément selon les 6 dimensions universelles (voir [references/framework-6d.md](references/framework-6d.md))
3. **Principes** : Identifier les principes de design sous-jacents
4. **Spécification** : Produire les specs techniques détaillées

Appliquer l'approche Dual-Layer sur chaque dimension :
- **Layer Causal** : POURQUOI cette interface fonctionne (principes cognitifs)
- **Layer Procédural** : COMMENT l'implémenter (spécifications techniques)

**Bonus mode browsing** : Extraire les valeurs réelles via `playwright-cli eval` :

```bash
# Couleurs, fonts, spacing réels
playwright-cli eval "const s = getComputedStyle(document.querySelector('h1')); JSON.stringify({font: s.fontFamily, size: s.fontSize, weight: s.fontWeight, color: s.color, lineHeight: s.lineHeight})"

# Grid/layout réel
playwright-cli eval "const s = getComputedStyle(document.querySelector('.container')); JSON.stringify({display: s.display, gridCols: s.gridTemplateColumns, gap: s.gap, maxWidth: s.maxWidth, padding: s.padding})"
```

### 4. Structurer l'output

Produire l'analyse structurée selon ce format obligatoire :

```
## 1. Dimension Structurelle
[Architecture spatiale, grilles, hiérarchie]

## 2. Dimension Interactive
[Patterns comportementaux, états, feedback]

## 3. Dimension Esthétique
[Système de design, couleurs hex, typographie, spacing]

## 4. Dimension Informationnelle
[Organisation contenu, hiérarchie info, densité]

## 5. Dimension Temporelle
[États dynamiques, transitions, animations]

## 6. Dimension Logique
[Modèle de données, règles métier, flux]

## Synthèse Développeur
[Ordre d'implémentation, code snippets, points de validation]
```

Chaque section doit contenir des mesures exactes (px, %, rem, hex colors), des code snippets si pertinent, et être marquée `[Non observable]` si l'information n'est pas visible.

Pour les spécifications détaillées de chaque dimension, consulter [references/framework-6d.md](references/framework-6d.md).

### 5. Valider avant livraison

Checklist de validation systématique :

- [ ] 6/6 dimensions couvertes (ou marquées [Non observable])
- [ ] Zéro information inventée — tout est basé sur l'observation directe
- [ ] Spécifications suffisantes pour implémentation autonome
- [ ] Distinction claire entre faits observés et inférences (marquées "Probablement", "Semble être")
- [ ] Ordre d'implémentation recommandé inclus
- [ ] Code snippets pour les patterns complexes
- [ ] En mode browsing : valeurs CSS extraites du DOM (pas estimées)

## Règles critiques

### Anti-hallucination

- Baser TOUTES les affirmations sur éléments VISIBLES (screenshot) ou MESURÉS (DOM/computed styles)
- Ne JAMAIS inventer interactions, états ou comportements non observés
- Élément flou/ambigu → indiquer clairement : "Élément X partiellement visible"
- Distinguer explicitement : **observé** vs **mesuré via DOM** vs **inféré**

### Gestion de problèmes

- **URL inaccessible** → Signaler l'erreur, proposer de fournir un screenshot
- **Page avec auth** → Signaler, demander credentials ou screenshot post-login
- **SPA avec chargement dynamique** → Attendre le rendu : `playwright-cli eval "await new Promise(r => setTimeout(r, 3000))"` puis snapshot
- **Image floue** → "Zone [X] illisible. Image plus nette nécessaire."
- **Interface partielle** → "Analyse basée sur zone visible."
- **Complexité excessive** → "Analyse par zones prioritaires."

### Ton et format

- Ton technique expert, vocabulaire développeur
- Chaque description doit permettre implémentation directe
- Factuel, sans opinion subjective sur esthétique
- Mesures exactes : px, %, rem, couleurs hex

## Adaptation par framework

Adapter les code snippets et patterns selon le framework cible :

- **React** → Component structure, props, state management, hooks
- **Vue** → Composition API, reactive data, template syntax
- **Angular** → Modules, services, directives, decorators
- **Vanilla** → Pure HTML/CSS/JS, sans hypothèse de framework

Pour les patterns détaillés par framework, consulter [references/framework-patterns.md](references/framework-patterns.md).

## Adaptation par niveau d'expertise

- **Senior** → Patterns avancés, optimisations, architecture complexe
- **Intermediate** → Bonnes pratiques, explications techniques modérées
- **Junior** → Instructions détaillées, exemples de code complets, best practices expliquées
