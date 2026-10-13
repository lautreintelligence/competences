---
type: "Specification"
description: "Format du fichier storyline.md du skill deck-builder : cadrage, récit Situation-Complication-Résolution, plan Dot-Dash et squelette, avec la raison de chaque élément, les tests de validation, un exemple complet de deck de décision sur un investissement Customer Success et un exemple court de deck de formation."
status: "stable"
tags: ["presentation", "communication", "redaction", "strategie"]
created: 2026-10-13
---

# Format du storyline

Le storyline est le contrat du deck. Il s'écrit avant toute slide. L'utilisateur le valide deux fois : après le récit et le plan Dot-Dash, puis après le squelette. Le deck est une projection de ce fichier. Tout ce que le deck dit se trouve dans le storyline, dans le même ordre, avec les mêmes titres.

## Emplacement et structure

Le fichier se nomme `storyline.md`. Il est dans le dossier de travail du deck, à côté de `deck.html`. Il contient quatre sections, dans cet ordre.

```markdown
# <Titre du deck>

## Cadrage
## Récit
## Dot-Dash
## Squelette
```

Le squelette est la seule table du fichier dont un en-tête contient le mot « Titre ». Le script `check_deck.py` lit cette table et compare ses titres aux titres du deck. Le fichier peut commencer par un frontmatter YAML. Le script l'ignore.

## Cadrage

### Contenu

Sept lignes, une par question.

```markdown
## Cadrage

- Effet attendu : <ce que le deck doit obtenir, en une phrase>
- Audience et personne clé : <qui lit le deck, et qui obtient ou donne l'effet>
- Genre : <décision, information, pilotage, pitch, commercial, retour d'expérience, formation>
- Question de l'audience : <la question dans ses mots>
- Matière disponible : <faits, chiffres, exemples, analyses, sources, avec leur emplacement>
- Manques : <ce qui n'existe pas, et ce que le deck fait de ce manque : estimation marquée, ou question à l'utilisateur>
- Contraintes : <langue, durée, nombre de slides, date, audience acquise ou hostile>
```

### Pourquoi

Le deck s'écrit pour une audience qui doit faire une chose précise. L'ouverture s'adresse à la personne clé. Les titres répondent à sa question. Le niveau de détail suit ce qu'elle sait déjà. Le genre fixe l'ouverture et la preuve typique (table des genres dans `SKILL.md`). Un cadrage absent produit un deck pour tout le monde, donc pour personne.

### Test

Une tierce personne lit le cadrage. Elle sait, sans autre explication, ce que le deck doit obtenir et de qui.

## Récit

### Contenu

Quatre paragraphes courts. Une page au plus. Le récit se lit d'une traite.

```markdown
## Récit

**Situation.** <Le contexte que l'audience admet : périmètre, faits de base, pourquoi le sujet compte.>

**Complication.** <Ce qui a changé, sa gravité, et le déclencheur qui rend l'action nécessaire maintenant.>

**Question.** <La question que la complication fait naître : « Que faut-il faire pour… ? »>

**Résolution.** <La réponse, ce qu'elle coûte, ce qu'elle apporte, quand, et ce que le deck demande à l'audience.>
```

### Comment écrire chaque partie

- La Situation contient seulement des faits que l'audience accepte sans discussion. Une Situation contestable fait perdre le lecteur avant la Complication.
- La Complication est la tension du récit. Elle est spécifique. « Les marges baissent » ne crée aucune tension. « La marge opérationnelle a perdu 12 M€ en trois ans et passe sous zéro en 2027 » crée une tension. Sans chiffre, un fait daté ou un exemple précis joue le même rôle.
- La Question est implicite dans le deck. Elle s'écrit ici pour vérifier que la Résolution répond à elle, et à elle seule.
- La Résolution donne la réponse d'abord, puis ses conditions. Elle contient l'élément que l'audience retient.

Pour une formation, la Situation est ce que l'apprenant sait faire. La Complication est le cas que ce savoir ne couvre pas. La Résolution est la capacité que le deck apporte.

### Pourquoi

