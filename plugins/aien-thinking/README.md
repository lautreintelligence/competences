# AIEN Thinking

Raisonner, expliquer, mettre en forme la pensée. Publié par L'Autre Intelligence & Nous dans le marketplace `competences`.

## Skills

| Skill | Invocation | Objet |
|---|---|---|
| `problem-framing` | `/aien-thinking:problem-framing` | Traite un problème complexe comme une anomalie de système : isole le signal, descend l'échelle causale, découpe les forces en MECE et fige la problématique. |
| `brainstorm` | `/aien-thinking:brainstorm` | Orchestre une table ronde à sept rôles cognitifs et sort des solutions classées sur applicabilité, effort et impact. |
| `doublecheck` | `/aien-thinking:doublecheck` | Produit une seconde réponse depuis des hypothèses opposées, puis synthétise les deux. Contre l'ancrage et le biais de confirmation. |
| `mece-checklist` | `/aien-thinking:mece-checklist` | Décompose un projet en checklist MECE : zéro doublon, zéro oubli, vérifié par framework. |
| `first-principles` | `/aien-thinking:first-principles` | Explique en partant d'un exemple concret et familier, puis remonte couche par couche jusqu'aux principes fondamentaux. |
| `sprezzatura` | `/aien-thinking:sprezzatura` | Explique en portant ensemble la méthode et les mécanismes, pour rendre capable de reproduire et d'adapter. |
| `unslop` | `/aien-thinking:unslop` | Détecte et corrige six catégories de marqueurs d'écriture IA, avec un garde-fou contre la surcorrection. |
| `session-digest` | `/aien-thinking:session-digest` | Distille une session de travail en note markdown datée : décisions prises, questions ouvertes, prochaines étapes. |

`first-principles` et `sprezzatura` expliquent toutes deux, mais en sens inverse : la première
remonte du concret vers l'abstrait, la seconde vise la complétude opérationnelle.

## Fichiers produits

`session-digest` écrit une note dans le répertoire indiqué par l'utilisateur ; à défaut, dans
`./notes/` à la racine du répertoire de travail.

## Composants

Plugin de skills seules. Aucun hook, serveur MCP, sous-agent ni exécutable déclaré au manifeste.
