---
name: deck-builder
description: >
  Deck Builder — Construit avec l'utilisateur, sur tout sujet, un deck qui porte un message et
  obtient un effet : décision, adhésion, compréhension ou action. Méthode en cinq états validés
  un par un : cadrage, storyline en markdown (récit Situation-Complication-Résolution, plan
  Dot-Dash), squelette, deck HTML sur un gabarit à grille fixe, révision. Un script contrôle la
  structure du deck. Chaque règle donne le geste et la raison, pour adapter le geste quand le
  cas sort du standard. Utilise ce skill quand l'utilisateur veut un deck, des slides, une
  présentation pour un comité, une direction, une équipe, un client ou des apprenants, ou dit
  « fais-moi un deck », « prépare les slides », « présentation pour le COMEX », « deck builder ».
  Ne l'utilise pas pour un discours sans support, pour un support de conférence fait d'images
  plein écran, ni pour un support d'atelier.
license: Apache-2.0
metadata:
  version: "0.1.0"
  author: "L'Autre Intelligence & Nous"
  tags: "presentation, slides, communication"
---

# Deck Builder

Tu construis un deck avec l'utilisateur. Un deck porte un message et obtient un effet sur une audience. L'effet est une décision, une adhésion, une compréhension ou une action. Chaque règle de ce skill sert cet effet. Si une règle gêne, reviens à l'effet attendu. L'effet attendu tranche.

Tu travailles en deux temps. D'abord, tu écris le récit en texte. Ensuite, tu construis les slides. L'utilisateur valide le texte avant la première slide.

## Pourquoi le texte avant les slides

Une faille logique se corrige en une ligne dans un texte. La même faille se corrige en une heure dans un deck. La mise en page cache les failles : un visuel soigné donne l'impression d'une preuve. Un texte montre une affirmation sans preuve. Pour cette raison, aucune slide n'existe avant la validation du storyline, et chaque révision de fond passe par le storyline.

## Les trois objets

| Objet | Rôle | Emplacement |
|---|---|---|
| `storyline.md` | Le contrat : cadrage, récit, plan Dot-Dash, squelette. Tout ce que le deck dit, dans l'ordre du deck. | Dossier de travail |
| `deck.html` | Le produit : une copie de `assets/deck.html` remplie de sections. Un seul fichier, sans dépendance. Il s'ouvre dans un navigateur et s'imprime en PDF. | Dossier de travail |
| `scripts/check_deck.py` | La porte : le script contrôle la structure du deck et sa concordance avec le squelette. Zéro erreur avant la livraison. | Skill |

Le dossier de travail est le dossier que l'utilisateur désigne. Sans indication, crée un dossier au nom du sujet dans le répertoire courant.

Trois références détaillent les objets. Lis une référence au moment où tu en as besoin.

- `references/format-storyline.md` : le format du storyline, élément par élément, avec deux exemples.
- `references/visuels.md` : le choix, la conception et la production de chaque preuve visuelle.
- `references/gabarit.md` : les règles du gabarit, le balisage des treize mises en page, le contrôle.
- `assets/exemple.html` et `assets/exemple-storyline.md` : un deck complet de quatorze slides et son storyline. Ouvre-les pour voir chaque mise en page et un SVG écrit pour le cas.

## Les genres de deck

Un deck a un genre. Le genre fixe l'effet attendu, l'ouverture du deck et la preuve typique. Déclare le genre au cadrage. Les neuf règles s'appliquent à tous les genres. La table donne les adaptations.

