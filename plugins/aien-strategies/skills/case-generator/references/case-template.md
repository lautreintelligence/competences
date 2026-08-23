# Template canonique d'un fichier de cas

Reproduis cette structure à l'identique — l'interviewer du skill case-partner en dépend. Les commentaires entre ⟨crochets⟩ décrivent ce qu'il faut mettre.

```markdown
# Cas NN — ⟨NomClient⟩ (⟨Type⟩)

**Type** : ⟨Profitabilité | Entrée de marché | M&A | Pricing | Market sizing | Croissance | Opérations⟩ | **Durée cible** : ⟨X-Y min⟩ | **Format** : ⟨interviewer-led / candidate-led / les deux⟩
**Twist** : ⟨l'insight central en une phrase — visible seulement par l'interviewer⟩

## Prompt d'ouverture (à lire au candidat)

« ⟨3-4 phrases : qui est le client, contexte, symptôme ou ambition, question posée. Rien qui divulgue le twist.⟩ »

## Clarifications autorisées (si demandées)

- ⟨Périmètre, objectif chiffré du client, horizon de temps — les 2-4 questions de clarification les plus probables et leurs réponses.⟩

## Données — À RÉVÉLER UNIQUEMENT SUR DEMANDE EXPLICITE

**D1 — ⟨Nom neutre de la donnée⟩ (⟨condition de révélation : "si le candidat demande X"⟩)**
⟨Contenu.⟩

**D2 — ...** ⟨3 à 6 blocs. La donnée qui débloque le twist doit porter une condition de révélation exigeante — le candidat doit la mériter par une bonne question. Ne jamais nommer une donnée d'une façon qui trahit le twist.⟩

## Exhibit A — ⟨Titre⟩

⟨Tableau markdown. 1 à 2 exhibits par cas. Indiquer le moment de présentation si le cas est interviewer-led. Ajouter si utile une "note interviewer" sur les pièges de lecture de l'exhibit.⟩

## Calculs attendus (vérifiés)

⟨Chaque calcul que le candidat doit produire, avec le résultat exact. Tous validés par le script Python. Terminer par l'insight central chiffré.⟩

## Questions imposées (format interviewer-led uniquement)

1. « Comment structureriez-vous... »
2. ⟨4-5 questions dans l'ordre, dont une question d'opinion piégée ("le CFO propose X, qu'en pensez-vous ?") avec la réponse attendue entre parenthèses.⟩
5. Synthèse 60 secondes.

## Nudges autorisés (candidate-led, un seul si blocage > 3 échanges)

- ⟨1-2 relances légères, formulées comme des questions, jamais comme des indices directs.⟩

## Recommandation attendue (fourchette acceptable)

⟨La recommandation corrigée, hiérarchisée, chiffrée quand c'est possible. Préciser ce qui distingue un candidat "correct" d'un candidat "top" sur ce cas, et quelles conclusions alternatives restent acceptables.⟩
```

## Contraintes transverses

- Longueur totale du fichier : 60 à 120 lignes. En dessous, l'interviewer devra improviser ; au-dessus, il se perd.
- Tout chiffre du fichier doit apparaître dans le script de validation Python.
- Le bloc « Nudges » n'existe que pour les cas jouables en candidate-led ; le bloc « Questions imposées » que pour les cas jouables en interviewer-led. Un cas « les deux formats » a les deux blocs.
