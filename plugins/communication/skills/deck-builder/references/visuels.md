---
type: "Guide"
description: "Choix, conception et production des preuves visuelles d'un deck construit avec le skill deck-builder : type de preuve selon l'enseignement, graphiques, cascades, prévisions, tableaux, preuves sans chiffre (image, chronologie, citation, exemple, schéma), décor, palette, et moyens de produire le visuel inséré dans le gabarit."
status: "stable"
tags: ["dataviz", "presentation", "communication"]
created: 2026-10-13
---

# Visuels

Une preuve visuelle fait voir un enseignement sans effort. Elle se choisit d'après la nature de cet enseignement, pas d'après le goût. Elle se produit par le moyen adapté au cas, puis s'insère dans l'emplacement `figure` du gabarit.

## Choisir la preuve par l'enseignement

Nomme d'abord ce que le lecteur doit voir. Neuf natures couvrent les cas.

| Nature | Question du lecteur | Preuve | Pourquoi cette preuve |
|---|---|---|---|
| Comparaison | Lequel est le plus grand ? Comment chacun évolue dans le temps ? | Colonnes pour peu de catégories ou une série temporelle. Barres horizontales triées pour des catégories nombreuses ou des libellés longs. | L'œil compare des longueurs alignées sur une base commune avec précision. |
| Composition | De quoi un total est-il fait ? Comment ses parts changent-elles ? | Colonnes empilées quand les totaux comptent. Colonnes 100 % quand seules les parts comptent. Aires empilées pour une évolution continue. | Les parts restent des hauteurs sur une base commune. |
| Variation | Comment passe-t-on d'une valeur de départ à une valeur d'arrivée ? | Cascade de variation | Chaque cause de la variation devient une hauteur isolée. |
| Écart | Que manque-t-il pour atteindre la cible ? | Cascade d'écart | Les leviers acquis et l'écart restant se lisent côte à côte. |
| Relation | Deux variables changent-elles ensemble ? | Nuage de points | La position dans le plan rend la liaison visible, et les exceptions aussi. |
| Distribution | Comment une population se répartit-elle ? | Histogramme par tranches | La fréquence devient une hauteur par tranche. |
| Séquence | Dans quel ordre les choses se passent-elles, ou se feront-elles ? | Chronologie (`timeline`) ; flux de boîtes (`framework`) pour une séquence logique | L'ordre devient une position de gauche à droite. |
| Exemple | À quoi cela ressemble-t-il en vrai ? | Image (capture, photo, document annoté) ; avant-après en deux panneaux | Le lecteur reconnaît le cas réel sans le reconstruire. |
| Témoignage | Qui le dit, et avec quels mots ? | Slide-affirmation avec citation et attribution | La formulation d'origine porte plus que sa paraphrase. |

Règle de passage : une preuve de six valeurs ou moins devient un tableau ou un chiffre clé. Un graphique n'ajoute rien à six valeurs, et il coûte de la place. Une preuve sans valeur numérique devient un exemple, une citation, une image, une chronologie ou un schéma. N'invente pas de chiffre pour obtenir un graphique.

Test : le lecteur énonce l'enseignement en regardant la preuve, avant de lire le titre. S'il doit lire le titre pour comprendre la preuve, la preuve est mal choisie.

## Interdits

- **Camembert et anneau.** L'œil ne mesure pas un angle ni une surface. Deux parts de 28 % et 33 % se confondent. Les étiquettes s'entassent autour du cercle. Un cercle dans un rectangle gaspille un tiers de l'emplacement. Remplace-le par des barres horizontales triées.
- **Relief, ombres, dégradés.** Ils déforment les hauteurs que le lecteur compare.
- **Double axe vertical.** Le lecteur ne sait pas quelle courbe lit quel axe. L'échelle choisie fabrique la corrélation. Fais deux graphiques côte à côte, ou indexe les deux séries en base 100.
- **Axe tronqué sans mention.** Il amplifie une variation. Si l'axe ne part pas de zéro, écris-le sur l'axe.
- **Plus de quatre séries.** Au-delà, les couleurs ne se distinguent plus et la légende remplace la lecture. Regroupe, ou fais plusieurs petits graphiques.
- **Légende quand l'étiquette suffit.** Étiquette la série au bout de sa courbe ou sur sa colonne.
- **Image de décoration.** Une image qui ne prouve pas le titre n'est pas sur la slide.