La séquence est le mécanisme d'un récit. Une base stable rassure. Une rupture inquiète. La réponse résout l'inquiétude. Le lecteur veut la suite parce que la complication le concerne. Un deck qui commence par la méthode et finit par la conclusion ne crée aucune tension : le lecteur décroche avant la fin.

### Test

Le récit se lit sans rupture logique et sans retour en arrière. Chaque phrase de la Résolution répond à la Question. Un lecteur qui ne connaît pas le sujet comprend le problème et la réponse.

## Dot-Dash

### Contenu

Une liste à deux niveaux. Un Dot est une affirmation clé : une phrase complète et spécifique, qui devient un titre d'action. Un Dash est une preuve de ce Dot : la preuve, sa source, et le visuel que la preuve devient.

```markdown
## Dot-Dash

- **Dot 1.** <Affirmation complète, futur titre d'action.>
  - Dash 1.1 — <Preuve.> Source : <origine>. Visuel : <type et contenu>.
  - Dash 1.2 — <Preuve.> Source : <origine>. Visuel : <type et contenu>.
- **Dot 2.** <Affirmation complète.>
  - Dash 2.1 — …
```

### Règles

1. Un Dot est une phrase avec un verbe et un élément spécifique : un chiffre, un nom, une date, un exemple. « Les coûts logistiques » n'est pas un Dot. « La hausse des coûts logistiques a effacé 12 M€ de résultat entre 2021 et 2024 » est un Dot. « Le circuit court supprime l'intermédiaire qui retient 30 % du prix » est un Dot.
2. Un Dot tient en deux lignes. Au-delà, il porte deux messages : scinde-le.
3. Chaque Dash nomme sa source. Une estimation s'écrit « estimation : <hypothèse> ». N'invente aucun chiffre.
4. Chaque Dash nomme le visuel qu'il devient, choisi selon `visuels.md`. Une preuve de six valeurs ou moins devient un tableau ou un chiffre clé. Une preuve sans chiffre devient un exemple, une citation, une image, une chronologie ou un schéma.
5. Un Dot sans Dash est supprimé, ou devient une question posée à l'utilisateur avant la suite.
6. Les Dots suivent l'ordre de la pyramide : la réponse, puis les raisons dans l'ordre de leur force, puis les preuves d'appui. Pour une formation, les Dots suivent la progression des concepts.

### Pourquoi

Le Dot-Dash exige la preuve au moment où l'affirmation s'écrit, quand sa suppression ne coûte rien. Sans lui, l'affirmation sans preuve apparaît une fois la slide construite, et la slide est jetée. Il fixe aussi la double lecture du deck : les Dots sont la lecture horizontale (titres seuls), les Dashes la lecture verticale (corps des slides).

### Test

La lecture des Dots seuls, dans l'ordre, raconte le récit. Chaque Dash prouve le Dot au-dessus de lui et rien d'autre. Aucun élément spécifique d'un Dot n'est absent de ses Dashes.

## Squelette

### Contenu

Une table, une ligne par slide, dans l'ordre du deck. La couverture et les intercalaires ont leur ligne.

```markdown
## Squelette

| # | Section | Titre d'action | Mise en page | Preuve | Source |
|---|---|---|---|---|---|
| 1 | — | <titre de couverture> | cover | — | — |
| 2 | Résumé exécutif | <titre du résumé exécutif> | exec-summary | Situation, Complication, Résolution | — |
| 3 | 01 <Section> | <titre d'intercalaire> | divider | — | — |
| 4 | 01 <Section> › <Sous-section> | <Dot 1, caractère pour caractère> | chart-insights | <visuel : Dash 1.1, Dash 1.2> | <source> |
```

Colonnes :

- `#` : le numéro de la slide.
- `Section` : l'indicateur affiché en haut de la slide, de la forme `01 Diagnostic › Coûts`. Vide pour la couverture et les intercalaires.
- `Titre d'action` : le titre, caractère pour caractère. Le deck reprend cette chaîne sans modification. Le script compare les deux.
- `Mise en page` : une des treize mises en page du gabarit (`gabarit.md`).
- `Preuve` : le ou les Dashes que le corps montre, et le type de visuel.
- `Source` : ce que le pied de la slide affiche.

