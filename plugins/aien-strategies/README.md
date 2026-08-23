# AIEN Strategies

Préparation aux entretiens de conseil en stratégie, et évaluation d'idées de business.
Publié par L'Autre Intelligence & Nous dans le marketplace `competences`.

## Skills

| Skill | Invocation | Objet |
|---|---|---|
| `case-partner` | `/aien-strategies:case-partner` | Fait passer un entretien de cas complet façon McKinsey, BCG ou Bain, puis débriefe sur quatre dimensions. |
| `case-generator` | `/aien-strategies:case-generator` | Conçoit des cas d'entretien aux chiffres vérifiés par exécution Python et alimente la banque de cas. |
| `case-auditor` | `/aien-strategies:case-auditor` | Contrôle à froid la banque de cas : recalcul des chiffres, fuites de twist, conformité au gabarit. |
| `pei-interviewer` | `/aien-strategies:pei-interviewer` | Conduit le Personal Experience Interview : construit une banque de stories depuis le CV, puis creuse une dimension par session. |
| `minto` | `/aien-strategies:minto` | Évalue une vraie idée de business en candidate-led case et rend une recommandation GO / NO-GO en pyramide de Minto. |

Les trois skills `case-*` travaillent ensemble : `case-generator` produit, `case-partner` joue,
`case-auditor` vérifie. `minto` et `pei-interviewer` s'utilisent seules.

## Fichiers produits

Ces skills persistent leur état dans le répertoire de travail de l'utilisateur, jamais dans
le plugin :

| Fichier | Écrit par | Contenu |
|---|---|---|
| `cases/index.md` | `case-generator` | Index de la banque de cas |
| `case-progress.json` | `case-partner` | Progression et cas déjà joués |
| `pei-stories.json` | `pei-interviewer` | Banque de stories personnelles |

## Composants

Plugin de skills seules. Aucun hook, serveur MCP, sous-agent ni exécutable déclaré au manifeste.
