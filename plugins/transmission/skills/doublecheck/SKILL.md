---
name: doublecheck
description: >
  DoubleCheck — Protocole d'auto-correction dialectique inspiré du
  "dialectical bootstrapping" (Herzog & Hertwig, 2009) et du "consider
  the opposite" (Lord et al., 1984). Applique ce skill chaque fois que
  l'utilisateur demande de vérifier, reconsidérer, challenger, ou
  améliorer une réponse, une analyse, une estimation, ou un raisonnement.
  Utilise-le aussi quand l'utilisateur dit « t'es sûr ? », « vérifie »,
  « doublecheck », « reconsidère », « challenge ça », « joue l'avocat du
  diable », « qu'est-ce que tu pourrais avoir raté ? », « pousse plus
  loin », « est-ce qu'on a pas oublié quelque chose ? », ou toute
  formulation qui exprime un doute sur la complétude ou la justesse d'une
  réponse — y compris la tienne. Utilise-le aussi de ta propre initiative
  quand tu sens que ta première réponse repose sur des hypothèses fragiles,
  qu'un sujet est controversé, qu'une estimation pourrait être biaisée,
  ou qu'un raisonnement mériterait un second regard.
license: Apache-2.0
metadata:
  version: "0.1.0"
  author: "L'Autre Intelligence & Nous"
  tags: ["biais-cognitif", "verification", "raisonnement"]
---

# DoubleCheck — Protocole d'auto-correction dialectique

## Pourquoi ce protocole existe

Le cerveau humain — et les LLMs — ont une tendance naturelle à l'ancrage :
une fois qu'une première réponse est formulée, tout ce qui suit gravite
autour d'elle. Le biais de confirmation fait le reste : on cherche
inconsciemment les éléments qui confirment plutôt que ceux qui infirment.

La recherche en psychologie cognitive montre qu'on peut réduire
significativement ces biais avec une technique simple : se forcer à
produire une seconde estimation construite depuis des hypothèses
différentes, puis combiner les deux. C'est le principe du "dialectical
bootstrapping" — reproduire la sagesse des foules à l'intérieur d'un
seul esprit.

Ton rôle quand ce skill s'active : devenir ton propre contradicteur,
puis synthétiser.

## Le protocole en 4 mouvements

La réponse suit quatre mouvements qui se fondent dans un texte fluide.
Pas de titres "Étape 1" etc. — la progression doit être naturelle.

### 1. Poser la première position

Commence par rappeler clairement la réponse, l'analyse ou l'estimation
initiale. Si elle vient de toi dans un message précédent, résume-la
honnêtement — sans la déformer ni l'embellir. Si elle vient de
l'utilisateur, reformule-la fidèlement pour montrer que tu l'as comprise.

Ce qui compte : la première position doit être explicite et assumée.
C'est ta "thèse". On ne peut pas la remettre en question si elle reste
floue.

### 2. La présomption de faille

Pars du principe que cette première position est significativement
imparfaite. Pas marginalement — significativement. C'est contre-intuitif,
mais cette présomption est le moteur du protocole : elle force le cerveau
à quitter l'orbite de la première réponse.

Pose-toi ces questions (dans ton raisonnement interne, pas forcément
toutes à voix haute) :

- **Hypothèses implicites** : Quelles prémisses ai-je acceptées sans
  les examiner ? Quel cadrage ai-je adopté par défaut ?
- **Angles morts** : Qu'est-ce qui manque dans mon analyse ? Quels
  facteurs, acteurs, contraintes ou données n'ai-je pas considérés ?
- **Direction du biais** : Ma première réponse était-elle probablement
  trop optimiste ou trop pessimiste ? Trop simple ou trop compliquée ?
  Trop conventionnelle ou trop originale ?
- **La perspective de l'opposant** : Quelqu'un d'intelligent et bien
  informé qui serait en désaccord avec moi — que dirait-il ? Pourquoi
  aurait-il raison ?

Ce dernier point est important. La recherche (Van de Calseyde & Efendić,
2022) montre que se mettre dans la peau d'un contradicteur produit de
meilleures corrections que simplement "repenser" de façon abstraite.

### 3. La reconstruction

À partir des failles identifiées, construis une position alternative.
Pas un simple ajustement cosmétique — une reconstruction qui intègre
les éléments que la première position ignorait.

Ce qui compte ici :

- La nouvelle position doit être *substantiellement* différente, pas
  juste la première avec une nuance ajoutée
- Elle doit s'appuyer sur les éléments concrets identifiés à l'étape
  précédente, pas sur un vague "d'un autre côté..."
- Si tu trouves des informations factuelles pertinentes que la première
  réponse ne prenait pas en compte, intègre-les ici avec leur source

### 4. La synthèse

Combine les deux positions en une réponse finale plus robuste. Ce n'est
pas un simple "la vérité est au milieu" — c'est une intégration
dialectique :

- Identifie ce qui tient dans chaque position
- Explique pourquoi certains éléments de la première position étaient
  fragiles et comment la reconstruction les corrige
- Propose la réponse révisée avec un degré de confiance honnête :
  qu'est-ce qui reste incertain malgré cette seconde passe ?

## Calibrage contextuel

L'intensité du protocole s'adapte à l'enjeu :

**Questions factuelles vérifiables** : Le doublecheck est rapide — il
s'agit surtout de vérifier si la première réponse est factuelle ou si
elle extrapole. Chercher des sources contradictoires, corriger si
nécessaire.

**Analyses et raisonnements** : Le doublecheck est plus profond — il
faut remonter aux hypothèses, examiner les cadres alternatifs, peser
les arguments.

**Estimations et prédictions** : Le doublecheck est maximal — c'est
là que le biais d'ancrage frappe le plus fort. Forcer une seconde
estimation depuis des hypothèses différentes, puis combiner les deux.

**Opinions et jugements de valeur** : Le doublecheck explore les
perspectives alternatives avec honnêteté, sans prétendre qu'il existe
une "bonne réponse" unique.

## Ce que DoubleCheck ne fait PAS

- Simuler un faux débat pour le spectacle — chaque objection doit
  être sincère et substantielle
- Conclure systématiquement que "les deux ont raison" — parfois la
  première position tient, parfois la reconstruction la remplace
- Ajouter des caveats mous ("il faut nuancer", "c'est complexe") sans
  apporter de contenu réel
- S'appliquer aux questions triviales ou purement mécaniques où il
  n'y a rien à reconsidérer

## Style

Le ton est celui d'un penseur rigoureux qui a l'honnêteté de se
corriger publiquement. Pas d'excuses ("désolé, j'aurais dû..."),
pas de dramatisation ("en réalité, tout est faux !") — juste un
raisonnement qui gagne en qualité par la friction interne.

Le texte est fluide, en prose. Les listes à puces ne sont utilisées
que si elles clarifient réellement la comparaison entre les deux
positions.
