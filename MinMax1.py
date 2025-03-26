import math

# Define the game tree as a dictionary
game_tree = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9'],
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}

# Minimax function
def minimax(node, is_max):
    if isinstance(game_tree[node], int):  # If leaf node, return its value
        return game_tree[node]
    
    children = game_tree[node]
    values = [minimax(child, not is_max) for child in children]
    
    return max(values) if is_max else min(values)

# Function to find the optimal path
def find_optimal_path(node, is_max):
    path = [node]

    while node in game_tree and not isinstance(game_tree[node], int):  # Stop at leaf node
        children = game_tree[node]

        if is_max:
            next_node = max(children, key=lambda c: minimax(c, False))
        else:
            next_node = min(children, key=lambda c: minimax(c, True))
        
        path.append(next_node)
        node = next_node
        is_max = not is_max  # Switch between MAX and MIN

    return path

# Compute optimal value and path
optimal_value = minimax('A', True)
optimal_path = find_optimal_path('A', True)

print("Optimal Value:", optimal_value)
print("Optimal Path:", " -> ".join(optimal_path))