## Cascades

Une cascade montre comment des composantes s'additionnent. Trois formes existent.

| Forme | Montre | Première colonne | Dernière colonne |
|---|---|---|---|
| Construction | Les contributions qui forment un total | Première contribution | Total |
| Variation | Le passage d'une valeur initiale à une valeur finale, par ses causes | Valeur initiale | Valeur finale |
| Écart | Les leviers acquis et ce qui reste à combler pour atteindre une cible | Situation actuelle | Cible, précédée de la colonne d'écart |

Règles :

1. Couleurs fixes : contributions positives en `pos`, négatives en `neg`, totaux en `neutral`, cible en `accent`, colonne d'écart blanche avec une bordure pointillée `neg`. Le lecteur lit le signe avant le chiffre.
2. Une flèche d'écart entre la première et la dernière colonne, avec la différence en valeur et en pourcentage. Cette différence est le chiffre du titre.
3. Un ou deux commentaires au plus, au-dessus des colonnes qui expliquent le plus la variation. Un commentaire nomme la cause en moins de dix mots.
4. Chaque colonne porte sa valeur. Un connecteur fin relie le haut d'une colonne au pied de la suivante.
5. Ne force pas la cascade. Si la donnée n'a pas de logique de cumul, elle est une comparaison : utilise des colonnes simples.

Pourquoi : la cascade isole chaque cause comme une hauteur. Le lecteur identifie la cause principale en une seconde. Sans logique de cumul, la cascade fabrique une addition qui n'existe pas, et le lecteur cherche un sens absent.

Signe de réussite : le lecteur nomme la cause principale de la variation sans lire les commentaires.

## Prévisions

Chaque valeur projetée se distingue d'une valeur constatée. Trois moyens existent.

| Moyen | Geste | Quand |
|---|---|---|
| Couleur et fond | Les colonnes projetées prennent la couleur `forecast`. Un fond `shade` couvre la zone projetée. Le mot « Prévision » est écrit dans le fond. | Une seule trajectoire. Une audience qui doit voir la frontière sans effort. |
| Traits pointillés | La partie projetée d'une courbe passe en pointillés. Plusieurs scénarios prennent des longueurs de tiret différentes. | Plusieurs scénarios sur un même graphique. Impression en noir et blanc. |
| Suffixe sur l'étiquette | L'étiquette d'axe porte `F` (prévision), `E` (estimation) ou `T` (cible) : `2027F`. | Toute prévision, en complément des deux autres moyens. Seul, quand la continuité visuelle compte plus que la frontière. |

Arbitrage : devant un comité d'audit, de risques ou une audience financière, marque franchement : couleur, fond et suffixe. La crédibilité se joue sur la frontière entre fait et projection. Devant une audience commerciale, ou pour montrer un élan, le suffixe seul garde la continuité de la trajectoire sans cacher la nature de la donnée. Ne descends jamais sous le suffixe.

Signe de réussite : la frontière entre constaté et projeté se voit sans légende.

## Tableaux

### Tableau structuré

Pour une donnée matricielle que le lecteur compare ligne à ligne. Règles :

1. Une hiérarchie d'en-têtes : un en-tête de groupe au-dessus de ses colonnes. Le lecteur voit la structure avant les valeurs.
2. Les nombres alignés à droite, avec la même précision dans toute la colonne.
3. Une ligne mise en avant quand une option est recommandée. Une ligne de total quand le total a un sens.
4. Une légende de couleurs seulement si une couleur porte une information.
5. Huit lignes au plus. Au-delà, le tableau va en annexe.

Pourquoi : un tableau brut demande au lecteur de construire la comparaison. Les en-têtes groupés, l'alignement et la ligne mise en avant font la comparaison à sa place.

### Tableau combiné

Un tableau structuré dont des cellules portent une micro-visualisation. Une micro-barre montre un poids ou un pourcentage. Un niveau sur cinq montre un score ou un risque. Le gabarit les rend à partir des attributs `data-bar` et `data-level` (`gabarit.md`).

Pourquoi : la micro-barre permet de comparer les lignes d'un coup d'œil sans quitter le tableau. Une colonne de chiffres demande une lecture ligne à ligne.

## Preuves sans chiffre

### Image