| Genre | Effet attendu | Ouverture | Preuve typique |
|---|---|---|---|
| Décision | Une décision de la personne clé | Résumé exécutif : la réponse d'abord | Chiffre, comparaison d'options, trajectoire |
| Information (annonce, bilan, point d'étape) | Une compréhension partagée | Résumé exécutif : le message principal d'abord | Fait daté, chiffre, exemple |
| Pilotage (comité de projet) | Une décision sur les points bloqués | Résumé exécutif : état, écarts, décisions demandées | Avancement, écart au plan, risque |
| Pitch (investisseur, sponsor) | Un engagement | Résumé exécutif : la demande et la promesse d'abord | Traction, marché, équipe |
| Commercial (proposition) | Un accord du client | Résumé exécutif : le problème du client, puis la réponse | Cas client, démonstration, chiffre |
| Retour d'expérience | Des enseignements adoptés | Résumé exécutif : les enseignements d'abord | Chronologie, exemple, chiffre |
| Formation | Une capacité acquise | Slide « ce que vous saurez faire », puis une progression concept par concept | Exemple, démonstration, exercice |

Pour la formation, la règle « la réponse d'abord » s'applique au deck entier : la première slide annonce l'objectif. Elle ne s'applique pas à chaque section : une section construit un concept avant d'en donner l'usage.

## Déroulé

Le déroulé a cinq états. Chaque état se termine par une validation de l'utilisateur. À chaque validation, pose une seule question fermée. N'avance pas sans réponse : chaque état s'appuie sur l'état précédent.

Point d'entrée : si l'utilisateur apporte un storyline validé, commence à l'état 2. S'il apporte un deck à réviser, reconstitue le squelette depuis les titres du deck, puis commence à l'état 4.

### État 0 — Cadrer

1. Reformule le besoin en une phrase : « Si je comprends bien, il faut obtenir [effet] de [audience] à partir de [matière disponible]. »
2. Lis la matière que l'utilisateur a fournie : fichiers, notes, analyses. Pose seulement les questions que la matière ne règle pas. Pose-les en un seul message, quatre au plus :
   - Quel effet le deck doit-il obtenir, et de qui ?
   - Quel est le genre du deck ?
   - Quelle question l'audience se pose-t-elle, dans ses mots ?
   - Quelle matière existe : faits, chiffres, exemples, sources ? Quelle matière manque ?
   - Quelles contraintes : langue, durée, nombre de slides, date, audience acquise ou hostile ?
3. Qualifie le cas :
   - **Sans chiffres** : les preuves sont des faits datés, des exemples, des citations, des images, des démonstrations. N'invente aucun chiffre. Une estimation est marquée comme estimation, avec son hypothèse.
   - **Audience hostile à la conclusion** : garde la réponse en tête de deck. Dans le résumé exécutif, écris une Situation et une Complication que l'audience admet. L'audience acquiesce avant de lire la Résolution.
   - **Formation** : l'ouverture annonce la capacité visée. Chaque section construit un concept, puis donne son usage.

Pourquoi : le deck entier dérive de l'effet attendu et de l'audience. L'ouverture s'écrit pour la personne clé. Les titres répondent à sa question. Le niveau de détail suit ce qu'elle sait déjà. Sans ce cadrage, tu produis un document, pas un deck.

### État 1 — Écrire le storyline

Écris `storyline.md` selon `references/format-storyline.md` : Cadrage, Récit, Dot-Dash. N'écris pas le squelette à cet état.

- **Récit** : quatre parties, sur une page, lues d'une traite.
  - Situation : le contexte que l'audience admet.
  - Complication : ce qui a changé et rend l'action nécessaire.
  - Question : la question que la complication fait naître.
  - Résolution : la réponse et ce qu'elle implique.
- **Dot-Dash** : chaque affirmation clé est un Dot. Un Dot est une phrase complète et spécifique. Il devient un titre d'action. Sous chaque Dot, écris des Dashes : les preuves, leur source, et le visuel que chaque preuve devient. Un Dot sans Dash est supprimé, ou devient une question posée à l'utilisateur.

Validation : l'utilisateur lit la page et valide la logique. Ne produis rien d'autre avant cette validation.

Pourquoi : la séquence Situation, Complication, Résolution est le mécanisme d'un récit. Une base stable, une rupture qui crée une tension, puis la réponse qui résout la tension. Le lecteur veut la suite parce que la complication le concerne. Le Dot-Dash interdit la slide sans preuve : la preuve est exigée au moment où l'affirmation s'écrit, quand sa suppression ne coûte rien.

### État 2 — Dessiner le squelette

Ajoute au storyline la section `## Squelette` : une table, une ligne par slide. Chaque ligne donne le numéro, la section, le titre d'action, la mise en page, la preuve et la source. Règles :

1. La première slide de contenu est l'ouverture du genre : un résumé exécutif autonome, ou la slide d'objectif pour une formation. Un lecteur qui lit cette seule slide connaît le message principal et ce que le deck attend de lui.
2. L'ordre suit la pyramide : la réponse, puis les raisons, puis les preuves. Un Dot devient une slide. Un Dash devient le corps de cette slide, ou un panneau si plusieurs Dashes prouvent le même Dot.
3. Au-delà de huit slides, divise le deck en sections. Chaque section commence par un intercalaire. Chaque slide porte l'indicateur de sa section.
4. Chaque ligne choisit une mise en page du gabarit et un type de preuve visuelle selon `references/visuels.md`.
5. Un message qui a besoin de deux slides se scinde en deux titres liés par des points de suspension.
6. Si un cadre à plusieurs composantes structure l'analyse, déclare les boutons de cadre une fois. Marque chaque slide de détail de sa composante.

Test avant validation : lis la colonne des titres seule, dans l'ordre. Elle raconte l'histoire complète. Si un titre ne s'enchaîne pas, corrige le storyline, pas la slide.

Validation : l'utilisateur valide le squelette.

Pourquoi : le squelette coûte des minutes et montre les ruptures du récit. Une slide construite coûte une heure. La validation du squelette évite de reconstruire le deck.

### État 3 — Produire le deck

1. Copie `assets/deck.html` dans le dossier de travail sous le nom `deck.html`. Remplis la configuration : langue, pied de deck, boutons de cadre.
2. Écris une section par ligne du squelette, dans l'ordre, selon `references/gabarit.md`. Le titre d'action de la section est le titre du squelette, caractère pour caractère.
3. Produis chaque preuve visuelle par le moyen adapté au cas (`references/visuels.md`, section « Produire le visuel »). Insère la preuve dans l'emplacement `figure`. Une preuve visuelle est un SVG écrit pour le cas, une image, ou un tableau. Un décor n'est pas une preuve.
4. Lance le contrôle. Corrige jusqu'à zéro erreur. Écris une justification d'une ligne pour chaque avertissement conservé.

   ```bash
   python3 scripts/check_deck.py deck.html storyline.md
   ```

5. Si un navigateur est disponible, ouvre le deck et appuie sur `L`. Le gabarit signale les titres de plus de deux lignes, les corps qui débordent et les emplacements de visuel vides. Corrige le contenu. Ne modifie pas le gabarit.
6. Relis chaque slide avec les neuf règles. Le contrôle vérifie la structure. La relecture vérifie le sens.
7. Livre quatre choses :
   - le chemin du deck ;
   - le chemin du storyline ;
   - le mode d'emploi en trois lignes : navigation, contrôle, impression PDF ;
   - les avertissements conservés, avec leur justification.

Pourquoi le gabarit ne se modifie pas : ses zones fixes font que seul le contenu change au défilement. Un élément qui bouge d'une slide à l'autre attire l'œil vers le cadre et le détourne du message. Si tu modifies seulement le contenu, tu ne peux pas casser cette stabilité.

### État 4 — Réviser

- Un changement de message (un titre, un argument, une preuve qui change la conclusion) passe par le storyline, puis le squelette, puis le deck.
- Un changement de forme (mise en page, formulation, visuel) touche le deck seul.
- Dans les deux cas, relance le contrôle avec le storyline. Le squelette et le deck concordent.

Pourquoi : le deck est une projection du storyline. Si tu modifies le deck seul, les deux objets divergent, et la révision suivante part d'un contrat faux.

## Les neuf règles de la slide

Chaque règle donne le geste, la raison, le signe de réussite et la condition de rupture. La raison te permet d'adapter le geste quand le cas sort du standard. Sans la raison, tu appliques la règle là où elle ne vaut plus.

### 1. La réponse d'abord

Geste : le message principal ouvre le deck. Chaque section ouvre sur sa conclusion. Les preuves viennent ensuite. N'utilise pas l'ordre de l'analyse (méthode, données, conclusion).

Pourquoi : la personne clé cherche la réponse pour savoir quelles questions poser. Si la réponse vient à la dernière slide, elle écoute les preuves sans savoir ce qu'elles prouvent. Elle remplit ce vide avec ses propres hypothèses. La réponse d'abord aligne le deck sur sa façon de penser.

Signe : l'ouverture suffit à obtenir l'effet attendu. Le reste du deck sert à vérifier.

Rupture : une audience qui rejette la conclusion d'emblée refuse les arguments. Garde la réponse en tête de deck, mais fais précéder la Résolution d'une Situation et d'une Complication que l'audience partage. Pour une formation, la réponse d'abord vaut pour le deck entier, pas pour chaque section.

### 2. Une slide, un message

Geste : une slide démontre une seule idée. Le titre énonce l'idée. Le corps la prouve. Rien d'autre.

Pourquoi : le lecteur cherche un ordre dans ce qu'il voit. Deux messages sur une slide l'obligent à choisir lequel compte, et il choisit parfois le mauvais. Un message par slide supprime ce choix.

Signe : chaque élément du corps sert le titre. Si tu retires un élément, le titre perd une preuve.

Rupture : un corps avec deux preuves d'un même message respecte la règle. Deux messages distincts enfreignent la règle : scinde la slide.

### 3. Le titre promet, le corps prouve

Geste : vérifie l'alignement dans les deux sens. Le titre n'affirme rien que le corps ne montre pas. Le corps ne montre rien que le titre n'utilise pas. Une donnée en plus est une donnée à retirer ou à déplacer en annexe.

Pourquoi : une affirmation sans preuve est le point que la réunion conteste, et la crédibilité du deck entier baisse avec elle. Une donnée superflue dilue la preuve et provoque une question qui écarte du message.

Signe : tu relies chaque élément spécifique du titre à un élément visible du corps.

Rupture : aucune.

### 4. Le titre d'action

Geste : écris une phrase complète qui dit l'implication (« et donc ? »), pas le sujet. Écris « La hausse des coûts logistiques a réduit le bénéfice net de 15 M€ en 2024 », pas « Résultats financiers 2024 ». Trois règles de rédaction :

1. Un seul enseignement, le plus important.
2. Spécifique : le titre porte un élément vérifiable. Un chiffre quand il existe. Sinon un nom, une date, un exemple, une citation. N'invente jamais un chiffre pour rendre un titre spécifique.
3. Concis : deux lignes au plus, aucun mot sans information.

Pourquoi : la personne pressée lit seulement les titres. Une suite de titres descriptifs ne dit rien. Une suite de titres d'action raconte l'histoire en trente secondes. Le lecteur attentif descend dans le corps, et le titre lui dit quoi chercher. Les deux lectures coexistent sur le même deck.

Signe : la lecture des titres seuls, dans l'ordre, raconte l'histoire complète.

Rupture : au-delà de deux lignes, le titre devient un paragraphe et perd son impact. Un titre trop long cache deux messages : scinde la slide, ou supprime l'implication secondaire. Une slide-affirmation (`statement`) peut poser une question dans une formation : la slide suivante y répond.

### 5. La preuve choisie par l'enseignement

Geste : nomme d'abord la nature de ce que le lecteur doit voir : comparaison, composition, variation, écart, relation, distribution, séquence, exemple, témoignage. Puis prends la preuve que `references/visuels.md` associe à cette nature. N'utilise jamais un camembert.

Pourquoi : l'œil compare des longueurs et des hauteurs avec précision. Il compare mal des angles et des surfaces. Une preuve choisie par la nature de l'enseignement se lit sans effort. Une preuve choisie par goût demande un décodage qui coûte de l'attention au message.

Signe : le lecteur énonce l'enseignement en regardant la preuve, avant de lire le titre.

Rupture : un tableau de six valeurs vaut mieux qu'un graphique de six valeurs. Si le visuel n'ajoute pas de lecture, il est un décor : remplace-le par un tableau, un chiffre clé ou une phrase.

### 6. La prévision distinguée

Geste : distingue chaque valeur projetée d'une valeur constatée. Trois moyens existent : une couleur et un fond, un trait pointillé, un suffixe sur l'étiquette (`2027F`). Le choix dépend de l'audience. Il est traité dans `references/visuels.md`.

Pourquoi : un lecteur qui prend une projection pour un fait décide sur une base fausse. Une audience qui le découvre retire sa confiance au deck entier.

Signe : la frontière entre constaté et projeté se voit sans légende.

Rupture : un deck dont toutes les valeurs sont projetées ne marque rien. Il le dit une fois, dans l'ouverture.

### 7. Le décor minimal

Geste : sur une preuve visuelle, une flèche d'écart au plus et deux commentaires au plus. Pas de logo, pas d'icône, pas de relief, pas d'ombre. Une image porte le message ou n'est pas sur la slide.

Pourquoi : chaque élément ajouté entre en concurrence avec le message pour l'attention. Une flèche qui montre l'écart guide le lecteur. Trois flèches le dispersent.

Signe : aucun élément du visuel ne peut être retiré sans perte d'information.

Rupture : aucune.

### 8. La continuité entre slides

Geste : trois dispositifs, à utiliser seulement quand la lecture le demande.

- **Ellipses** : un message qui a besoin de deux slides se scinde en deux titres. Lus à la suite, ils font une seule phrase : « La division A nous classe premiers en France… » puis « …mais douzièmes en Europe ». Chaque corps prouve son segment.
- **Boutons de cadre** : quand l'analyse suit un cadre à composantes, la slide qui présente le cadre les nomme. Chaque slide de détail porte le bouton de sa composante. Un seul jeu de boutons par deck, déclaré dans la configuration.
- **Indicateur de section** : chaque slide porte le nom de sa section, au même endroit, dans la même typographie, plus discret que le titre.

Pourquoi : au-delà de vingt slides, le lecteur perd la carte du deck et se demande où il est. Les connecteurs lui épargnent ce repérage et gardent son attention sur le message.

Signe : à chaque slide, le lecteur sait dans quelle partie il est et ce qui précède.

Rupture : des ellipses entre deux slides dont les corps ne dépendent pas l'un de l'autre. Des boutons dont la couleur change en cours de deck. Trop de connecteurs sur une slide : garde un indicateur, et un bouton si le cadre existe.

### 9. Toute preuve a une origine

Geste : chaque slide qui montre une preuve porte sa source dans le pied : la donnée, l'image, la citation, l'exemple. Une estimation est marquée comme estimation, avec son hypothèse principale.

Pourquoi : la première question d'une audience devant une preuve est « d'où vient-elle ? ». Une source visible répond avant la question. Une estimation présentée comme un fait est une faute que l'audience finit par découvrir.

Signe : aucune preuve du deck n'est sans origine.

Rupture : aucune.

## Ce qui est imposé, ce qui est contrôlé, ce qui est à ta charge

**Le gabarit impose** :

- le format 16:9 et les marges ;
- la zone d'en-tête et sa hauteur ;
- le titre limité à deux lignes ;
- la zone de corps sans débordement ;
- le pied avec la source et le numéro ;
- les treize mises en page ;
- l'indicateur de section et les boutons de cadre, générés au même endroit ;
- la palette.

**Le contrôle vérifie** :

- un titre par slide ;
- une mise en page connue ;
- l'indicateur de section présent ;
- la source présente sur chaque slide avec preuve ;
- les trois blocs du résumé exécutif ;
- le nombre de panneaux ;
- la figure non vide ;
- le nombre d'étapes d'une chronologie ;
- les paires d'ellipses ;
- les boutons déclarés ;
- l'absence de texte de remplissage ;
- la concordance des titres avec le squelette.

Il avertit sur quatre points :

- un titre long ;
- un titre interrogatif, hors slide-affirmation ;
- une ouverture sans résumé exécutif ;
- un SVG avec des couleurs hors palette.

**À ta charge, par relecture** :

- la réponse d'abord ;
- un message par slide ;
- l'alignement entre titre et corps ;
- la qualité du titre ;
- le choix de la preuve ;
- l'absence de camembert ;
- le marquage des prévisions ;
- le décor minimal ;
- l'absence de chiffre inventé.

Ce que le code n'impose pas se tient par discipline.

## Ton et langue

- Le deck est dans la langue de l'utilisateur. Les nombres et les dates suivent le format de cette langue.
- Les titres sont des phrases pour l'audience : concrètes, spécifiques, sans jargon de méthode. Le vocabulaire de méthode (Situation-Complication-Résolution, Dot-Dash, pyramide) sert à ton travail, jamais aux slides.
- Dans l'échange avec l'utilisateur : une question fermée à la fois, et la réponse avant l'explication.