### Règles

1. La première slide de contenu est l'ouverture du genre : un résumé exécutif, ou la slide d'objectif pour une formation. Elle tient seule.
2. Un Dot fait une slide. Plusieurs Dashes pour un même Dot font une slide à panneaux, ou une slide par Dash si chaque preuve a besoin de la place.
3. Au-delà de huit slides, le deck a des sections avec un intercalaire. Chaque slide d'une section porte son indicateur.
4. Un message en deux slides se scinde en deux titres liés par des points de suspension. Le premier titre finit par « … ». Le second commence par « … ». Lus à la suite, ils font une phrase.
5. Si un cadre à composantes structure l'analyse, les boutons de cadre sont déclarés une fois dans la configuration du deck. Chaque slide de détail porte le sien.
6. Les annexes viennent après la dernière slide de contenu, dans une section « Annexes ». Elles portent seulement ce qu'une question probable réclame.

### Pourquoi

Le squelette coûte des minutes et montre les ruptures du récit. Une slide construite coûte une heure. La validation du squelette évite de reconstruire le deck. La colonne des titres est le premier test du deck : lue seule, elle raconte l'histoire.

### Test

Lis la colonne `Titre d'action` seule, dans l'ordre : elle raconte le récit complet. Chaque ligne a une preuve qui suffit à son titre. Aucune ligne ne porte deux titres.

## Exemple 1 : deck de décision

Cas inventé : un éditeur de logiciel B2B, Nordis, demande à son comité d'investissement de financer une équipe Customer Success.