Une capture d'écran, une photo, un document, un schéma existant. Mise en page `image` (plein corps) ou `chart-insights` (image à gauche, enseignements à droite). Règles :

1. L'image prouve le titre. Si le lecteur ne voit pas dans l'image ce que le titre affirme, l'image n'est pas la bonne.
2. Entoure ou pointe l'élément à voir. Un cadre `accent` ou une flèche, pas plus.
3. Recadre sur l'élément à voir. Une page entière pour montrer un paragraphe est une image mal cadrée.
4. Une image par slide. Deux images font un avant-après en `panels-2`.
5. Donne la source dans le pied : le document, la date, l'auteur.

### Chronologie

Une suite d'événements ou de jalons, de trois à sept. Mise en page `timeline`. Règles :

1. Chaque étape porte une date ou un rang, un titre court, et une ligne.
2. L'étape où l'audience se trouve est mise en avant (`class="on"`).
3. Les étapes sont à égale distance. Si la durée réelle compte, écris-la dans l'étape ; ne déforme pas les espacements.

### Citation

Les mots d'une personne, avec son nom et sa fonction. Mise en page `statement`. Règles :

1. Cite les mots exacts. Une citation reformulée est une paraphrase, et elle se présente comme telle.
2. Trente mots au plus. Au-delà, coupe avec des points de suspension entre crochets.
3. L'attribution est sous la citation : nom, fonction, date.
4. Une citation prouve un ressenti ou une position. Elle ne prouve pas un fait : un fait a besoin d'une autre preuve.

### Exemple et avant-après

