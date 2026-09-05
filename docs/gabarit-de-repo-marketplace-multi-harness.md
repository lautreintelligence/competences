---
type: "Specification"
title: "Gabarit de repo marketplace multi-harness"
description: "Structure d'un repo marketplace servant Claude Code, Codex et le socle neutre .agents/ : catalogues, manifestes de plugin, fichiers de composants, variables substituables et règles de nommage."
status: "draft"
tags: ["genie-logiciel", "agent-ia", "packaging", "interoperabilite"]
created: 2026-08-21
related: ["[[Claude Code]]", "[[Codex]]", "[[Model Context Protocol]]"]
---

# Gabarit de repo marketplace multi-harness

Patron neutre pour un repo marketplace servant Claude Code, Codex et le socle neutre `.agents/`. Il s'applique à un repo public comme à un repo privé.

Les blocs de code de ce document sont annotés en JSONC. Les fichiers réels du repo sont en JSON strict, sans commentaires : `plugin.json` et `marketplace.json` échouent à la validation si un commentaire y figure. Le gabarit exécutable correspondant se trouve dans `templates/plugin-template/`.

Placeholders : `<org>`, `<repo>`, `<marketplace-name>`, `<plugin-name>`, `<skill-name>`, `<agent-name>`, `<server-name>`, `<category>`.

## 1. Portée

| Élément | Claude Code | Codex | Neutre | Mutualisable |
|---|---|---|---|---|
| Catalogue | `.claude-plugin/marketplace.json` | `.agents/plugins/marketplace.json` | — | non |
| Manifeste plugin | `.claude-plugin/plugin.json` | `.codex-plugin/plugin.json` | — | non |
| Skills | `skills/<n>/SKILL.md` | `skills/<n>/SKILL.md` | `SKILL.md` (spec) | oui |
| Serveurs MCP | `.mcp.json` | `.mcp.json` | — | oui |
| Hooks | `hooks/hooks.json` | `hooks.json` (racine) | — | non |
| Sous-agents | `agents/<n>.md` | `agents/openai.yaml` | — | non |
| Commandes | `commands/<n>.md` | `commands/<n>.md` | — | oui (legacy) |
| LSP | `.lsp.json` | — | — | Claude seul |
| Monitors | `monitors/monitors.json` | — | — | Claude seul |
| Workflows | `workflows/*.js` | — | — | Claude seul |
| Output styles | `output-styles/*.md` | — | — | Claude seul |
| Thèmes | `themes/*.json` | — | — | Claude seul |
| Exécutables | `bin/` | `scripts/` | — | non |
| Connecteurs | via MCP | `.app.json` | — | non |
| Contexte projet | `CLAUDE.md` | `AGENTS.md` | `AGENTS.md` | non |
| Skills projet | `.claude/skills/` | `.agents/skills/` | `.agents/skills/` | via symlink |

`skills/` est le seul répertoire réellement portable. Un plugin qui ne contient que `skills/` fonctionne sur les deux harnesses sans adaptation.

## 2. Arborescence du repo marketplace

```
<org>/<repo>/
├── .claude-plugin/
│   └── marketplace.json                  # catalogue Claude Code
├── .agents/
│   ├── plugins/
│   │   └── marketplace.json              # catalogue Codex
│   └── skills/                           # optionnel — skills projet, chemin neutre
├── plugins/                              # plugins produits et maintenus ici
│   └── <plugin-name>/
├── external_plugins/                     # optionnel — contributions tierces
├── templates/
│   ├── plugin-template/
│   └── skill-template/
│       └── SKILL.md
├── docs/
├── .github/
│   ├── workflows/
│   │   └── validate.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── ISSUE_TEMPLATE/
│   └── CODEOWNERS
├── AGENTS.md                             # instructions projet — Codex et outils neutres
├── CLAUDE.md                             # instructions projet — Claude Code
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
├── NOTICE
├── .gitignore
└── README.md
```

