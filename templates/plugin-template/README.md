# Plugin Template

Gabarit de depart pour un plugin servant Claude Code et Codex.

## Utilisation

1. Copier le dossier sous `plugins/<plugin-name>/`.
2. Remplacer `plugin-template` par le nom du plugin dans les deux manifestes.
   Ce nom est immuable une fois le plugin publie.
3. Supprimer tout composant non utilise, et retirer la cle correspondante des manifestes.
4. Ajouter une entree dans les deux catalogues, a la racine du repo.
5. Valider : `claude plugin validate plugins/<plugin-name>`.

## Composants

| Chemin | Harness | Obligatoire |
|---|---|---|
| `.claude-plugin/plugin.json` | Claude Code | oui, pour Claude Code |
| `.codex-plugin/plugin.json` | Codex | oui, pour Codex |
| `skills/` | les deux | non — seul repertoire portable |
| `.mcp.json` | les deux | non |
| `commands/` | les deux | non |
| `hooks/hooks.json` | Claude Code | non |
| `hooks.json` | Codex | non |
| `agents/<n>.md` | Claude Code | non |
| `agents/openai.yaml` | Codex | non |
| `workflows/` `output-styles/` `themes/` `monitors/` `.lsp.json` `settings.json` `bin/` | Claude Code | non |
| `.app.json` `ui/` `assets/` | Codex | non |

Un plugin qui ne contient que `skills/` fonctionne sur les deux harnesses sans adaptation.

## Reference

Specification complete et annotee :
[docs/gabarit-de-repo-marketplace-multi-harness.md](../../docs/gabarit-de-repo-marketplace-multi-harness.md)