Un cas réel qui montre le message. Mise en page `panels-2` (avant, après) ou `chart-insights` (le cas à gauche, ce qu'il montre à droite). Règles :

1. L'exemple est réel et daté. Un exemple inventé est annoncé comme fictif.
2. L'avant et l'après montrent la même chose, dans la même forme. Seul le point à voir change.
3. Un exemple illustre. Il ne prouve pas une généralité : pour une généralité, ajoute une preuve de portée (combien de cas, sur quelle période).

### Schéma

Un modèle, une organisation, une séquence logique. Mise en page `framework`. Règles :

1. Trois à cinq boîtes. Au-delà, le modèle est trop complexe pour une slide.
2. Chaque boîte porte un titre court et deux ou trois lignes.
3. Le sens de lecture est unique : de gauche à droite, ou de haut en bas.
4. La boîte que la section détaille est mise en avant (`class="box on"`).

Pourquoi : la forme porte la structure. Un flux dit « séquence ». Une grille dit « composantes ». Si la forme contredit le propos, le lecteur retient la forme.

## Graphique et enseignements côte à côte

La mise en page `chart-insights` place la preuve à gauche et deux à quatre enseignements à droite. Règles :

1. Chaque enseignement commence par un titre court en gras, suivi d'une phrase.
2. L'enseignement porte la couleur de la série ou de la colonne qu'il commente (`data-tone`). Le lecteur relie le texte à la preuve sans chercher.
3. L'ordre des enseignements suit l'ordre de lecture de la preuve. Cet ordre va de gauche à droite, ou de la plus grande valeur à la plus petite.
4. Aucun enseignement ne répète le titre. Chacun ajoute une précision ou une cause.

## Décor

Sur une preuve visuelle : une flèche d'écart au plus, deux commentaires au plus, les valeurs sur les marques, un axe de base. Rien d'autre. Pas de quadrillage, sauf pour un nuage de points. Pas d'icône, pas de logo, pas de bordure autour du graphique.

Pourquoi : chaque élément ajouté entre en concurrence avec le message pour l'attention. Test : retire l'élément. Si aucune information ne disparaît, l'élément ne revient pas.

## Palette

Le gabarit définit la palette en variables CSS et en classes pour les SVG. Aucune autre couleur n'entre dans le deck.

| Nom | Classes SVG | Rôle |
|---|---|---|
| `s1` à `s4` | `f-s1`… `f-s4`, `s-s1`… `s-s4` | Séries, dans l'ordre d'importance : `s1` bleu accent, `s2` gris, `s3` bleu foncé, `s4` gris clair |
| `pos`, `neg` | `f-pos`, `f-neg`, `s-pos`, `s-neg` | Variation positive, variation négative |
| `neutral` | `f-neutral`, `s-neutral` | Totaux, éléments sans signe |
| `forecast` | `f-forecast`, `s-forecast` | Valeurs projetées |
| `accent` | `f-accent`, `s-accent` | Cible, élément mis en avant, cadre sur une image |
| `ink`, `muted`, `line`, `shade` | `f-ink`, `f-muted`, `s-line`, `f-shade` | Texte, texte secondaire, axes et connecteurs, fond de zone projetée |

Pour mettre une valeur en avant parmi d'autres : la valeur en `s1`, les autres en `s4`. Pour un graphique à une série : `s1`.

Pourquoi : une palette courte rend chaque couleur signifiante. Le vert dit « gain » partout. Le bleu clair dit « projeté » partout. Une couleur nouvelle oblige le lecteur à apprendre un code pendant la lecture.

## Produire le visuel

Le gabarit ne dessine rien. Le visuel se produit par le moyen adapté au cas, dans cet ordre de préférence.

1. **Tableau ou chiffre clé** quand la preuve tient en six valeurs ou moins. Balisage dans `gabarit.md`.
2. **SVG écrit pour le cas** pour les colonnes, les barres, les cascades, les courbes, les nuages de points. Le SVG est écrit dans la section, avec les classes de la palette. Règles d'écriture ci-dessous.
3. **Outil externe** quand le visuel est complexe : carte, petits multiples, nombreuses séries. Utilise un skill ou une bibliothèque de visualisation, ou un tableur. Exporte en SVG de préférence, en PNG à double résolution sinon. Insère le SVG dans la section et remplace ses couleurs par les classes de la palette, ou insère l'image par `img`. Une couleur en dur qui reste déclenche un avertissement du contrôle : justifie-le.
4. **Image fournie ou capturée** : capture d'écran, photo, document. Insère-la par `img`, avec sa source dans le pied.

### Écrire un SVG pour le cas

1. Donne au SVG un `viewBox` aux dimensions de l'emplacement. La table des emplacements est dans `gabarit.md`. N'écris pas d'attributs `width` ni `height`. Le gabarit met le SVG à l'échelle.
2. Mets les couleurs par les classes `f-*` (fond) et `s-*` (trait). N'écris aucune couleur en dur.
3. Écris les valeurs sur les marques, en 12 unités au moins, en `ink`. Écris les étiquettes de catégorie sous l'axe, en `muted`.
4. Trace l'axe de base en `s-ink`. N'ajoute pas de quadrillage pour des colonnes ou des barres.
5. Trie les barres horizontales par valeur décroissante, sauf si l'ordre des catégories porte un sens (temps, étapes).
6. Étiquette chaque série au bout de sa courbe ou sur sa colonne, pas dans une légende.
7. Pour une prévision : fond `f-shade` sur la zone projetée, colonnes projetées en `f-forecast`, courbe projetée en `stroke-dasharray`, suffixe sur les étiquettes.
8. Pour une cascade : applique les règles de la section « Cascades ». La flèche d'écart utilise un `marker` défini dans le SVG.
9. Garde le texte dans le SVG, jamais dans une image. Le texte reste lisible, sélectionnable et imprimable.

Squelette minimal d'un graphique à colonnes :

```html
<figure>
  <svg viewBox="0 0 677 512" role="img" aria-label="ARR par année, en millions d'euros">
    <text x="0" y="13" class="f-muted">M€</text>
    <rect x="60" y="212" width="64" height="260" class="f-s1"/>
    <text x="92" y="204" text-anchor="middle">16,3</text>
    <text x="92" y="494" text-anchor="middle" class="f-muted">2024</text>
    <!-- autres colonnes -->
    <line x1="8" x2="668" y1="472" y2="472" class="s-ink"/>
  </svg>
</figure>
```

### Liste de contrôle d'une preuve visuelle

1. La nature de l'enseignement est nommée. Le type de preuve en découle.
2. Le titre de la slide se lit sur la preuve : l'élément spécifique du titre y est visible.
3. Les valeurs sont écrites sur les marques, ou l'élément à voir est pointé sur l'image.
4. Une seule unité, écrite une fois.
5. Les prévisions sont distinguées.
6. Les couleurs viennent de la palette et portent un sens.
7. Une flèche au plus, deux commentaires au plus.
8. La source est dans le pied de la slide.