## 3. Arborescence d'un plugin

Aucun élément n'est obligatoire, sauf le manifeste du harness visé.

```
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json                       # manifeste Claude Code — seul fichier autorisé ici
├── .codex-plugin/
│   └── plugin.json                       # manifeste Codex
├── skills/                               # portable — lu par Claude Code et Codex
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── references/                   # chargé à la demande depuis SKILL.md
│       ├── assets/
│       └── scripts/
├── SKILL.md                              # alternative mono-skill, sans dossier skills/
├── commands/
│   └── <command-name>.md                 # → /<plugin-name>:<command-name>
├── agents/
│   ├── <agent-name>.md                   # sous-agent Claude Code
│   └── openai.yaml                       # métadonnées d'agent Codex
├── hooks/
│   └── hooks.json                        # hooks Claude Code
├── hooks.json                            # hooks Codex — à la racine du plugin
├── workflows/<workflow-name>.js          # Claude Code
├── output-styles/<style-name>.md         # Claude Code
├── themes/<theme-name>.json              # Claude Code (expérimental)
├── monitors/monitors.json                # Claude Code (expérimental)
├── bin/<executable>                      # Claude Code — ajouté au PATH du Bash
├── scripts/                              # scripts appelés par hooks et commandes
├── ui/                                   # Codex — ressources d'interface
├── assets/                               # icônes et captures référencées au manifeste Codex
├── .mcp.json                             # serveurs MCP — Claude Code et Codex
├── .lsp.json                             # serveurs LSP — Claude Code
├── .app.json                             # connecteurs — Codex
├── settings.json                         # Claude Code — défauts à l'activation
├── package.json                          # dépendances Node auto-installées si lockfile
├── plugin.lock.json                      # Codex — verrou de dépendances
├── CHANGELOG.md
├── README.md
└── LICENSE
```

Contraintes de chemins :

- `.claude-plugin/` et `.codex-plugin/` ne contiennent rien d'autre que `plugin.json`.
- Tout chemin déclaré au manifeste est relatif et commence par `./`. `../` est interdit.
- Le plugin root est le dossier du plugin, jamais `~/.claude/`.

## 4. Catalogues

### 4.1 Claude Code

Fichier `.claude-plugin/marketplace.json`.

```jsonc
{
  "$schema": "https://json.schemastore.org/claude-code-marketplace.json",

  // obligatoire
  "name": "<marketplace-name>",            // kebab-case, unique par utilisateur
                                           // noms réservés interdits : claude-*, anthropic-*
  "owner": {
    "name": "<owner-name>",                // obligatoire
    "email": "<email>",                    // optionnel
    "url": "<url>"                         // optionnel
  },
  "plugins": [],

  // optionnel
  "description": "<description>",
  "version": "<version-du-manifeste>",
  "allowCrossMarketplaceDependenciesOn": ["<autre-marketplace>"],
  "renames": {
    "<ancien-nom>": "<nouveau-nom>",
    "<nom-supprime>": null
  }
}
```

Entrée de plugin :

```jsonc
{
  // obligatoire
  "name": "<plugin-name>",                 // kebab-case, identifiant public, immuable
  "source": "<source>",                    // chaîne ou objet, voir les formes ci-dessous

  // métadonnées
  "displayName": "<libellé UI>",
  "description": "<description>",
  "version": "<x.y.z>",                    // posé ici ou dans plugin.json ⇒ épingle
  "author": { "name": "<n>", "email": "<e>", "url": "<u>" },
  "homepage": "<url>",
  "repository": "<url>",
  "license": "<SPDX>",
  "keywords": ["<kw>"],
  "metadata": {},                          // libre, ignoré par le client
  "category": "<category>",
  "tags": ["<tag>"],
  "defaultEnabled": true,
  "strict": true,                          // plugin.json fait autorité sur les composants
  "relevance": {},                         // suggestions contextuelles (managed settings)

  // chemins de composants — surcharge du manifeste
  "skills":     "<path|array>",
  "commands":   "<path|array>",
  "agents":     "<path|array>",
  "hooks":      "<path|object>",
  "mcpServers": "<path|object>",
  "lspServers": "<path|object>"
}
```

