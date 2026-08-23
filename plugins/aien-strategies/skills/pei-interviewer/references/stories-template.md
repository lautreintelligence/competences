# Banque de stories — schéma et bootstrap

## Schéma de `pei-stories.json` (racine de la banque)

```json
{
  "version": 1,
  "stories": [
    {
      "id": "story-01",
      "titre": "Refonte du planning bénévoles contre l'avis du bureau",
      "dimensions": ["Connection", "Leadership"],
      "force": 3,
      "resume": "2-3 phrases : situation, enjeu, ce que le candidat a fait, résultat.",
      "moments_cles": [
        "La conversation où X a refusé — arguments échangés",
        "La décision de passer outre la procédure Y"
      ],
      "resultat": "Chiffré si possible (ex. +30 % de présence, 12 bénévoles retenus).",
      "apprentissage": "Ce que le candidat applique encore aujourd'hui.",
      "notes_creusement": "Points faibles révélés en session : dialogues flous sur le moment 2, impact non chiffré.",
      "derniere_session": "2026-07-12"
    }
  ]
}
```

Règles :
- `dimensions` : 1-2 par story (une story qui « couvre tout » ne couvre rien — la rattacher à sa dimension la plus forte).
- `force` (1-5) : évaluation honnête de la story **telle que racontée aujourd'hui**, pas de son potentiel. Réévaluée à chaque session.
- `moments_cles` : les 2-3 scènes que le creusement visitera — c'est là que la story vit ou meurt.
- 4 à 6 stories au total ; chaque dimension (Connection, Drive, Leadership, Growth) doit avoir au moins une story à force ≥ 3.

## Qualité d'une story PEI (à vérifier au bootstrap)

Une bonne story PEI n'est pas une ligne de CV réussie, c'est une **expérience traversée** :

1. **Un obstacle réel**, de préférence interpersonnel (désaccord, résistance, conflit, échec) — sans opposition, rien n'est testé.
2. **Un rôle personnel isolable** : le candidat peut dire « moi » à chaque étape décisive.
3. **Des scènes** : conversations, décisions datées, lieux — matière à 15 questions de creusement sans tourner à vide.
4. **Un résultat attribuable**, chiffré quand c'est possible.
5. **Un apprentissage appliqué depuis**, avec un exemple d'application.

Équilibre du récit visé en entretien : ~20 % contexte, ~60 % actions personnelles, ~20 % résultat et recul.

## Questions de bootstrap (interview guidée après lecture du CV)

Pour chaque expérience prometteuse du CV :

- « Racontez-moi le moment le plus difficile de cette expérience. »
- « Qui n'était pas d'accord avec vous, et sur quoi ? »
- « Qu'avez-vous accompli là-bas dont vous êtes le plus fier — et qu'est-ce qui aurait pu faire échouer ? »
- « Y a-t-il eu un moment où vous avez failli abandonner ou vous tromper lourdement ? »

Pour déterrer les dimensions manquantes :

- **Connection** : « Quand avez-vous dû faire changer d'avis quelqu'un de plus senior / plus têtu que vous ? »
- **Drive** : « Quel objectif vous êtes-vous fixé que personne ne vous demandait d'atteindre ? »
- **Leadership** : « Quand avez-vous été responsable d'un groupe qui n'avançait pas ? »
- **Growth** : « Quel est l'échec ou le feedback qui vous a le plus changé ? Racontez-moi le jour où vous l'avez reçu. »

Hors CV aussi : associatif, sport, projets personnels — le PEI n'exige pas du professionnel, il exige du vécu.

## Ce qu'on ne met PAS dans la banque

- Des stories inventées ou « améliorées » : elles s'effondrent au creusement (c'est précisément ce que le creusement détecte).
- Plus de 6 stories : mieux vaut 4 histoires profondes que 8 superficielles.
- Des réponses rédigées mot pour mot : la banque stocke la matière (moments, faits, chiffres), pas un script à réciter.
