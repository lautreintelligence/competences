# Organisation

Structurer un problème, décomposer un projet, distiller une session de travail. Publié par L'Autre Intelligence & Nous dans le marketplace `competences`.

## Skills

| Skill | Invocation | Objet |
|---|---|---|
| `problem-framing` | `/organisation:problem-framing` | Traite un problème complexe comme une anomalie de système : isole le signal, descend l'échelle causale, découpe les forces en MECE et fige la problématique. |
| `mece-checklist` | `/organisation:mece-checklist` | Décompose un projet en checklist MECE : zéro doublon, zéro oubli, vérifié par framework. |
| `brainstorm` | `/organisation:brainstorm` | Orchestre une table ronde à sept rôles cognitifs et sort des solutions classées sur applicabilité, effort et impact. |
| `session-digest` | `/organisation:session-digest` | Distille une session de travail en note markdown datée : décisions prises, questions ouvertes, prochaines étapes. |

`session-digest` écrit une note dans le répertoire indiqué par l'utilisateur ; à défaut, dans `./notes/` à la racine du répertoire de travail.

## Composants

Plugin de skills seules. Aucun hook, serveur MCP, sous-agent ni exécutable déclaré au manifeste.
