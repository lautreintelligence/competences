---
type: "Procedure"
title: "Contributing"
description: "Procedure de contribution au marketplace competences : contrat de frontmatter des SKILL.md, ajout d'une skill ou d'un plugin, validations obligatoires et regles de branche."
status: "stable"
tags: ["genie-logiciel", "agent-ia", "packaging"]
created: 2026-08-21
---

# Contributing

Lire [docs/pieges-verifies.md](docs/pieges-verifies.md) et
[docs/conventions-de-nommage.md](docs/conventions-de-nommage.md) avant d'écrire un manifeste.
Les deux documents portent des comportements mesurés qui contredisent la documentation
courante, et des noms qu'on ne peut plus changer après publication.

## Frontmatter des SKILL.md

Le protocole n'autorise que six champs. Toute autre clé fait échouer l'envoi vers la
Skills API et vers claude.ai, alors que Claude Code l'accepte en local.

```
name  description  license  allowed-tools  metadata  compatibility
```

Ce dépôt en exige quatre.

| Champ | Statut | Contrainte |
|---|---|---|
| `name` | requis par le protocole | kebab-case strict, 64 caractères, identique au nom du dossier |
| `description` | requis par le protocole | 1024 caractères, aucun chevron `<` ou `>` |
| `license` | requis par ce dépôt | identifiant SPDX — `Apache-2.0` pour ce dépôt |
| `metadata` | requis par ce dépôt | objet portant `version`, `author` et `tags` |
| `allowed-tools` | facultatif | — |
| `compatibility` | facultatif | 500 caractères |

| Clé de `metadata` | Statut | Contrainte |
|---|---|---|
| `version` | requis | chaîne |
| `author` | requis | chaîne, `AIEN` par défaut |
| `tags` | requis | liste de chaînes, **trois au maximum** |

`metadata` est un objet libre. Il accueille les champs que le protocole refuse au premier
niveau — `version`, `homepage`, `argument-hint` — sans sortir du spec.

```yaml
---
name: fitz
description: >
  Ce que la skill produit. Utiliser quand les situations qui doivent la déclencher
  se présentent.
license: Apache-2.0
metadata:
  version: "0.1.0"
  author: "AIEN"
  tags: ["email", "redaction", "communication"]
---
```

Un seul `SKILL.md` par skill, à `skills/<skill-name>/SKILL.md`. Un `SKILL.md` imbriqué est
rejeté à l'envoi, même si Claude Code le charge en local. Un document d'appui se nomme
autrement : `references/<sujet>.md`.

## Ajouter une skill à un plugin existant

1. Créer `plugins/<plugin>/skills/<skill-name>/SKILL.md`.
2. Remplir le frontmatter selon le contrat ci-dessus.
3. Ajouter la ligne dans le tableau du `README.md` du plugin.
4. Incrémenter `version` dans les **deux** manifestes du plugin, et le `CHANGELOG.md`.
5. Valider, brancher, ouvrir une pull request.

## Ajouter un plugin

1. Choisir le nom selon [docs/conventions-de-nommage.md](docs/conventions-de-nommage.md) :
   `aien-<domaine>`. Il est immuable après publication.
2. Copier `templates/plugin-template/` sous `plugins/<plugin-name>/`.
3. Remplacer `plugin-template` par le nom dans les deux manifestes.
4. Supprimer tout composant inutilisé, et retirer la clé correspondante des manifestes.
5. Ajouter une entrée dans `.claude-plugin/marketplace.json` et dans
   `.agents/plugins/marketplace.json`. La `source` porte le chemin complet depuis la
   racine du dépôt : `"./plugins/<plugin-name>"`.
6. Valider, brancher, ouvrir une pull request.

## Valider avant de pousser

```bash
uv run scripts/validate-skills.py
claude plugin validate plugins/<plugin-name>
claude plugin validate .
```

Le premier contrôle le frontmatter de chaque `SKILL.md` du dépôt. Les deux autres
contrôlent les manifestes. Les trois doivent passer.

`scripts/validate-skills.py` porte son propre auto-contrôle :

```bash
uv run scripts/validate-skills.py --demo
```

## Branches et commits

Une branche par tâche, nommée `<type>/<description-courte>`. Jamais de commit direct
sur `main`.

Message de commit :

```
<type>(<scope>): <description à l'impératif, en français>
```

`type` parmi `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`.

## Renommer

Un renommage de plugin après publication exige une entrée dans `renames` du catalogue,
conservée indéfiniment :

```json
"renames": { "ancien-nom": "nouveau-nom" }
```

Sans elle, toute installation existante casse sans message utile.
