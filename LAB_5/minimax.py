import math

def minimax(depth, node_index, is_max, values):
    if depth == 0:
        return values[node_index]
    
    if is_max:
        max_eval = float('-inf')
        for i in range(2):
            child_index = 2 * node_index + i
            if child_index < len(values):
                eval_score = minimax(depth - 1, child_index, False, values)
                max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            child_index = 2 * node_index + i
            if child_index < len(values):
                eval_score = minimax(depth - 1, child_index, True, values)
                min_eval = min(min_eval, eval_score)
        return min_eval


if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    
    tree_depth = int(math.log2(len(values)))
    
    optimal_value = minimax(tree_depth, 0, True, values)
    print(f"Optimal value: {optimal_value}")