# 📘 README – Résolution de Problème Multiobjectif

## 👤 Auteur

Nom : **Sogoba Emmanuel**
Projet : Résolution de problèmes multiobjectifs
Méthodes : Scalarisation, ε-contraintes, NSGA-II

---

## 🎯 Objectif du projet

Ce projet montre comment résoudre un **problème d’optimisation multiobjectif**, c’est-à-dire un problème où plusieurs objectifs doivent être optimisés en même temps.

👉 Exemple :

* Minimiser le coût
* Minimiser le temps

Ces objectifs sont souvent **en conflit**, donc on cherche un **compromis** appelé **solution de Pareto**.

---

## 📊 Problème étudié

Variable :

* x ∈ [0,10]

Fonctions objectifs :

* f1(x) = x²
* f2(x) = (x - 5)²

👉 Interprétation :

* f1 représente le coût
* f2 représente le temps

---

## ⚙️ Méthodes utilisées

### 🔵 1. Scalarisation

On transforme plusieurs objectifs en un seul :

f(x) = w1·f1(x) + w2·f2(x)

👉 Exemple :

* w1 = 0.5, w2 = 0.5
* Résultat : x = 2.5

✔️ Avantage :

* Simple à implémenter

❌ Inconvénient :

* Dépend du choix des poids

---

### 🟢 2. Méthode des ε-contraintes

On optimise un objectif et on limite l’autre :

Minimiser f1(x)
Sous contrainte : f2(x) ≤ ε

👉 Exemple :

* ε = 4 → x = 3
* ε = 1 → x = 4

✔️ Avantage :

* Donne plusieurs solutions

❌ Inconvénient :

* Nécessite plusieurs calculs

---

### 🔴 3. Algorithme NSGA-II

Méthode basée sur les **algorithmes génétiques**.

Étapes :

1. Générer une population initiale
2. Appliquer sélection, croisement, mutation
3. Trier les solutions (Pareto)
4. Garder les meilleures

👉 Résultat :

* Ensemble de solutions (front de Pareto)
* x ∈ [0,5]

✔️ Avantage :

* Trouve plusieurs solutions en une seule exécution

❌ Inconvénient :

* Plus complexe

---

## 📈 Résultats obtenus

| Méthode       | Résultat      |
| ------------- | ------------- |
| Scalarisation | x = 2.5       |
| ε-contraintes | x = 3, 4, ... |
| NSGA-II       | x ∈ [0,5]     |

---

## ⚖️ Conclusion

* **Scalarisation** : simple mais limitée
* **ε-contraintes** : plus précise
* **NSGA-II** : méthode la plus complète

👉 Pour les problèmes réels, **NSGA-II est recommandé**.

---

## 🚀 Améliorations possibles

* Ajouter un code Python (ex : bibliothèque DEAP)
* Visualiser le front de Pareto (graphique)
* Tester avec des données réelles

---

## 🧠 À retenir

✔️ Multiobjectif = plusieurs solutions
✔️ Pareto = meilleur compromis
✔️ NSGA-II = méthode moderne

---

## 📌 Utilisation

1. Lire le document
2. Comprendre les méthodes
3. Comparer les résultats
4. Adapter à d’autres problèmes

---

💡 Ce projet est idéal pour :

* étudiants en informatique
* optimisation
* data science

---
