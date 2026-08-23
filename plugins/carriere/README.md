# Carrière

Préparer les entretiens de conseil en stratégie et construire sa banque de cas. Publié par L'Autre Intelligence & Nous dans le marketplace `competences`.

## Skills

| Skill | Invocation | Objet |
|---|---|---|
| `case-partner` | `/carriere:case-partner` | Fait passer un entretien de cas complet façon McKinsey, BCG ou Bain, puis débriefe sur quatre dimensions. |
| `case-generator` | `/carriere:case-generator` | Conçoit des cas d'entretien aux chiffres vérifiés par exécution Python et alimente la banque de cas. |
| `case-auditor` | `/carriere:case-auditor` | Contrôle à froid la banque de cas : recalcul des chiffres, fuites de twist, conformité au gabarit. |
| `pei-interviewer` | `/carriere:pei-interviewer` | Conduit le Personal Experience Interview : construit une banque de stories depuis le CV, puis creuse une dimension par session. |

Les trois skills `case-*` travaillent ensemble : `case-generator` produit, `case-partner` joue, `case-auditor` vérifie.

Ces skills persistent leur état dans le répertoire de travail de l'utilisateur, jamais dans le plugin : `cases/index.md` pour l'index de la banque, `case-progress.json` pour la progression, `pei-stories.json` pour les stories personnelles.

## Composants

Plugin de skills seules. Aucun hook, serveur MCP, sous-agent ni exécutable déclaré au manifeste.
