---
type: "Register"
title: "Pièges vérifiés"
description: "Comportements de Claude Code et de la CLI Codex qui contredisent la documentation courante des plugins et des skills : chemins de source, clé agents, champs de frontmatter, plans d'installation, nettoyage des caches. Chaque entrée porte la mesure qui l'établit."
status: "stable"
tags: ["genie-logiciel", "agent-ia", "packaging"]
created: 2026-08-21
---

# Pièges vérifiés

Chaque entrée a été mesurée, pas déduite d'une documentation. Les entrées 1 à 13 ont été établies sur **Claude Code 2.1.220**, les entrées 14 à 17 sur **Claude Code 2.1.201** et sur la CLI **Codex** livrée avec l'application ChatGPT, le 23 août 2026. Vérifier de nouveau après une montée de version : ces comportements peuvent changer sans préavis.

Le format est constant : ce qui a été observé, la commande qui l'établit, ce qu'il faut écrire.

## 1. `metadata.pluginRoot` n'est pas appliqué à `source`

**Observé.** Un catalogue déclarant `"metadata": {"pluginRoot": "./plugins"}` et une entrée `"source": "./mon-plugin"` produit à l'installation :

```
✘ Failed to install plugin: Source path does not exist:
  ~/.claude/plugins/marketplaces/<mkt>/mon-plugin
```

Le clone contient pourtant `plugins/mon-plugin`. L'installateur résout `source` depuis la racine du dépôt et ignore le préfixe.

**À écrire.** Le chemin complet, toujours :

```json
"source": "./plugins/mon-plugin"
```

Ne pas déclarer `metadata.pluginRoot` : il n'apporte rien et laisse croire à un raccourci qui n'existe pas.

## 2. La clé `agents` exige des chemins de fichiers

**Observé.** Dans `.claude-plugin/plugin.json`, `"agents": "./agents/"` échoue :

```
✘ agents: Invalid input
```

Quatre formes testées :

| Valeur | Résultat |
|---|---|
| `"./agents/"` | rejet |
| `"./agents"` | rejet |
| `"./agents/mon-agent.md"` | accepté |
| `["./agents/mon-agent.md"]` | accepté |
| `"./nexistepas.md"` | rejet |

La clé attend un ou plusieurs chemins de fichiers `.md` **qui existent**. Les autres clés de composants — `skills`, `commands`, `workflows`, `outputStyles` — acceptent un dossier.

## 3. `claude plugin validate` n'a pas d'option `--strict`

**Observé.** `claude plugin validate --help` n'expose que `-h`. Une chaîne d'intégration continue qui appelle `--strict` échoue.

**À écrire.**

```bash
claude plugin validate <chemin-du-plugin>
claude plugin validate .                  # le marketplace
```

Vérifier l'aide de la version installée avant de câbler la validation.

## 4. `description` interdit les chevrons

**Observé.** Le validateur de skill rejette toute `description` contenant `<` ou `>`. Un gabarit écrit `Utiliser quand <la situation se présente>` produit une skill non publiable — le défaut se propage à chaque copie du gabarit.

**À écrire.** Des placeholders sans chevrons. Réserver `<...>` aux blocs de code et aux tableaux, jamais au champ `description`.

## 5. Six champs de frontmatter, pas un de plus

**Observé.** Le validateur livré avec `skill-creator` porte la liste close :

```python
ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}
```

Contraintes mesurées : `name` en kebab-case strict, 64 caractères, identique au nom du dossier. `description` 1024 caractères. `compatibility` 500 caractères. `name` et `description` sont les deux seuls requis.

**Le piège.** Claude Code tolère des clés hors spec ; la Skills API et claude.ai les rejettent. Un relevé de 373 `SKILL.md` installées en montre six en circulation : `user-invocable` (151), `argument-hint` (140), `version` (139), `homepage` (12), `tools` (2), `disable-model-invocation` (1). Une skill qui les porte fonctionne en local et échoue à la publication.

