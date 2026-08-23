# competences

Marketplace d'**AIEN**. Il sert Claude Code et Codex depuis le même dépôt.

## Pour un agent qui arrive ici

Lire dans cet ordre, avant toute modification :

| Document | Ce qu'il fixe |
|---|---|
| [docs/conventions-de-nommage.md](docs/conventions-de-nommage.md) | noms de marketplace, de plugin et de skill — immuables après publication |
| [docs/pieges-verifies.md](docs/pieges-verifies.md) | dix comportements mesurés qui contredisent la documentation courante |
| [CONTRIBUTING.md](CONTRIBUTING.md) | contrat de frontmatter, procédure d'ajout, validations obligatoires |
| [docs/gabarit-de-repo-marketplace-multi-harness.md](docs/gabarit-de-repo-marketplace-multi-harness.md) | spécification complète des manifestes et des composants |

`docs/pieges-verifies.md` évite de refaire des erreurs déjà payées. Le lire avant d'écrire
un manifeste, pas après un échec de validation.

## Structure

```
competences/
├── .claude-plugin/marketplace.json     catalogue Claude Code — name: competences
├── .agents/plugins/marketplace.json    catalogue Codex
├── plugins/
│   ├── aien-communication-pro/         fitz, presentation-architect
│   ├── aien-strategies/                case-partner, case-generator, case-auditor,
│   │                                   pei-interviewer, minto
│   ├── aien-thinking/                  problem-framing, brainstorm, doublecheck,
│   │                                   mece-checklist, first-principles, sprezzatura,
│   │                                   unslop, session-digest
│   └── aien-dev/                       clean-code-audit, ui-to-spec
├── templates/
│   ├── plugin-template/                gabarit complet, deux harnesses
│   └── skill-template/
├── scripts/validate-skills.py          contrôle le contrat de frontmatter
└── docs/
```

## Installation

```
/plugin marketplace add lautreintelligence/competences
/plugin install aien-communication-pro@competences
/plugin install aien-strategies@competences
/plugin install aien-thinking@competences
/plugin install aien-dev@competences
```

```
codex plugin marketplace add lautreintelligence/competences
codex plugin add aien-communication-pro
codex plugin add aien-strategies
codex plugin add aien-thinking
codex plugin add aien-dev
```

Un plugin installé est une copie réelle sous `~/.claude/plugins/cache/`. Les skills se
chargent hors ligne ; seules l'installation et la mise à jour demandent le réseau.

## Plugins

| Plugin | Installation | Skills |
|---|---|---|
| [`aien-communication-pro`](plugins/aien-communication-pro/README.md) | `/plugin install aien-communication-pro@competences` | Rédaction et communication professionnelle — 2 skills |
| [`aien-strategies`](plugins/aien-strategies/README.md) | `/plugin install aien-strategies@competences` | Préparation aux entretiens de conseil en stratégie — 5 skills |
| [`aien-thinking`](plugins/aien-thinking/README.md) | `/plugin install aien-thinking@competences` | Raisonner, expliquer, mettre en forme la pensée — 8 skills |
| [`aien-dev`](plugins/aien-dev/README.md) | `/plugin install aien-dev@competences` | Audit de code et spécification d'interface — 2 skills |

Le README de chaque plugin décrit ses skills, leur invocation et ce qu'elles produisent.

## Avant de pousser

Les six validations doivent passer :

```bash
uv run scripts/validate-skills.py
claude plugin validate plugins/aien-communication-pro
claude plugin validate plugins/aien-strategies
claude plugin validate plugins/aien-thinking
claude plugin validate plugins/aien-dev
claude plugin validate .
```
