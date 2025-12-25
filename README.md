# Visual Scripting Prototype

## 1. Problème résolu

La programmation traditionnelle repose sur du code textuel, ce qui peut constituer une barrière
pour les designers, artistes ou débutants.  
Ce projet propose un **prototype de visual scripting**, inspiré de systèmes comme *Blueprints*,
permettant de créer une logique simple à l’aide de **nœuds graphiques connectables**.

Objectif : faciliter la compréhension et la construction de logiques sans écrire de code.

---

## 2. Architecture technique

Le projet est développé en **C++17** avec **SDL3 + ImGui**.

### Architecture générale

- `App`  
  - Point central de l’application
  - Gère le cycle de vie, la boucle principale et les événements

- `GUI`  
  - Interface utilisateur ImGui
  - Création, affichage et manipulation des nœuds
  - Connexion visuelle entre les pins

- `Core`
  - `Node` : définition d’un nœud (opération, condition, événement)
  - `Pin` : entrées/sorties des nœuds
  - `Graph` : graphe de nœuds connectés
  - `Executor` : exécution de la logique du graphe

- `Utils`
  - Fonctions utilitaires (logs, math, helpers)

---

## 3. Compilation et exécution

### Prérequis
- Python 3
- clang++
- SDL3
- ImGui

### Build
```bash
python build.py

