---
type: "Guide"
title: "README"
description: "Configuration et utilisation du plugin data-gouv-fr avec le serveur MCP officiel de data.gouv.fr."
status: "stable"
tags: ["donnee-publique", "interoperabilite", "agent-ia"]
created: 2026-09-05
sources:
  - title: "data.gouv.fr MCP Server"
    author: "data.gouv.fr"
    resource: "https://github.com/datagouv/datagouv-mcp"
---

# data-gouv-fr

Plugin de la marketplace **competences**, publié par L’Autre Intelligence & Nous.
Il connecte Claude Code et Codex au serveur MCP officiel de data.gouv.fr.
Ce plugin est indépendant de l’équipe data.gouv.fr.

## Contenu

- `.claude-plugin/plugin.json` : manifeste Claude Code.
- `.codex-plugin/plugin.json` : manifeste Codex.
- `.mcp.json` : connexion HTTP à `https://mcp.data.gouv.fr/mcp`.

Le serveur distant fournit les outils. Aucun serveur local ni clé API n’est nécessaire.
Une connexion Internet est requise. Les outils du serveur sont actuellement en lecture seule.
Cette version contient uniquement la connexion MCP, sans compétence, agent ou script supplémentaire.

## Utilisation

Après installation du plugin depuis la marketplace competences, ouvrir une nouvelle session.
Demander par exemple : « Recherche des jeux de données sur la population des communes françaises. »
Vérifier que la réponse utilise les outils du serveur `datagouv` et cite les jeux de données consultés.
La consultation tabulaire dépend des ressources prises en charge par le serveur.

## Vérification locale

Depuis la racine du dépôt :

```sh
claude plugin validate plugins/data-gouv-fr
python3 scripts/validate-releases.py
```

La validation des fichiers ne remplace pas un essai de chargement du MCP dans chaque application.
Les outils et limites du service sont décrits dans la [documentation officielle](https://github.com/datagouv/datagouv-mcp).
