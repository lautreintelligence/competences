---
name: synthese-de-conversation
description: >
  Distille une conversation longue (brainstorm, session de travail, exploration) en une note
  propre avec conclusions et next steps. Sauvegarde la note dans le répertoire indiqué par
  l'utilisateur, sinon ./notes/ à la racine du répertoire de travail. Utilise ce skill quand
  l'utilisateur dit « /synthese-de-conversation », « tldr », « fais le point », « résume la
  session », « distille la conversation ».
license: Apache-2.0
metadata:
  version: "0.1.1"
  author: "L'Autre Intelligence & Nous"
  tags: "synthese, notes, conversation"
---

# Synthèse de conversation

Relire l'integralite de la conversation en cours, en extraire l'essentiel, et sauvegarder une note markdown propre dans le repertoire de notes de l'utilisateur.

## Processus

1. Scanner toute la conversation — identifier les sujets abordes, les decisions prises, les questions restees ouvertes, les idees generees.
2. Structurer la note selon le format ci-dessous.
3. Generer un nom de fichier : `YYYY-MM-DD-synthese-<sujet-court>.md` (ex: `2026-04-22-synthese-pricing-strategy.md`).
4. Sauvegarder dans le repertoire indique par l'utilisateur. A defaut, `./notes/` a la racine du repertoire de travail — creer le dossier s'il n'existe pas.
5. Afficher un resume court a l'utilisateur avec le chemin du fichier cree.

## Format de la note

```markdown
# Synthèse — <Sujet>

Date : YYYY-MM-DD
Projet : <nom du projet si identifiable>

## Contexte

<1-3 phrases. De quoi on a parle et pourquoi.>

## Conclusions

<Liste a puces. Les decisions prises, les constats importants, les choses tranchees.>

## Next steps

<Liste a puces. Actions concretes a faire, par qui si identifiable. Chaque item commence par un verbe a l'infinitif.>

## Questions ouvertes

<Liste a puces. Ce qui n'a pas ete tranche, ce qui merite d'y revenir. Omettre cette section si rien n'est en suspens.>
```

## Regles

- Ton factuel, pas de reformulation decorative. Droit au contenu.
- La note doit etre comprehensible dans 3 mois sans le contexte de la conversation.
- Ne pas inclure les tatonnements, les fausses pistes abandonnees, ou les echanges de coordination. Seulement ce qui a survecu.
- Si la conversation portait sur du code : inclure les fichiers modifies et les choix techniques dans les conclusions.
- Si l'utilisateur a fourni des arguments en appelant /synthese-de-conversation, les traiter comme indication du sujet ou du perimetre a distiller.
- Pas de frontmatter YAML, pas de tags, pas de wikilinks. Markdown pur.