Formes de `source` :

```jsonc
"./<dossier>"                                                          // relatif au repo
{ "source": "github",    "repo": "<owner>/<repo>", "ref": "<branche|tag>", "sha": "<commit>" }
{ "source": "url",       "url": "<git-url>", "ref": "<ref>", "sha": "<commit>" }
{ "source": "git-subdir","url": "<git-url>", "path": "<sous-dossier>", "ref": "<ref>", "sha": "<commit>" }
{ "source": "npm",       "package": "<pkg>", "version": "<semver>", "registry": "<url>" }
{ "source": "archive",   "url": "<https-zip>", "sha256": "<64-hex>" }
{ "source": "command",   "command": "<cmd>", "timeout": 60, "mode": "copy|link" }
```

Un chemin relatif part de la racine du dépôt : `"./plugins/<plugin-name>"`, jamais `"./<plugin-name>"`.

`sha` l'emporte sur `ref` quand les deux sont posés.

### 4.2 Codex

Fichier `.agents/plugins/marketplace.json`.

```jsonc
{
  "name": "<marketplace-name>",
  "interface": {
    "displayName": "<libellé affiché>"
  },
  "plugins": [
    {
      "name": "<plugin-name>",
      "source": {
        "source": "local",
        "path": "./plugins/<plugin-name>"
      },
      "policy": {
        "installation": "AVAILABLE",       // gouvernance portée par le catalogue
        "authentication": "ON_INSTALL",    // ou ON_USE
        "products": ["CODEX"]              // optionnel — filtrage par surface
      },
      "category": "<category>"
    }
  ]
}
```

L'entrée ne porte ni `version` ni `description`. Ces valeurs viennent du manifeste du plugin.

## 5. Manifestes de plugin

### 5.1 Claude Code

Fichier `.claude-plugin/plugin.json`.

```jsonc
{
  "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",

  // identité
  "name": "<plugin-name>",                 // obligatoire, kebab-case, immuable
                                           // sert de namespace : /<plugin-name>:<skill-name>
  "displayName": "<libellé UI>",
  "version": "<x.y.z>",                    // épingle si posé — à incrémenter à chaque release
  "description": "<description>",
  "author": { "name": "<n>", "email": "<e>", "url": "<u>" },
  "homepage": "<url>",
  "repository": "<url>",
  "license": "<SPDX>",
  "keywords": ["<kw>"],
  "metadata": {},
  "defaultEnabled": true,                  // false = installé mais désactivé

  // chemins de composants
  "skills":       ["./skills/"],           // s'ajoute aux emplacements par défaut
  "commands":     ["./commands/"],         // remplace
  "agents":       ["./agents/<agent-name>.md"],  // remplace — fichiers, pas dossier
  "workflows":    "./workflows/",          // remplace
  "outputStyles": "./output-styles/",      // remplace
  "hooks":        "./hooks/hooks.json",    // fusionne
  "mcpServers":   "./.mcp.json",           // fusionne
  "lspServers":   "./.lsp.json",           // fusionne
  "experimental": {
    "themes":   "./themes/",
    "monitors": "./monitors/monitors.json"
  },

  // configuration demandée à l'utilisateur
  "userConfig": {
    "<clé>": {
      "type": "string",                    // string | number | boolean | file | directory
      "title": "<label>",                  // obligatoire
      "description": "<aide>",             // obligatoire
      "required": false,
      "sensitive": false,                  // masque la saisie, stockage sécurisé
      "default": "<valeur>",
      "multiple": false,                   // type string — autorise un tableau
      "min": 0, "max": 10                  // type number
    }
  },

  // canaux — intégrations de messagerie
  "channels": [
    { "server": "<server>", "userConfig": {} }
  ],

  // dépendances vers d'autres plugins
  "dependencies": [
    "<plugin-name>",
    { "name": "<plugin-name>", "version": "^1.0.0" }
  ]
}
```