```markdown
# Enrayer l'attrition : investir 2 M€ dans une équipe Customer Success

## Cadrage

- Effet attendu : le comité valide un budget de 2 M€ sur 2027-2028 pour recruter six Customer Success Managers.
- Audience et personne clé : le comité d'investissement, cinq membres ; la directrice générale décide ; le directeur financier est sceptique sur tout recrutement.
- Genre : décision.
- Question de l'audience : « Est-ce que ça se rembourse, et en combien de temps ? »
- Matière disponible : ARR par client et par an 2024-2026 (export CRM), 44 entretiens de résiliation (Direction Clients), chiffrage des options (Direction financière), modèle financier à deux scénarios.
- Manques : aucun benchmark externe de churn ; le churn cible de 9 % est une estimation fondée sur les comptes déjà suivis.
- Contraintes : quinze minutes, douze slides au plus, français, comité le 13 octobre 2026.

## Récit

**Situation.** Nordis réalise 18,8 M€ d'ARR auprès de 320 clients et croît de 12 % par an. Les clients de moins de 50 K€ d'ARR représentent 61 % du portefeuille et n'ont aucun interlocuteur dédié.

**Complication.** L'attrition est passée de 8 % à 14 % en dix-huit mois. Elle efface 1,1 M€ d'ARR par an et reprend près de la moitié des ventes nouvelles. Sans action, l'ARR 2028 plafonne à 17,1 M€, sous le niveau de 2026.

**Question.** Que faut-il faire pour ramener l'attrition sous 10 % avant 2029 sans sacrifier la croissance ?

**Résolution.** Recruter six Customer Success Managers affectés aux comptes de moins de 50 K€, pour 2 M€ sur deux ans. L'attrition revient à 9 % fin 2028. Le dispositif retient 1,5 M€ d'ARR par an et se rembourse en vingt mois. Le comité valide le budget et un démarrage des recrutements au 1er janvier 2027.

## Dot-Dash

- **Dot 1.** Entre 2024 et 2026, l'attrition a repris 2,2 M€ sur les 4,7 M€ gagnés en ventes nouvelles et en expansion.
  - Dash 1.1 — ARR 2024 : 16,3 M€ ; ventes nouvelles +3,9 ; expansion +0,8 ; attrition −2,2 ; ARR 2026 : 18,8 M€. Source : comptabilité analytique. Visuel : cascade de variation.
  - Dash 1.2 — Churn de 8 % en 2024 et 14 % en 2026. Source : CRM. Visuel : commentaire sur la colonne attrition.
- **Dot 2.** Le churn se concentre sur les clients de moins de 50 K€ d'ARR, qui n'ont eu aucun contact depuis six mois dans 68 % des cas.
  - Dash 2.1 — Churn par segment : 21 % sous 50 K€, 9 % de 50 à 200 K€, 4 % au-dessus. Source : CRM, 44 clients perdus. Visuel : barres horizontales triées.
  - Dash 2.2 — 68 % des clients perdus sans contact depuis six mois. Source : CRM. Visuel : chiffre clé.
  - Dash 2.3 — Motifs de résiliation : adoption faible 23, prix 11, concurrent 7, autre 3. Source : entretiens de résiliation. Visuel : liste.
- **Dot 3.** Le churn décroît avec la fréquence de contact : au-delà de quatre échanges par an, il tombe sous 6 %.
  - Dash 3.1 — Churn par classe de fréquence de contact, huit classes. Source : CRM, 320 clients. Visuel : nuage de points.
- **Dot 4.** Des trois options chiffrées, seule l'équipe dédiée agit sur les deux causes du churn et se rembourse en moins de deux ans.
  - Dash 4.1 — Coût, churn cible, ARR retenu et délai de retour des trois options. Source : Direction financière. Visuel : tableau structuré.
- **Dot 5.** Sans action, l'attrition ramène l'ARR à 17,1 M€ en 2028 ; six CSM le portent à 22,4 M€.
  - Dash 5.1 — Trajectoires 2024-2028 des deux scénarios. Source : modèle financier. Visuel : courbes, prévision marquée à partir de 2027.
  - Dash 5.2 — Décomposition de l'écart : rétention +2,1, expansion +1,4, écart restant 1,8 par les ventes. Source : modèle financier. Visuel : cascade d'écart.
- **Dot 6.** Décision demandée : valider 2 M€ sur 2027-2028 et un démarrage des recrutements au 1er janvier 2027.
  - Dash 6.1 — Ce que le comité valide, jalons de contrôle, risques et parades. Source : Direction Clients. Visuel : trois panneaux.

## Squelette

| # | Section | Titre d'action | Mise en page | Preuve | Source |
|---|---|---|---|---|---|
| 1 | — | Enrayer l'attrition : investir 2 M€ dans une équipe Customer Success | cover | — | — |
| 2 | Résumé exécutif | Investir 2 M€ sur deux ans dans six Customer Success Managers retient 1,5 M€ d'ARR par an et se rembourse en 20 mois | exec-summary | Situation, Complication, Résolution | — |
| 3 | 01 Diagnostic | Diagnostic : d'où vient l'attrition | divider | — | — |
| 4 | 01 Diagnostic › ARR | Entre 2024 et 2026, l'attrition a repris 2,2 M€ sur les 4,7 M€ gagnés en ventes nouvelles et en expansion | chart-insights | Cascade de variation (Dash 1.1), commentaire churn (Dash 1.2) | Comptabilité analytique Nordis |
| 5 | 01 Diagnostic › Segments | Le churn se concentre sur les clients de moins de 50 K€ d'ARR, qui n'ont eu aucun contact depuis six mois dans 68 % des cas | panels-3 | Barres par segment, chiffre clé, liste des motifs (Dashes 2.1 à 2.3) | CRM Nordis, 44 clients perdus |
| 6 | 01 Diagnostic › Contacts | Le churn décroît avec la fréquence de contact : au-delà de quatre échanges par an, il tombe sous 6 % | chart-insights | Nuage de points (Dash 3.1) | CRM Nordis, 320 clients |
| 7 | 02 Recommandation | Recommandation : six Customer Success Managers | divider | — | — |
| 8 | 02 Recommandation › Options | Des trois options chiffrées, seule l'équipe dédiée agit sur les deux causes du churn et se rembourse en moins de deux ans | table | Tableau des options (Dash 4.1) | Direction financière, septembre 2026 |
| 9 | 02 Recommandation › Trajectoire | Sans action, l'attrition ramène l'ARR à 17,1 M€ en 2028… | chart-insights | Courbes deux scénarios, prévision dès 2027 (Dash 5.1) | Modèle financier Nordis |
| 10 | 02 Recommandation › Trajectoire | …tandis que six CSM portent l'ARR 2028 à 22,4 M€, dont 1,8 M€ restent à gagner par les ventes | chart-insights | Cascade d'écart (Dash 5.2) | Modèle financier Nordis |
| 11 | 02 Recommandation › Décision | Décision demandée : valider 2 M€ sur 2027-2028 et un démarrage des recrutements au 1er janvier 2027 | panels-3 | Validation, jalons, risques (Dash 6.1) | Direction Clients Nordis |
```

