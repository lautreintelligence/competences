# Exemples — Tissage vs séparation

Ces exemples illustrent la différence entre une explication « plate » (un seul type de compréhension) et une explication tissée (les deux intégrés).

---

## Exemple 1 : Négociation salariale

### ❌ Procédural seul (recette aveugle)
« Pour négocier ton salaire : 1) Fais des recherches sur le marché. 2) Annonce un chiffre 10-15% au-dessus de ta cible. 3) Ne parle jamais en premier du salaire. 4) Si on te propose moins, dis que tu dois réfléchir. 5) Fais une contre-offre. »

→ Le lecteur peut suivre les étapes, mais si le recruteur change de tactique, il est perdu. Il ne sait pas *pourquoi* annoncer au-dessus, ni quand cette stratégie ne marche plus.

### ❌ Causal seul (théorie flottante)
« La négociation salariale repose sur l'effet d'ancrage (Tversky & Kahneman, 1974) : le premier chiffre posé dans une négociation influence disproportionnellement le résultat final. La BATNA (Best Alternative To a Negotiated Agreement) détermine votre pouvoir de négociation réel. L'asymétrie d'information joue aussi un rôle clé. »

→ Le lecteur comprend les principes mais ne sait pas concrètement quoi dire, quand le dire, ni comment réagir aux situations courantes.

### ✅ Tissé (Sprezzatura)
« Commence par annoncer un chiffre 10-15% au-dessus de ce que tu vises — le premier nombre posé sur la table recadre toute la conversation, et l'autre partie va naturellement négocier à partir de là plutôt qu'à partir de son propre budget. C'est pour ça que tu ne veux jamais que le recruteur annonce en premier : son ancre deviendrait le point de départ. Si ça arrive quand même, ne réagis pas au chiffre — demande plutôt comment ils sont arrivés à ce montant. Ça déplace la discussion du nombre vers les critères, ce qui te redonne de la marge. Et si on te fait une offre basse, dis que tu as besoin de réfléchir. Pas par tactique : parce que sous pression, tu accepteras moins que ce que tu vaux, et le recruteur le sait. »

→ Chaque geste est accompagné de sa raison. Le lecteur peut reproduire ET adapter.

---

## Exemple 2 : Git rebase

### ❌ Procédural seul
« Pour faire un rebase : `git checkout feature-branch`, puis `git rebase main`. S'il y a des conflits, résous-les et fais `git rebase --continue`. »

### ❌ Causal seul
« Le rebase réécrit l'historique en rejouant les commits d'une branche sur une autre base. Contrairement au merge, il produit un historique linéaire. Attention : ne jamais rebaser une branche publique car cela modifie les hash SHA des commits. »

### ✅ Tissé
« Un rebase reprend tes commits un par un et les rejoue au-dessus de main — comme si tu les avais écrits aujourd'hui, sur le code le plus récent. Concrètement : `git checkout ta-branche` puis `git rebase main`. Si un de tes commits touche une ligne qui a changé depuis sur main, Git s'arrête et te demande de choisir — c'est un conflit. Résous-le dans le fichier, `git add`, puis `git rebase --continue` pour passer au commit suivant. Le piège : comme le rebase réécrit les identifiants de chaque commit, si quelqu'un d'autre travaille déjà sur cette branche, ses commits et les tiens ne correspondent plus. D'où la règle : on ne rebase que ce qui est resté local. »

---

## Patron de tissage

Ce qui rend ces exemples « tissés » plutôt que « séparés » :

1. **La raison est dans le même souffle que le geste.** Pas après, pas dans une note, pas dans un paragraphe séparé.
2. **Les connecteurs sont naturels** : « parce que », « c'est pour ça que », « le piège c'est que », « comme X fait Y ». Jamais « le mécanisme sous-jacent est » ou « d'un point de vue théorique ».
3. **Les conditions de validité arrivent au bon moment** — quand le lecteur en a besoin pour éviter une erreur, pas dans un disclaimer en bas de page.
4. **C'est plus court que les deux versions séparées combinées.** Le tissage compresse, il ne rallonge pas.