`agents` n'accepte pas un chemin de dossier. Le validateur de la version 2.1.220 rejette `"./agents/"` et `"./agents"`, et exige un ou plusieurs chemins de fichiers `.md` existants. Les autres clés de composants acceptent un dossier.

Les valeurs `userConfig` se lisent par `${user_config.<clé>}` dans les fichiers de composants, ou par la variable d'environnement `CLAUDE_PLUGIN_OPTION_<CLÉ>`.

### 5.2 Codex

Fichier `.codex-plugin/plugin.json`.

```jsonc
{
  "name": "<plugin-name>",
  "version": "<x.y.z>",
  "description": "<description>",
  "author": { "name": "<n>", "url": "<u>" },
  "homepage": "<url>",
  "repository": "<url>",
  "license": "<SPDX>",
  "keywords": ["<kw>"],

  // chemins de composants
  "skills": "./skills/",
  "mcpServers": "./.mcp.json",
  "apps": "./.app.json",

  // fiche vitrine — spécifique Codex
  "interface": {
    "displayName": "<libellé>",
    "shortDescription": "<une ligne>",
    "longDescription": "<paragraphe>",
    "developerName": "<éditeur>",
    "category": "<category>",
    "capabilities": ["Interactive", "Read", "Write"],
    "websiteURL": "<url>",
    "privacyPolicyURL": "<url>",
    "termsOfServiceURL": "<url>",
    "defaultPrompt": ["<suggestion 1>", "<suggestion 2>"],
    "brandColor": "#<hex>",
    "composerIcon": "./assets/<icone>.png",
    "logo": "./assets/<logo>.png",
    "screenshots": ["./assets/<capture>.png"]
  }
}
```

## 6. Fichiers de composants

### 6.1 SKILL.md

Fichier `skills/<skill-name>/SKILL.md`.

```markdown
---
name: <skill-name>                 # = nom du dossier, kebab-case
description: >                     # champ qui pilote le déclenchement automatique
  <ce que la skill produit>. Utiliser quand <situations, formulations utilisateur>.
license: <SPDX>
compatibility: <contrainte>
metadata: {}
allowed-tools: <Outil(motif) ...>  # pré-approuve des outils pour le tour d'invocation
disable-model-invocation: false    # true = invocable seulement par slash
user-invocable: true               # false = invocable seulement par le modèle
context: fork                      # exécute la skill dans un sous-agent isolé
---
```

Portabilité du frontmatter :

| Champ | Claude Code | Codex | claude.ai et Skills API |
|---|---|---|---|
| `name` `description` `license` `compatibility` `metadata` `allowed-tools` | oui | oui | oui — les six seuls acceptés |
| `disable-model-invocation` | oui | oui | non |
| `user-invocable` `context` | oui | non | non |
| Injection dynamique par backtick-bang | oui | non | non |
| `${CLAUDE_PLUGIN_ROOT}` | oui | non | non |

Toute clé hors des six du spec fait échouer l'envoi vers claude.ai et vers la Skills API. Le validateur exige `name` et `description`, limite `name` à 64 caractères en kebab-case strict, `description` à 1024 caractères sans chevron, et `compatibility` à 500 caractères.

