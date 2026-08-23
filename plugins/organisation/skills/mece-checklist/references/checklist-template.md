# Template de Checklist MECE

Charger ce fichier en Phase 2 (Structuration) pour formater la sortie.

## Format Standard

```markdown
# CHECKLIST MECE : [TITRE DU PROJET]

## METADONNEES
- **Objectif** : [Une phrase precise]
- **Echeance** : [Date]
- **Complexite** : [Simple/Moderee/Elevee]
- **Framework MECE utilise** : [Temporel/Acteur/Domaine/Mixte]

## CRITERES DE SUCCES (Mesurables)
1. [Critere quantifiable]
2. [Critere verifiable]
3. [Critere observable]

## VUE D'ENSEMBLE MECE
[PROJET]
├── [CATEGORIE 1] (X% effort)
├── [CATEGORIE 2] (Y% effort)
├── [CATEGORIE 3] (Z% effort)
└── [CATEGORIE 4] (W% effort)
= 100% (Collectivement Exhaustif)

## EXECUTION DETAILLEE

### [CATEGORIE 1] : [Nom explicite]
**Objectif** : [Ce que cette categorie doit accomplir]
**Prerequis** : [Ce qui doit etre fait avant]

#### Sous-categorie 1.1 : [Nom]
- [ ] [Action detaillee] (methode : [comment], validation : [critere], duree : [estimation])
- [ ] [Action detaillee] (depend de : [reference], outils : [lesquels])

**Points critiques** :
- [Piege frequent et comment l'eviter]
- [Dependance externe a surveiller]

#### Sous-categorie 1.2 : [Nom]
[...]

### [CATEGORIE 2] : [Nom]
[Structure identique]

## CHECKLIST DE VALIDATION FINALE

**Test MECE - Exclusivite Mutuelle :**
- [ ] Aucune tache n'apparait dans plusieurs categories
- [ ] Les categories ne se chevauchent pas
- [ ] Les responsabilites sont clairement delimitees

**Test MECE - Exhaustivite Collective :**
- [ ] Simulation complete effectuee sans identifier de manques
- [ ] Tous les livrables ont leurs taches associees
- [ ] Tous les risques ont leurs mitigations

## AMELIORATION CONTINUE
- **Lecons apprises** : [Zone pour capturer les retours]
- **Optimisations identifiees** : [Pour la prochaine fois]
```

## Regles de Formatage

### Niveaux de hierarchie
- **Niveau 1** : 3-7 categories max (les grandes sections MECE)
- **Niveau 2** : Sous-categories MECE dans chaque L1
- **Niveau 3** : Actions detaillees, 5-9 max par section

### Detail d'une action
Chaque action finale repond a : QUOI + COMMENT + CRITERE DE VALIDATION
- Bon : "Configurer DNS du domaine via Cloudflare (4 enregistrements A, 2 MX, 1 TXT SPF)"
- Mauvais : "S'occuper du DNS"

### Verbes interdits
Ne jamais utiliser : "Gerer", "S'occuper de", "Voir pour", "Faire le necessaire"
Utiliser des verbes precis : configurer, rediger, valider, deployer, tester, creer, migrer...
