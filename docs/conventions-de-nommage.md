---
type: "Policy"
title: "Conventions de nommage"
description: "Regles de nommage des marketplaces, des plugins et des skills publies par L'Autre Intelligence & Nous : marketplace nomme competences, plugins prefixes aien-, kebab-case anglais, et procedure de renommage."
status: "stable"
tags: ["packaging", "agent-ia", "identite-visuelle"]
created: 2026-08-21
---

# Conventions de nommage

Le nom d'un plugin est son namespace d'invocation et il est immuable après publication. Ces règles se fixent avant la première mise en ligne, pas après.

## Le marketplace porte le nom de l'organisation

```
name: competences
```

Pas le nom du dépôt. Le dépôt peut être renommé sans conséquence ; le marketplace, non — son nom apparaît dans l'identifiant d'installation `<plugin>@competences` que les utilisateurs ont tapé.

## Les plugins portent le préfixe de l'organisation

```
aien-<domaine>
```

| Plugin | Installation | Invocation d'une skill |
|---|---|---|
| `aien-communication-pro` | `/plugin install aien-communication-pro@competences` | `/aien-communication-pro:fitz` |

Le préfixe fait deux choses. Il rend l'origine lisible dans une liste de plugins venus de sources multiples, et il écarte toute collision avec un plugin tiers portant un nom générique.

## Forme des noms

Kebab-case strict : minuscules, chiffres, traits d'union. Ni tiret initial ou final, ni tiret double. Soixante-quatre caractères au maximum.

L'anglais pour les identifiants — marketplace, plugin, skill. Le français reste dans la prose : `description`, `displayName`, documentation.

Le nom d'une skill est identique au nom de son dossier. Le validateur le contrôle.

## Noms réservés

Les préfixes `claude-` et `anthropic-` sont réservés. Un marketplace qui les porte est refusé.

## Ce que le nom ne porte pas

Ni la version, portée par le champ `version`. Ni le domaine fonctionnel au-delà d'un mot. Ni la mention du harness visé : un plugin sert Claude Code et Codex depuis le même dossier.

## Cloisonnement

Ce dépôt ne mentionne aucune autre organisation : ni dans les manifestes, ni dans les gabarits, ni dans les fichiers de licence. Le copyright de chaque `LICENSE` nomme L'Autre Intelligence & Nous.

Un gabarit repris d'un autre dépôt porte ses métadonnées d'origine — auteur, copyright, URL de dépôt. Les remplacer fait partie de la reprise, avant tout commit.

## Changer un nom

Avant la première publication, un renommage ne coûte rien.

Après, le catalogue doit déclarer la correspondance et la conserver :

```json
"renames": {
  "ancien-nom": "nouveau-nom",
  "nom-supprime": null
}
```

Une installation existante suit le renommage. Sans cette déclaration, elle casse sans message utile.

Renommer un marketplace laisse en plus son cache sur chaque machine. `claude plugin marketplace remove` retire la déclaration et laisse les fichiers : supprimer `~/.claude/plugins/cache/<ancien-nom>/` fait partie de l'opération.
