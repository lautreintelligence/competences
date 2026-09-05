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
| `name` | requis par le protocole | chaîne non vide, kebab-case strict, 64 caractères, identique au nom du dossier |
| `description` | requis par le protocole | chaîne non vide, 1024 caractères, aucun chevron `<` ou `>` |
| `license` | requis par ce dépôt | chaîne non vide — `Apache-2.0` pour ce dépôt |
| `metadata` | requis par ce dépôt | clés et valeurs de type chaîne ; `version`, `author` et `tags` requis |
| `allowed-tools` | facultatif | chaîne non vide, noms d'outils séparés par des espaces |
| `compatibility` | facultatif | chaîne non vide, 500 caractères |

| Clé de `metadata` | Statut | Contrainte |
|---|---|---|
| `version` | requis | chaîne non vide |
| `author` | requis | chaîne non vide, `L'Autre Intelligence & Nous` par défaut |
| `tags` | requis | chaîne contenant un à trois tags non vides, séparés par des virgules |

Le [standard Agent Skills](https://agentskills.io/specification#metadata-field) impose des clés et valeurs de type chaîne dans `metadata`.
Les propriétés supplémentaires, comme `homepage`, doivent respecter ce type. Les listes et objets imbriqués sont interdits.

```yaml
---
name: email-diplomatique
description: >
  Ce que la skill produit. Utiliser quand les situations qui doivent la déclencher
  se présentent.
license: Apache-2.0
metadata:
  version: "0.1.0"
  author: "L'Autre Intelligence & Nous"
  tags: "email, redaction, communication"
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
   un enjeu de compétences du ROME, en un mot, sans préfixe. Il est immuable après publication.
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
uv run --with pyyaml==6.0.3 python -m unittest discover -s scripts -p 'test_*.py'
uv run scripts/validate-releases.py --base-ref origin/main
claude plugin validate plugins/<plugin-name>
claude plugin validate .
```

Le premier contrôle les skills publiées et les gabarits. Les tests couvrent les valeurs invalides et les versions.
Le contrôle des versions compare les deux manifestes, leur nom et la présence d'une note de version.
Avec `--base-ref`, il exige une version supérieure pour chaque plugin modifié depuis cette révision Git.
Actualiser `origin/main` avec `git fetch origin` avant cette comparaison.
Les commandes Claude contrôlent les manifestes natifs. Tous ces contrôles doivent passer.

GitHub Actions exécute les contrôles Python à chaque pull request et sur `main`.
Sur les pull requests, la révision cible sert de référence au contrôle des hausses de version.
Ces contrôles ne remplacent pas un essai d'utilisation dans chaque agent.

`scripts/validate-skills.py` porte son propre auto-contrôle :

```bash
uv run scripts/validate-skills.py --demo
```

## Versions distribuées

Utiliser des versions stables `x.y.z`, sans zéro initial dans chaque composante.
Après toute modification distribuée d'un plugin, augmenter sa version dans les deux manifestes et compléter son `CHANGELOG.md`.
Les versions des deux manifestes doivent être identiques. Un changement de métadonnées est aussi une modification distribuée.
Incrémenter également `metadata.version` de chaque skill modifiée.
Documenter les anciennes et nouvelles invocations lors d'un renommage de skill.

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
