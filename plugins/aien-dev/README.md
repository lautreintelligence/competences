# AIEN Dev

Audit de code et spécification d'interface. Publié par L'Autre Intelligence & Nous dans le marketplace `competences`.

## Skills

| Skill | Invocation | Objet |
|---|---|---|
| `clean-code-audit` | `/aien-dev:clean-code-audit` | Audite du code contre les six principes du Clean Code — nommage, fonctions, commentaires, formatage, gestion d'erreur, DRY — avec score pondéré et exemples de refactoring. |
| `ui-to-spec` | `/aien-dev:ui-to-spec` | Transforme une interface, URL ou capture d'écran, en spécification technique reproductible selon un framework à six dimensions. |

## Prérequis

`ui-to-spec` appelle le binaire `playwright-cli` pour son mode de navigation autonome. Sans lui,
seul le mode capture d'écran fonctionne — l'utilisateur fournit alors l'image.

## Composants

Plugin de skills seules. Aucun hook, serveur MCP, sous-agent ni exécutable déclaré au manifeste.
