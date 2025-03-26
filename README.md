# Minimax Search Algorithm - Optimal Path Finder

## Description
This project implements the **Minimax Search Algorithm** to determine the optimal path in a given game tree. The Minimax algorithm is widely used in artificial intelligence for two-player games like chess, tic-tac-toe, and other adversarial games. It helps in decision-making by minimizing possible losses while maximizing possible gains.

## Files
- **MinMax1.py**: Implements the Minimax search algorithm for the first game tree.
- **MinMax2.py**: Implements the Minimax search algorithm for the second game tree.

## Algorithm Description
### Minimax Algorithm
The **Minimax Algorithm** is a recursive decision-making strategy that operates on a tree representation of a game. It alternates between two players:
- **MAX Player**: Tries to maximize the score.
- **MIN Player**: Tries to minimize the score.

### Steps:
1. **Game Tree Representation**:
   - The game is represented as a tree with nodes.
   - The root node is the starting point.
   - The leaf nodes contain numerical values representing the utility of an outcome.
2. **Player Turns**:
   - MAX player aims to select the maximum possible value.
   - MIN player aims to select the minimum possible value.
   - Levels in the tree alternate between MAX and MIN nodes.
3. **Recursive Minimax Function**:
   - If the node is a leaf, return its value.
   - Otherwise, recursively compute values for child nodes.
   - If it's a MAX node, choose the highest value from children.
   - If it's a MIN node, choose the lowest value from children.
4. **Finding the Optimal Path**:
   - The algorithm traverses the tree, applying the Minimax rule.
   - The optimal path is determined by following the best choices at each level.

## Implementation
### MinMax1.py
```python
import math

game_tree = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9'],
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}

def minimax(node, is_max):
    if isinstance(game_tree[node], int):
        return game_tree[node]
    children = game_tree[node]
    values = [minimax(child, not is_max) for child in children]
    return max(values) if is_max else min(values)

def find_optimal_path(node, is_max):
    path = [node]
    while node in game_tree and not isinstance(game_tree[node], int):
        children = game_tree[node]
        next_node = max(children, key=lambda c: minimax(c, False)) if is_max else min(children, key=lambda c: minimax(c, True))
        path.append(next_node)
        node = next_node
        is_max = not is_max
    return path

optimal_value = minimax('A', True)
optimal_path = find_optimal_path('A', True)

print("Optimal Value:", optimal_value)
print("Optimal Path:", " -> ".join(optimal_path))
```

### MinMax2.py
```python
import math

game_tree = {
    'A': ['B1', 'B2'],
    'B1': ['C1', 'C2'],
    'B2': ['C3', 'C4'],
    'C1': ['D1', 'D2'],
    'C2': ['D3', 'D4'],
    'C3': ['D5', 'D6'],
    'C4': ['D7', 'D8'],
    'D1': ['E1', 'E2'],
    'D2': ['E3', 'E4'],
    'D3': ['E5', 'E6'],
    'D4': ['E7', 'E8'],
    'D5': ['E9', 'E10'],
    'D6': ['E11', 'E12'],
    'D7': ['E13', 'E14'],
    'D8': ['E15', 'E16'],
    'E1': 5, 'E2': -1, 'E3': 4, 'E4': 3,
    'E5': -2, 'E6': -5, 'E7': 9, 'E8': 8,
    'E9': 6, 'E10': 1, 'E11': -4, 'E12': 2,
    'E13': 4, 'E14': 7, 'E15': 3, 'E16': -3
}

def minimax(node, is_max):
    if isinstance(game_tree[node], int):
        return game_tree[node]
    children = game_tree[node]
    values = [minimax(child, not is_max) for child in children]
    return max(values) if is_max else min(values)

def find_optimal_path(node, is_max):
    path = [node]
    while node in game_tree and not isinstance(game_tree[node], int):
        children = game_tree[node]
        next_node = max(children, key=lambda c: minimax(c, False)) if is_max else min(children, key=lambda c: minimax(c, True))
        path.append(next_node)
        node = next_node
        is_max = not is_max
    return path

optimal_value = minimax('A', True)
optimal_path = find_optimal_path('A', True)

print("Optimal Value:", optimal_value)
print("Optimal Path:", " -> ".join(optimal_path))
```

## Output
For **MinMax1.py**, the output will display the optimal value and path based on the given tree structure.
For **MinMax2.py**, the output will be computed similarly based on its tree structure.

## Usage
1. Clone the repository.
2. Run `MinMax1.py` or `MinMax2.py` using Python.
   ```bash
   python MinMax1.py
   ```
   ```bash
   python MinMax2.py
   ```
3. View the computed **optimal value** and **optimal path** in the console.

## Code Repository
Click on: [Repository Link](https://github.com/Nagur-Meera/Minimax-Search-Algorithm)

---

This README provides a structured explanation of the project, algorithm, implementation, and usage details.

