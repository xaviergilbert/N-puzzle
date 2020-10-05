# N-puzzle
42's school project

## Description
Le but de ce programme est de résoudre un jeu de taquin en utilisant le moins de coup possible et le plus rapidement possible.

On est donc dans une logique de résolution de problème en utilisant un algorithme de pqrcours de graphe sous contrainte de temps et d'espace.

L'algorithme implenté est l'algorithme A* mais l'utilisateur aura le choix d'utiliser Djikstra, des versions pondérés de A* pour accelerer sa recherche ou bien de passer par l'algorithme
du Greedy search pour avoir une réponse rapide sans tenir compte de l'optimum de coups.

Les heuristiques utilisées dans ce projets sont :

- Manhattan distance heuristic

- Misplaced tiles heuristic

- Euclidian distance heuristic

- Corner tiles heuristique

- Linear conflict

## Usage
source my_env/bin/activate pour activer l'espace de travail sur linux/mac

./python exec.py [-h] file / ./exec.py [-h] file