Claude Code tolère des clés hors spec. Un relevé de 373 `SKILL.md` installées en montre six : `user-invocable` (151), `argument-hint` (140), `version` (139), `homepage` (12), `tools` (2), `disable-model-invocation` (1). Elles ferment la porte à claude.ai. Les clés supplémentaires de `metadata` doivent avoir des valeurs de type chaîne, conformément au [standard Agent Skills](https://agentskills.io/specification#metadata-field).

Ce dépôt exige quatre champs — `name`, `description`, `license`, `metadata` — et trois clés sous `metadata` : `version`, `author`, `tags`.
Ces trois valeurs sont des chaînes non vides. `tags` contient un à trois tags séparés par des virgules, par exemple `tags: "redaction, edition, style"`.
Voir [CONTRIBUTING.md](../CONTRIBUTING.md).

### 6.2 Hooks

Fichier `hooks/hooks.json` pour Claude Code, `hooks.json` à la racine du plugin pour Codex.

```jsonc
{
  "hooks": {
    "<EventName>": [
      {
        "matcher": "<motif>",              // filtre sur l'outil ou le fichier
        "if": "<condition>",
        "hooks": [
          { "type": "command",  "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/<script>" },
          { "type": "command",  "command": ["<script>", "<arg>"] },
          { "type": "http",     "url": "<url>", "headers": {} },
          { "type": "mcp_tool", "server": "plugin:<plugin-name>:<server-name>", "tool": "<tool>" },
          { "type": "prompt",   "prompt": "<instruction ${ARGUMENTS}>", "model": "<model-id>" },
          { "type": "agent",    "agent": "plugin:<plugin-name>:<agent-name>" }
        ]
      }
    ]
  }
}
```

Événements : `SessionStart`, `Setup`, `UserPromptSubmit`, `UserPromptExpansion`, `PreToolUse`, `PermissionRequest`, `PermissionDenied`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Notification`, `MessageDisplay`, `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `Stop`, `StopFailure`, `InstructionsLoaded`, `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`, `PreCompact`, `PostCompact`, `Elicitation`, `ElicitationResult`, `SessionEnd`.

### 6.3 Serveurs MCP

Fichier `.mcp.json`.

```jsonc
{
  "mcpServers": {
    "<server-name>": {
      "command": "${CLAUDE_PLUGIN_ROOT}/<binaire>",
      "args": ["<arg>"],
      "env": { "<VAR>": "${CLAUDE_PLUGIN_DATA}" },
      "timeout": 30000
    },
    "<server-name-http>": {
      "type": "http",                      // stdio (défaut) | http | sse | ws
      "url": "<url>",
      "headers": { "Authorization": "Bearer ${user_config.<clé>}" }
    }
  }
}
```

Le nom d'outil résultant est `mcp__plugin_<plugin-name>_<server-name>__<tool>`.

### 6.4 Serveurs LSP

Fichier `.lsp.json`, Claude Code seulement.

```jsonc
{
  "<language-id>": {
    "command": "<binaire>",                              // obligatoire, doit être dans le PATH
    "extensionToLanguage": { ".<ext>": "<language-id>" }, // obligatoire
    "args": ["<arg>"],
    "transport": "stdio",                                // stdio | socket
    "env": { "<VAR>": "<valeur>" },
    "initializationOptions": {},
    "settings": {},
    "workspaceFolder": "${CLAUDE_PROJECT_DIR}",
    "startupTimeout": 5000,
    "shutdownTimeout": 3000,
    "restartOnCrash": true,
    "maxRestarts": 3,
    "diagnostics": true
  }
}
```

### 6.5 Monitors

Fichier `monitors/monitors.json`, Claude Code seulement, expérimental.

```jsonc
[
  {
    "name": "<monitor-name>",              // obligatoire, unique dans le plugin
    "command": "<commande persistante>",   // obligatoire — chaque ligne stdout est notifiée
    "description": "<résumé>",             // obligatoire — affiché dans le panneau
    "when": "always"                       // always | on-skill-invoke:<skill-name>
  }
]
```

Les monitors ne supportent pas `${user_config.*}` et ne fonctionnent qu'en session interactive.

### 6.6 Connecteurs Codex

Fichier `.app.json`.

```jsonc
{
  "apps": {
    "<app-name>": { "id": "<connector-id>" }
  }
}
```

### 6.7 Sous-agents Claude Code

Fichier `agents/<agent-name>.md`.

```markdown
---
name: <agent-name>
description: <quand déléguer à cet agent>
tools: <liste d'outils autorisés>
model: <model-id>
---

<system prompt du sous-agent>
```

Un hook le référence par `plugin:<plugin-name>:<agent-name>`.

### 6.8 Réglages d'activation

Fichier `settings.json` à la racine du plugin, Claude Code seulement.

```jsonc
{
  "agent": "<agent-name>",                 // active un agent du plugin comme thread principal
  "subagentStatusLine": "<config>"
}
```

Ce fichier est prioritaire sur la clé `settings` du `plugin.json`. Les clés inconnues sont ignorées.

## 7. Variables substituables

| Variable | Résout vers | Portée |
|---|---|---|
| `${CLAUDE_PLUGIN_ROOT}` | dossier d'installation du plugin | Claude Code |
| `${CLAUDE_PLUGIN_DATA}` | `~/.claude/plugins/data/<id>/`, persiste entre versions | Claude Code |
| `${CLAUDE_PROJECT_DIR}` | racine du projet | Claude Code |
| `${user_config.<clé>}` | valeur `userConfig` non sensible | Claude Code |
| `CLAUDE_PLUGIN_OPTION_<CLÉ>` | valeur `userConfig`, y compris sensible, par l'environnement | Claude Code |

## 8. Invocation et namespace

```
/<skill-name>                    skill personnelle, projet ou entreprise
/<plugin-name>:<skill-name>      skill fournie par un plugin — toujours namespacée
```

- Le préfixe vient du champ `name` du manifeste du plugin.
- Une skill de plugin n'entre jamais en conflit avec les autres niveaux.
- Hors plugins, l'ordre de priorité est : entreprise, personnel, projet.
- Une skill de n'importe quel niveau surcharge une skill intégrée de même nom.
- `commands/<n>.md` et `skills/<n>/SKILL.md` produisent la même commande. En cas d'homonymie, la skill l'emporte.

## 9. Correspondance des commandes

| Action | Claude Code | Codex |
|---|---|---|
| Ajouter le catalogue | `/plugin marketplace add <org>/<repo>` | `codex plugin marketplace add <org>/<repo>` |
| Installer | `/plugin install <plugin>@<marketplace>` | `codex plugin add <plugin>` |
| Recharger | `/reload-plugins` | redémarrage |
| Valider | `claude plugin validate <path>` | — |
| Tester en local | `claude --plugin-dir <path>` | — |
| Cache | `~/.claude/plugins/cache/` | `~/.codex/plugins/cache/` |

`claude plugin validate` n'expose aucune option en version 2.1.220 : son aide ne liste que `-h`. Un `--strict` documenté ailleurs n'existe pas dans cette version. Vérifier l'aide de la version installée avant de câbler la validation en intégration continue.

## 10. Checklist de mise en place

- [ ] `name` du marketplace choisi, kebab-case, hors noms réservés.
- [ ] `name` de chaque plugin arrêté définitivement — il est immuable après publication.
- [ ] Stratégie de version tranchée : `version` explicite incrémentée à chaque release, ou champ absent sur source git, le SHA faisant office de version.
- [ ] `version` déclaré à un seul endroit. `plugin.json` l'emporte silencieusement.
- [ ] Frontmatter des `SKILL.md` limité aux six champs du spec si la portabilité claude.ai est visée.
- [ ] `renames` prévu avant tout renommage ou retrait.
- [ ] Sources tierces épinglées par `sha`, et non par `ref` seul.
- [ ] `claude plugin validate` passe sur chaque plugin.
- [ ] Contenu de `hooks/`, `bin/` et `.mcp.json` documenté dans le README du plugin.
