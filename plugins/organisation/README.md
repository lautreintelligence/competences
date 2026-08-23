# Organisation

Structurer un problème, décomposer un projet, distiller une session de travail. Publié par L'Autre Intelligence & Nous dans le marketplace `competences`.

## Skills

| Skill | Invocation | Objet |
|---|---|---|
| `cadrage-de-probleme` | `/organisation:cadrage-de-probleme` | Traite un problème complexe comme une anomalie de système : isole le signal, descend l'échelle causale, découpe les forces en MECE et fige la problématique. |
| `checklist-sans-oubli` | `/organisation:checklist-sans-oubli` | Décompose un projet en checklist MECE : zéro doublon, zéro oubli, vérifié par framework. |
| `brainstorm` | `/organisation:brainstorm` | Orchestre une table ronde à sept rôles cognitifs et sort des solutions classées sur applicabilité, effort et impact. |
| `synthese-de-conversation` | `/organisation:synthese-de-conversation` | Distille une session de travail en note markdown datée : décisions prises, questions ouvertes, prochaines étapes. |

`synthese-de-conversation` écrit une note dans le répertoire indiqué par l'utilisateur ; à défaut, dans `./notes/` à la racine du répertoire de travail.

## Composants

Plugin de skills seules. Aucun hook, serveur MCP, sous-agent ni exécutable déclaré au manifeste.
