# Framework Universel UI — 6 Dimensions

Référence complète des 6 dimensions universelles pour l'analyse d'interface.

## Table des matières

1. [Dimension Structurelle](#1-dimension-structurelle)
2. [Dimension Interactive](#2-dimension-interactive)
3. [Dimension Esthétique](#3-dimension-esthétique)
4. [Dimension Informationnelle](#4-dimension-informationnelle)
5. [Dimension Temporelle](#5-dimension-temporelle)
6. [Dimension Logique](#6-dimension-logique)
7. [Taxonomie MECE](#taxonomie-mece)

---

## 1. Dimension Structurelle

**Objet** : Architecture spatiale et hiérarchie visuelle.

### Éléments à analyser

- **Layout global** : Grid system (colonnes, gouttières), zones principales (header, nav, content, sidebar, footer)
- **Hiérarchie spatiale** : Nesting des conteneurs, profondeur z-index, priorité visuelle
- **Responsive behavior** : Breakpoints observables, stack/flow patterns, éléments qui disparaissent/apparaissent
- **Spacing system** : Marges, paddings, gaps — identifier le système (4px, 8px, etc.)
- **Alignment** : Axes d'alignement, grilles implicites, centres visuels

### Spécifications attendues

```
- Grid: [colonnes] x [colonnes] avec gap de [X]px
- Conteneur principal: max-width [X]px, padding [X]px
- Sections: [liste avec dimensions observées]
- Z-index layers: [ordre des couches si superposition visible]
```

---

## 2. Dimension Interactive

**Objet** : Patterns comportementaux, états et feedback utilisateur.

### Éléments à analyser

- **Éléments cliquables** : Boutons, liens, toggles, dropdowns — identifier par affordance visuelle
- **États observables** : Default, hover, active, disabled, focus, selected, error
- **Formulaires** : Inputs, selects, checkboxes, radios — labels, placeholders, validation
- **Navigation** : Menus, breadcrumbs, tabs, pagination — état actif/inactif
- **Feedback patterns** : Loaders, toasts, modals, tooltips visibles

### Spécifications attendues

```
- Boutons: [types observés] avec états [listés]
- Inputs: [types] avec [placeholder/label visibles]
- Navigation: [pattern] avec [X] items, actif = [style]
- Éléments interactifs marqués [Non observable] si état unique visible
```

**Note** : Si un seul état est visible, le décrire et marquer les autres comme inférés.

---

## 3. Dimension Esthétique

**Objet** : Système de design et cohérence visuelle.

### Éléments à analyser

- **Palette couleurs** : Couleurs principales, secondaires, neutres, accent — en hex
- **Typographie** : Familles, tailles (px/rem), poids (weight), line-height, letter-spacing
- **Iconographie** : Style (outline, filled, duotone), taille, cohérence du set
- **Ombres et élévation** : Box-shadow values, layers d'élévation
- **Bordures et radius** : Border-radius system, border styles et couleurs
- **Images et médias** : Ratios, traitements (overlay, crop, filter), placeholders

### Spécifications attendues

```
Couleurs:
  - Primary: #XXXXXX
  - Secondary: #XXXXXX
  - Background: #XXXXXX
  - Text: #XXXXXX
  - Accent: #XXXXXX

Typographie:
  - H1: [family], [size]px, weight [X], color #XXXXXX
  - H2: [family], [size]px, weight [X], color #XXXXXX
  - Body: [family], [size]px, weight [X], line-height [X]
  - Caption: [family], [size]px, weight [X], color #XXXXXX

Radius: [X]px (small), [X]px (medium), [X]px (large)
Shadow: [values observées]
```

---

## 4. Dimension Informationnelle

**Objet** : Organisation et présentation du contenu.

### Éléments à analyser

- **Hiérarchie de contenu** : Titres, sous-titres, corps, métadonnées — ordre de lecture
- **Densité informationnelle** : Ratio contenu/espace blanc, charge cognitive
- **Patterns de contenu** : Cards, lists, tables, grids de contenu, accordéons
- **Données structurées** : Tableaux, graphiques, statistiques, KPIs
- **Micro-contenu** : Labels, badges, tags, tooltips, empty states
- **Localisation visible** : Langue, format dates/nombres, monnaie

### Spécifications attendues

```
- Zones de contenu: [liste avec type et rôle]
- Pattern dominant: [card | list | table | grid]
- Niveaux de hiérarchie: [X] niveaux observés
- Données visibles: [types et format]
- Empty states: [observé/non observé]
```

---

## 5. Dimension Temporelle

**Objet** : États dynamiques et transitions.

### Éléments à analyser

- **États dynamiques visibles** : Loading, skeleton screens, progress bars, états de transition
- **Animations implicites** : Éléments qui suggèrent une animation (ombre portée, position décalée)
- **Notifications** : Badges compteurs, indicateurs temps réel, alertes
- **Progression** : Steppers, wizards, progress indicators
- **Temps réel** : Indicateurs de mise à jour live, timestamps "il y a X min"

### Spécifications attendues

```
- États dynamiques observés: [liste]
- Animations probables: [inférences marquées comme telles]
- Indicateurs temporels: [timestamps, compteurs, badges]
- Transitions suggérées: [durée estimée, easing probable]
```

**Note** : Cette dimension contient souvent le plus d'inférences. Marquer systématiquement ce qui est observé vs supposé.

---

## 6. Dimension Logique

**Objet** : Modèles de données et règles métier.

### Éléments à analyser

- **Entités de données** : Objets métier visibles (user, product, order, etc.)
- **Relations** : Liens entre entités (1:1, 1:N, N:N) déductibles de l'interface
- **Règles métier** : Validations, contraintes, conditions visibles
- **Flux utilisateur** : Parcours implicite, étapes, points de décision
- **Permissions** : Rôles, accès conditionnels, éléments grisés/masqués

### Spécifications attendues

```
- Entités identifiées: [liste avec attributs visibles]
- Relations: [entité A] → [entité B] (type)
- Règles métier: [contraintes observables]
- Flux: [étape 1] → [étape 2] → [étape N]
- Permissions: [inférences sur rôles si visible]
```

---

## Taxonomie MECE

Chaque analyse doit respecter le principe MECE (Mutually Exclusive, Collectively Exhaustive) :

### Validation exhaustivité

- Les 6 dimensions sont-elles couvertes ?
- Chaque élément visible est-il classé dans au moins une dimension ?
- Les dimensions marquées [Non observable] sont-elles justifiées ?

### Validation orthogonalité

- Un même élément n'est-il décrit qu'une fois dans sa dimension principale ?
- Les cross-references entre dimensions sont-elles explicites ?

### Hiérarchisation par priorité d'implémentation

Ordre recommandé :
1. **Structurel** → Le squelette en premier
2. **Esthétique** → Le système de design (couleurs, typo, spacing)
3. **Informationnel** → Le contenu et sa structure
4. **Interactif** → Les comportements et états
5. **Temporel** → Les animations et transitions
6. **Logique** → La couche données et métier