Lecture des titres seuls, lignes 2 à 11 : la réponse, le diagnostic en trois preuves, les options, la trajectoire en deux temps, la demande. Le récit tient sans le corps des slides.

## Exemple 2 : deck de formation, sans chiffres

Cas inventé : une formation d'une heure pour des chefs de projet sur la rédaction d'un compte rendu de réunion.

```markdown
# Rédiger un compte rendu que l'absent peut utiliser

## Cadrage

- Effet attendu : à la fin de la session, chaque participant rédige un compte rendu de réunion en dix minutes, lisible par une personne absente.
- Audience et personne clé : douze chefs de projet juniors ; la responsable du bureau des projets valide le format.
- Genre : formation.
- Question de l'audience : « Qu'est-ce que je mets dedans, et qu'est-ce que je laisse ? »
- Matière disponible : six comptes rendus réels anonymisés, dont trois jugés inutilisables par leurs destinataires ; le modèle de compte rendu du bureau des projets.
- Manques : aucune mesure du temps de rédaction actuel ; le deck n'en donne pas.
- Contraintes : une heure, vingt slides au plus, un exercice au milieu, français.

## Récit

**Situation.** Chaque réunion de projet produit un compte rendu. Le destinataire principal est la personne qui n'était pas là.

**Complication.** Trois des six comptes rendus étudiés racontent la réunion dans l'ordre où elle a eu lieu. Le lecteur absent ne trouve ni les décisions ni ce qu'on attend de lui. Il demande une réunion de rattrapage.

**Question.** Comment écrire un compte rendu que l'absent utilise sans poser de question ?

**Résolution.** Un compte rendu commence par les décisions, continue par les actions avec un responsable et une date, et finit par les points ouverts. Il omet le déroulé de la réunion. Les participants appliquent ce format sur un cas pendant la session.

## Dot-Dash

- **Dot 1.** Un compte rendu rédigé dans l'ordre de la réunion oblige l'absent à demander une seconde réunion.
  - Dash 1.1 — Compte rendu n° 3 : deux pages de déroulé, la décision principale en avant-dernier paragraphe. Source : corpus anonymisé. Visuel : image de la page avec la décision entourée.
  - Dash 1.2 — Citation du destinataire : « J'ai lu deux pages et j'ai appelé pour savoir ce qui avait été décidé. » Source : entretien. Visuel : slide-affirmation avec citation.
- **Dot 2.** L'absent cherche trois choses, dans cet ordre : ce qui est décidé, ce qu'il doit faire, ce qui reste ouvert.
  - Dash 2.1 — Les trois blocs du format, avec un exemple de chaque. Source : modèle du bureau des projets. Visuel : trois panneaux.
- **Dot 3.** Une action sans responsable ni date n'est pas une action.
  - Dash 3.1 — Compte rendu n° 5 : « revoir le planning » sans nom ni date, resté sans suite trois semaines. Source : corpus anonymisé. Visuel : avant-après en deux panneaux.
- **Dot 4.** Exercice : réécrivez le compte rendu n° 3 en dix minutes avec le format en trois blocs.
  - Dash 4.1 — Le compte rendu n° 3 et le format vide. Source : corpus anonymisé. Visuel : image de la page et panneau du format.
```

Le squelette suit le même format que l'exemple 1. La première slide de contenu est une slide-affirmation : « À la fin de cette heure, vous rédigez en dix minutes un compte rendu que l'absent utilise sans vous appeler. » Le script avertit qu'elle n'est pas un résumé exécutif. La justification à la livraison est « genre : formation ».
