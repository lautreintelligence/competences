---
type: "Policy"
title: "Conventions de nommage"
description: "Regles de nommage du marketplace competences, de ses plugins et de ses skills : marketplace nomme d'apres son contenu, plugins nommes d'apres les enjeux de competences du ROME, kebab-case strict, et procedure de renommage."
status: "stable"
tags: ["packaging", "agent-ia", "identite-visuelle"]
created: 2026-08-21
---

# Conventions de nommage

Le nom d'un plugin est son namespace d'invocation et il est immuable après publication. Ces règles se fixent avant la première mise en ligne, pas après.

## Le marketplace porte ce qu'il contient

```
name: competences
```

Pas le nom du dépôt. Le dépôt peut être renommé sans conséquence ; le marketplace, non — son nom apparaît dans l'identifiant d'installation `<plugin>@competences` que les utilisateurs ont tapé, et aucun mécanisme de redirection ne couvre son renommage.

Le nom de l'association ne figure pas dans les identifiants techniques. Il vit dans l'URL du dépôt, dans le champ `owner` du catalogue, dans le copyright de la licence, dans le fichier `NOTICE` et dans le champ `author` de chaque manifeste. Un identifiant doit être compris avant d'être signé.

## Les plugins portent un enjeu de compétences du ROME

Le ROME — Répertoire Opérationnel des Métiers et des Emplois de France Travail — range 19 462 compétences en 6 domaines et 32 enjeux. Chaque plugin porte le nom d'un enjeu, en un mot.

| Plugin | Enjeu ROME | Invocation d'une skill |
|---|---|---|
| `communication` | Communication, Multimédia | `/communication:email-diplomatique` |
| `organisation` | Organisation | `/organisation:checklist-sans-oubli` |
| `transmission` | Conseil, Transmission | `/transmission:sprezzatura` |
| `strategie` | Stratégie de développement | `/strategie:minto` |
| `carriere` | Développement des compétences | `/carriere:case-partner` |
| `technologie` | Data et Nouvelles technologies | `/technologie:clean-code-audit` |

Ce découpage donne à un professionnel le vocabulaire de son propre parcours plutôt qu'un classement technique.

**Aucun préfixe.** Le suffixe `@competences` qualifie déjà l'origine ; la répéter dans chaque nom coûte des caractères et n'écarte aucune collision.

## Forme des noms

Kebab-case strict : minuscules, chiffres, traits d'union. Ni tiret initial ou final, ni tiret double. Soixante-quatre caractères au maximum.

Un nom de plugin s'écrit sans accent, même quand le mot en porte : `strategie`, `carriere`. Le libellé accentué va dans `displayName`.

Le nom d'une skill est identique au nom de son dossier. Le validateur le contrôle.

## Noms réservés

Les préfixes `claude-` et `anthropic-` sont réservés. Un marketplace qui les porte est refusé.

## Ce que le nom ne porte pas

Ni la version, portée par le champ `version`. Ni le nom de l'éditeur. Ni la mention du harness visé : un plugin sert Claude Code et Codex depuis le même dossier.

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

Ce mécanisme ne couvre que les plugins. Renommer le marketplace lui-même casse toute installation existante, sans recours.
