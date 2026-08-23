# Guide de conception des cas

## Le twist : bibliothèque de mécaniques

Un twist est un insight que les données révèlent mais que l'intuition ne prédit pas. Pioche une mécanique et incarne-la dans un secteur — jamais deux fois la même mécanique dans la banque.

1. **Le mix masqué** — l'agrégat est stable mais sa composition s'est dégradée (ex. fréquentation stable, mix payant/abonné toxique). Sollicite : réflexe de désagrégation.
2. **Le segment contre-intuitif** — le segment en croissance est le moins rentable, ou le client le plus fidèle est destructeur de valeur. Sollicite : économie unitaire par segment.
3. **Le canal piégé** — la voie d'accès évidente est verrouillée ou économiquement morte ; la vraie question devient le « comment ». Sollicite : exploration d'alternatives.
4. **Le coût contractuel caché** — une clause (reversement forfaitaire, minimum garanti, indexation) rend un volume croissant destructeur de marge. Sollicite : lecture fine de la structure de coûts.
5. **Le dénominateur qui bouge** — un ratio s'améliore uniquement parce que son dénominateur fond (ex. marge en hausse car les ventes s'effondrent). Sollicite : méfiance envers les ratios.
6. **La capacité fantôme** — le problème apparent est commercial, la cause réelle est opérationnelle (goulot, taux d'utilisation, saisonnalité). Sollicite : penser au-delà du P&L.
7. **La cannibalisation du nouveau produit** — le lancement réussit en volume mais détruit la marge du produit historique. Sollicite : incrémentalité.
8. **Le faux problème de prix** — le client veut baisser les prix, les données montrent que l'élasticité ou le positionnement disent l'inverse. Sollicite : courage de contredire le client.
9. **Les synergies asymétriques (M&A)** — la cible ne vaut le prix que sous des hypothèses de synergies qu'un seul acquéreur peut réaliser — ou que personne ne peut. Sollicite : valorisation critique.
10. **Le coût d'acquisition qui ment** — le CAC moyen est sain, le CAC marginal du dernier canal est ruineux. Sollicite : raisonnement à la marge.
11. **Le levier opérationnel** — coûts fixes élevés : une baisse modérée du volume écrase le profit de façon disproportionnée (et chaque unité regagnée rapporte gros). Sollicite : distinction fixe/variable, point mort.
12. **Le benchmark révélateur** — le symptôme du client est en réalité un problème de marché entier (tous les concurrents souffrent) ou au contraire purement idiosyncratique. La comparaison externe change tout le diagnostic. Sollicite : réflexe interne/externe.
13. **Le seau percé** — la croissance de l'acquisition masque un churn massif ; seule une lecture par cohortes révèle que LTV < CAC. Sollicite : analyse par cohortes, stock vs flux.
14. **La concentration 80/20** — une poignée de clients, produits ou magasins génère tout le profit ; la longue traîne le détruit et la moyenne cache tout. Sollicite : désagrégation par unité, courage de tailler.
15. **Le profit sans cash** — rentable au P&L mais étranglé par le BFR (stocks, délais de paiement) ou le capex ; le vrai problème est la trésorerie. Sollicite : distinction profit/cash.
16. **Le choc externe** — régulation, disruption ou entrant agressif rend le modèle intenable à horizon visible ; le cas teste la réaction stratégique, pas le diagnostic. Sollicite : options sous contrainte de temps.

## Exigences par type de cas

| Type | Doit contenir | Dimension principalement testée |
|---|---|---|
| Profitabilité | Décomposition revenus/coûts + économie unitaire | Business sense |
| Entrée de marché | Sizing du marché + comparaison d'au moins 2 options d'entrée chiffrées | Structuration |
| M&A | Valorisation simple (multiple ou payback) + synergies chiffrées + un deal-breaker non financier | Business sense + quant |
| Pricing | Élasticité ou willingness-to-pay + impact P&L de 2 scénarios de prix | Quant |
| Market sizing | Approche demande + un sanity check par l'offre ou le revenu | Quant + communication |
| Croissance | Arbre de croissance (organique/inorganique, produit/géo) + priorisation chiffrée | Structuration |
| Opérations | Un goulot ou un ratio d'utilisation + calcul de capacité | Quant |

## Règles de chiffres propres (rappel opérationnel)

- Construis à rebours : résultat final rond → données d'entrée dérivées.
- Pourcentages autorisés : 10, 20, 25, 30, 40, 50, 60, 75, 80 %. Croissances : 5, 10, 15, 20 %.
- Grandeurs : multiples de 5 ou puissances de 10 (600 000 unités, 1,2 Md€, 20 M d'entrées).
- Chaque étape de calcul : faisable de tête en < 20 secondes.
- Les fourchettes acceptables des market sizings couvrent ×2 autour de la référence (ex. 1-3 M pour une référence à 1,5 M).

## Calibrage de la difficulté — échelle à 3 niveaux

La difficulté porte sur DEUX axes à la fois : le nombre de mécaniques (l'insight) et les exigences d'exécution (données, calculs, pression). Recettes par défaut :

- **Facile** : sans twist — cas d'exécution pure. 3 données demandables, 1 exhibit lisible, calculs à 2 étapes, structure canonique suffisante. On note la propreté du geste : cadrage, calcul, so what, synthèse. Un cas facile n'est PAS un cas bâclé : c'est le geste standard, joué sans piège.
- **Moyen** : 1 mécanique de twist. 4-5 données demandables, 1-2 exhibits, calculs à 2-3 étapes, twist atteignable en une désagrégation bien choisie.
- **Difficile** : 2 mécaniques emboîtées (la première désagrégation révèle un symptôme, la seconde la cause — ex. mix masqué + levier opérationnel). 5-6 données dont une fausse piste plausible, un exhibit avec piège de lecture (unités mélangées, ligne hors périmètre), calculs à 3 étapes, et une question d'opinion où la bonne réponse contredit le client. En passation : interruptions et temps raccourcis.
- La fausse piste d'un cas difficile doit coûter du temps, jamais rendre le cas insoluble : le chemin correct reste accessible depuis n'importe quel point.

**Règle de bruit anti-métajeu (obligatoire)** : environ 1 cas sur 5, casse la recette du niveau sans le dire — un difficile sans aucun twist mais aux exigences d'exécution maximales (volume de calculs, fausse piste, pression), ou un moyen à deux mécaniques légères et calculs simples. Raison : si nombre de twists = niveau, le candidat qui connaît le niveau déduit la solution avant d'analyser. Le champ « Twist » du fichier de cas documente honnêtement ce qu'il en est (y compris « aucun — cas d'exécution ») ; c'est le label de difficulté annoncé au candidat qui ne doit rien garantir. L'interviewer, lui, n'annonce jamais ni le niveau ni l'existence d'un twist.

## Secteurs — varier systématiquement

Alterne B2C/B2B et parmi : retail, transport, santé, logiciel/SaaS, industrie, énergie, agroalimentaire, loisirs, banque/assurance, éducation, logistique. Vérifie l'index avant d'attribuer un secteur : jamais deux cas dans le même secteur tant que la banque compte moins de 15 cas.
