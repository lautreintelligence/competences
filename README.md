# competences

**Les compétences professionnelles, mises dans les mains de vos équipes par l'Intelligence Artificielle.**

Marketplace de plugins pour Claude Code et Codex, publié par
[L'Autre Intelligence & Nous](https://github.com/lautreintelligence), association loi 1901.

Nous ne vous expliquons pas l'intelligence artificielle. Nous vous la mettons dans les mains,
sous la forme de compétences prêtes à l'emploi : rédiger, structurer un problème, expliquer,
préparer un entretien, auditer du code.

## Installation

Ajoutez le marketplace, puis installez les plugins qui servent votre travail.

```
/plugin marketplace add lautreintelligence/competences
/plugin install communication@competences
```

```
codex plugin marketplace add lautreintelligence/competences
codex plugin add communication@competences
```

Un plugin installé est une copie réelle sur votre machine. Les compétences se chargent hors
ligne ; l’installation, la mise à jour et les appels aux serveurs MCP distants demandent le réseau.

## Les sept plugins

| Plugin | Installation | Ce qu'il vous donne |
|---|---|---|
| [`communication`](plugins/communication/README.md) | `/plugin install communication@competences` | Rédiger, reformuler, structurer une prise de parole — 3 compétences |
| [`organisation`](plugins/organisation/README.md) | `/plugin install organisation@competences` | Structurer un problème, décomposer un projet, distiller une session — 4 compétences |
| [`transmission`](plugins/transmission/README.md) | `/plugin install transmission@competences` | Expliquer, transmettre, vérifier un raisonnement — 3 compétences |
| [`strategie`](plugins/strategie/README.md) | `/plugin install strategie@competences` | Évaluer une idée de business et trancher — 1 compétence |
| [`carriere`](plugins/carriere/README.md) | `/plugin install carriere@competences` | Préparer les entretiens de conseil en stratégie — 4 compétences |
| [`technologie`](plugins/technologie/README.md) | `/plugin install technologie@competences` | Auditer du code, extraire une spécification d'interface — 2 compétences |
| [`data-gouv-fr`](plugins/data-gouv-fr/README.md) | `/plugin install data-gouv-fr@competences` | Rechercher et explorer les données publiques — connexion MCP |

Le README de chaque plugin décrit ses compétences, comment les appeler et ce qu'elles produisent.

## Comment c'est organisé

Les six plugins de compétences suivent les **enjeux de compétences du ROME**, le répertoire des métiers de France
Travail. Un professionnel y retrouve le vocabulaire de son propre parcours plutôt qu'un
découpage technique.

```
competences/
├── plugins/          sept plugins, dix-sept compétences
├── templates/        gabarits pour en écrire de nouvelles
├── scripts/          contrôle de conformité
└── docs/             conventions et spécifications
```

## Contribuer

La procédure, le contrat de rédaction et les règles de nommage sont dans
[CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[Apache-2.0](LICENSE). Usage commercial libre, modification libre, redistribution libre.
L'attribution est décrite dans [NOTICE](NOTICE).