**À écrire.** `metadata` accepte des clés supplémentaires, mais chaque clé et chaque valeur doit être une chaîne.
Le [standard Agent Skills](https://agentskills.io/specification#metadata-field) exclut les listes et objets imbriqués.
Dans ce dépôt, écrire par exemple `tags: "redaction, edition, style"`.

## 6. Un seul `SKILL.md` par skill

**Observé.** Un `SKILL.md` imbriqué sous une skill est rejeté à l'envoi vers la Skills API, alors que le système de fichiers de Claude Code le charge sans rien dire. Le défaut n'apparaît qu'à la publication.

**À écrire.** Exactement un `SKILL.md`, à `skills/<nom>/SKILL.md`. Un document d'appui se nomme autrement : `references/<sujet>.md`.

## 7. Les manifestes n'acceptent pas de commentaires

**Observé.** `plugin.json` et `marketplace.json` sont lus comme du JSON strict. Un commentaire `//` fait échouer la validation.

**À écrire.** JSON strict dans les fichiers. L'annotation pédagogique va dans `docs/`, en JSONC, jamais dans le fichier réel.

## 8. Un marketplace privé fonctionne

**Observé.** Sur un dépôt privé de compte personnel :

```
claude plugin marketplace add <org>/<repo>
→ SSH not configured, cloning via HTTPS
→ ✔ Successfully added marketplace
```

Le clone utilise les identifiants du compte `gh` actif. Aucune configuration particulière.

**Conséquence.** Le compte `gh` actif décide de ce qui est visible. `gh auth switch` avant d'ajouter un marketplace privé appartenant à un autre compte.

## 9. Un plugin installé est une copie locale

**Observé.** Après installation, le plugin vit sous `~/.claude/plugins/cache/<marketplace>/<plugin>/` — une copie réelle de tous les fichiers, pas un lien vers le dépôt.

**Conséquence.** Les skills se chargent hors ligne et sans jeton valide. Seules `plugin install` et `marketplace update` demandent le réseau. Le marketplace est un canal de distribution, pas une dépendance d'exécution.

## 10. Le nom d'un plugin est immuable

Le champ `name` du manifeste sert de namespace d'invocation : `/<plugin-name>:<skill-name>`. Le changer casse toute installation existante.

**La seule sortie** est le champ `renames` du catalogue, qui déclare la correspondance :

```json
"renames": { "ancien-nom": "nouveau-nom", "nom-supprime": null }
```

Renommer avant la première publication coûte zéro. Après, il faut maintenir `renames` indéfiniment.

## 11. Le cache des plugins range par version

**Observé.** Après installation, l'arborescence est :

```
~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/
```

Les anciennes versions restent en place, marquées `.orphaned_at`. Tout chemin en dur vers
`cache/<marketplace>/<plugin>/skills/...` est faux, et un chemin incluant la version casse
au prochain bump.

**À écrire.** Ne jamais citer le cache dans une documentation. Référencer la copie de travail
du dépôt, ou laisser la skill résoudre ses propres fichiers : un composant de plugin dispose
de `${CLAUDE_PLUGIN_ROOT}`.

## 12. `plugin update` exige l'identifiant complet

**Observé.**

```
claude plugin update <plugin>                  → ✘ Plugin not found
claude plugin update <plugin>@<marketplace>    → ✔ updated from 0.2.0 to 0.3.0
```

Le nom seul suffit à `install` mais pas à `update`. Le message d'erreur laisse croire que le
plugin n'est pas installé.

**À écrire.** Toujours `<plugin>@<marketplace>`, dans les deux commandes.

## 13. `marketplace remove` laisse son cache

**Observé.** Après le renommage d'un marketplace, l'ancien nom a ete retire :

```
claude plugin marketplace remove <ancien-nom>
→ ✔ Successfully removed marketplace
```

La declaration disparait de `known_marketplaces.json`, et `~/.claude/plugins/cache/<ancien-nom>/` reste sur le disque — 736 Ko dans le cas mesure, deux copies de plugin marquees `.orphaned_at`.

Ce repertoire ne sera jamais reclame : plus aucun marketplace de ce nom n'existe pour le ramasser. Ce n'est pas un cache qui vieillit, c'est un orphelin definitif.

**Ce que fait Claude Code de son cote.** Le cache range par version et marque les versions superseded d'un fichier `.orphaned_at`, a cote d'un `.in_use` sur la version active. Une suppression differee est donc prevue pour les versions ; elle ne couvre pas un marketplace disparu.

**Ce qu'un nettoyeur generique n'y fait pas.** `mole` ne touche pas `~/.claude/plugins/cache/`. Sa liste detaillee ne contient que le cache de l'application de bureau. C'est protecteur : un balayage generique ne distinguerait pas le plugin vivant de l'orphelin.

**A faire.** Apres avoir renomme un marketplace, supprimer son ancien cache :

```bash
rm -rf ~/.claude/plugins/cache/<ancien-nom>
```

## 14. Deux plans d'installation coexistent, un seul laisse une trace

**Observé.** Un plugin installé depuis le Directory de claude.ai n'écrit rien sur le disque. Après suppression complète du plan local sur une machine :

```
known_marketplaces.json   {}
installed_plugins.json    plugins: {}
settings.json             enabledPlugins: {}
~/.claude/plugins/        20 Ko
```

125 skills continuent de répondre, servies par quatorze plugins dont `organisation`, `carriere`, `marketing` et `data`. Aucun de ces plugins n'apparaît dans `installed_plugins.json`, ni dans `plugin-catalog-cache.json`, ni dans `settings.json`.

**Conséquence.** L'état du plan compte ne se lit pas sur le disque. Une commande, un script d'inventaire ou un agent qui inspecte `~/.claude/plugins/` mesure le seul plan local et conclut à tort que rien n'est installé.

**À faire.** Pour savoir ce que le compte sert, lire la liste des skills exposées dans une session interactive. Un nom préfixé — `organisation:brainstorm` — vient d'un plugin. Un nom sans préfixe vient du répertoire local des skills.

**Prise en compte.** Le plan compte exige un redémarrage complet de l'application. Le plan local est immédiat.

## 15. `ListPlugins` ne voit pas les plugins servis par le compte

**Observé.** Sur une machine où quatorze plugins exposent 125 skills, l'outil `ListPlugins` renvoie une liste vide. `ListSkills`, en revanche, retourne les onze skills individuelles du compte : `docx`, `pdf`, `pptx`, `xlsx`, `mcp-builder`, `skill-creator`, `theme-factory`, `web-artifacts-builder`, `internal-comms`, `morning`, `import-memory`.

**Conséquence.** Aucun outil n'énumère les plugins d'un compte. Une réponse vide de `ListPlugins` n'établit pas qu'aucun plugin n'est installé.

**À faire.** Déduire les plugins des préfixes de skills, et le dire comme une déduction.

## 16. Codex supprime la racine du marketplace, Claude Code la laisse

**Observé.** Les deux CLI ne se comportent pas de la même façon au retrait d'un marketplace.

```
codex plugin marketplace remove <marketplace>
→ Removed installed marketplace root: ~/.codex/.tmp/marketplaces/<marketplace>

claude plugin marketplace remove <marketplace>
→ ✔ Successfully removed marketplace
   ~/.claude/plugins/cache/<marketplace>/  reste sur le disque
```

Sur un poste mesuré, six marketplaces retirés de Claude Code ont laissé 474 Mo de cache, dont 458 Mo pour un seul plugin.

**À faire.** Le piège n° 13 ne vaut que pour Claude Code. Après un `claude plugin marketplace remove`, supprimer `~/.claude/plugins/cache/` et `~/.claude/plugins/marketplaces/`. Après un `codex plugin marketplace remove`, ne rien faire de plus.

## 17. Codex accepte un catalogue au format Claude Code

**Observé.** Six dépôts sans catalogue Codex — `pbakaus/impeccable`, `anthropics/knowledge-work-plugins`, `anthropics/skills`, `anthropics/financial-services`, `better-auth/skills`, `mattpocock/skills` — sont acceptés par `codex plugin marketplace add`. Aucun ne contient de `.agents/plugins/marketplace.json` ; tous portent un `.claude-plugin/marketplace.json`.

`codex plugin add` réussit ensuite, et dépose les fichiers réels : `mattpocock-skills` arrive avec ses cinq skills, `marketing` avec ses huit.

**Ce qui n'est pas établi.** Que Codex charge ces skills en session. La commande réussit et les fichiers sont là ; le chargement effectif n'a pas été mesuré.

**À faire.** Ne pas conclure de la réussite d'une installation qu'un composant fonctionne. Pour un plugin destiné aux deux harnesses, écrire les deux manifestes.

## 18. Codex exige le préfixe `./` dans le chemin de source

**Observé.** Dans `.agents/plugins/marketplace.json`, un chemin de source écrit sans préfixe rend le marketplace entier invisible pour Codex.

| Valeur de `source.path` | `codex plugin list` |
|---|---|
| `"./plugins/mon-plugin"` | le marketplace et ses plugins apparaissent |
| `"plugins/mon-plugin"` | **le marketplace n'apparaît pas du tout** |

Aucun message d'erreur à l'ajout : `codex plugin marketplace add` réussit, `codex plugin marketplace list` montre bien le marketplace et sa racine, le clone contient tous les fichiers. Seul `codex plugin list` l'omet, et `codex plugin add` répond `plugin <nom> was not found in marketplace <nom>`.

**Le piège.** L'erreur ne désigne pas sa cause. Elle laisse croire à un problème de nom de plugin ou à un catalogue périmé, alors que la déclaration du chemin est seule en cause.

**À écrire.** Toujours le préfixe, dans les deux catalogues :

```json
"source": { "source": "local", "path": "./plugins/<nom>" }
```

Claude Code accepte les deux formes ; Codex n'en accepte qu'une.
