# Checklist d'audit — détail opérationnel

Applique les quatre familles dans l'ordre A → D pour chaque cas. Chaque contrôle raté produit un finding : sévérité + localisation (section/ligne) + correction minimale proposée.

## A. Calculs (scripts `cases/validation/NN-<slug>.py`)

Structure attendue d'un script (en-tête : date, fichier de cas audité) :

```python
# Validation du cas NN-<slug>.md — généré par case-auditor le AAAA-MM-JJ
# Données brutes du cas (section Données + Clarifications)
prix, volume, marge = 10, 20_000_000, 0.75
# Un assert par chiffre affirmé dans le fichier
resultat = ...
assert resultat == 45, resultat
print("NN-<slug> : tous les calculs sont cohérents.")
```

Contrôles :

1. **Couverture totale** : chaque chiffre de « Calculs attendus », de la « Recommandation attendue », des exhibits et des en-têtes (ex. un « doublement » annoncé dans la ligne Twist) a son assert. Un script existant qui passe mais ne couvre pas un chiffre du fichier = à compléter avant de conclure.
2. **Dérivabilité** : chaque chiffre doit être calculable depuis les données que le candidat peut obtenir (données révélables + clarifications). Une hypothèse implicite nécessaire (jours ouvrés, taux de conversion, périmètre) = finding **majeur** : soit l'ajouter au fichier, soit retirer le chiffre.
3. **Cohérence interne des exhibits** : les lignes somment vers les totaux ; les colonnes d'un comparatif utilisent les mêmes définitions (périmètre, unités, horizon — un comparatif opex annualisé vs capex sec sans horizon est un finding) ; les unités sont homogènes.
4. **Faisabilité mentale** : chaque étape de calcul attendue du candidat est faisable de tête en < 20 s (pourcentages ronds : 10/20/25/30/40/50/60/75/80 %, multiples de 5, divisions exactes). Une division sale acceptable dans un sanity check d'ordre de grandeur, pas dans le chemin principal.
5. **Écarts scriptés** : si deux chiffres du fichier divergent volontairement (ex. prompt vs exhibit), la note interviewer doit couvrir la question probable du candidat — sur les deux périodes/colonnes, pas seulement une.

## B. Fuites de twist

Test unique : **« un candidat qui lit ce texte peut-il énoncer le twist sans raisonner ? »**

1. **Prompt d'ouverture** : le symptôme est légitime (baisse de profit, retards, churn) ; le diagnostic ou la moitié du diagnostic ne l'est pas. Signaux de fuite : une corrélation temporelle appuyée (« depuis le lancement de X »), la variable clé déjà isolée (« alors que Y est resté stable »), le client décrit mot pour mot comme la réponse attendue.
2. **Noms des données** : neutres. « D5 — LE PIÈGE » ou « D4 — Le contrat caché » trahissent ; « D5 — Canal revendeurs », « D4 — Contrats fournisseurs » non.
3. **Contenus des données** : des faits bruts, jamais la conclusion. Fuite type : « le goulot est X, pas Y » (diagnostic servi) au lieu de « les 20 recrues sont opérationnelles ; le nombre de vans chargés par matin n'a pas augmenté » (faits qui laissent le raisonnement au candidat). Réécrire en retirant toute phrase qui commence l'analyse à la place du candidat.
4. **Conditions de révélation** : la donnée qui débloque le twist doit se mériter par une question précise — vérifier que sa condition n'est pas satisfaite par une question générique probable, et qu'elle reste atteignable (une condition impossible à formuler naturellement = twist inaccessible, finding critique).
5. **Notes interviewer et exhibits** : une note qui décrit un piège étranger au tableau qu'elle annote = finding mineur (confusion en passation).

## C. Conformité au template canonique

Référence : `case-template.md` du skill case-generator.

1. **En-tête** : Type, Durée cible, Format, ligne Twist (documentant honnêtement « aucun » le cas échéant).
2. **Sections requises** : Prompt d'ouverture ; Clarifications autorisées ; Données à révéler sur demande ; « Calculs attendus (vérifiés) » ; Recommandation attendue. Exhibits : 1-2 sauf justification (un cas sans exhibit = finding majeur pour un cas moyen/difficile).
3. **Blocs conditionnels** : interviewer-led → « Questions imposées » (avec une question d'opinion piégée et réponse attendue) ; candidate-led → « Nudges autorisés » (1-2, formulés en questions) ; « les deux » → les deux blocs.
4. **Longueur** : 60-120 lignes. En dessous, l'interviewer improvisera ; au-dessus, il se perdra.
5. **Moment des exhibits** : indiqué, et toujours **après** le travail que le candidat doit produire (un exhibit qui pré-calcule les marges unitaires ou la réponse d'une question imposée = finding majeur : déplacer sa présentation ou retirer les colonnes de résultats).
6. **Nommage** : `NN-type-nomclient.md`, numéro unique cohérent avec l'index.

## D. Cohérence de l'index

1. **Ligne par cas** : fichier, type, secteur, format recommandé, difficulté, résumé de twist conformes au fichier réel.
2. **Règles de sélection** : chaque ID cité existe ; le mapping « dimension faible → cas » couvre les cas ajoutés depuis ; la liste des cas « bruit anti-métajeu » est exacte.
3. **Affirmations globales** : « secteurs tous distincts » et « mécaniques de twist toutes distinctes » vérifiées sur l'ensemble de la banque.
4. **Garantie de validation** : la phrase de l'index sur la validation Python doit correspondre à l'état réel de `cases/validation/` (après un audit complet : « tous les cas », scripts relançables à l'appui).

## Sévérités

| Sévérité | Définition | Exemples |
|---|---|---|
| **Critique** | Fausserait une session en la jouant telle quelle | Chiffre faux dans la solution ; cas insoluble avec les données fournies ; twist énoncé dans une donnée révélable |
| **Majeur** | Dégrade nettement la valeur d'entraînement | Bloc de format manquant (interviewer forcé d'improviser) ; chiffre non dérivable ; exhibit qui pré-calcule le travail du candidat ; fuite partielle dans le prompt |
| **Mineur** | Polish | Longueur hors bornes ; nom de section non canonique ; note interviewer ambiguë ; écart de recette de difficulté |

## Rapport type

```
## Audit du JJ/MM — périmètre : cas X, Y, Z

| Cas | Calculs | Fuites | Template | Index |
|---|---|---|---|---|
| 01 | KO (1 critique) | OK | KO (1 majeur) | OK |

### Findings
1. [CRITIQUE][cas 01, Recommandation] <description — détail complet si cas joué, classe+localisation sinon>
   → Correction proposée : <diff minimal>
```

Terminer par : scripts exécutés (liste + résultat) et corrections en attente de confirmation.
