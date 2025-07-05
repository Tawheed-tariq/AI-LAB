import math

def expectimax(depth, node_index, is_max, values):
    if depth == 0:
        return values[node_index]
    
    if is_max:
        max_eval = float('-inf')
        for i in range(2):
            child_index = 2 * node_index + i
            if child_index < len(values):
                eval_score = expectimax(depth - 1, child_index, False, values)
                max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        total = 0
        count = 0
        for i in range(2):
            child_index = 2 * node_index + i
            if child_index < len(values):
                eval_score = expectimax(depth - 1, child_index, True, values)
                total += eval_score
                count += 1
        return total / count if count > 0 else 0


if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    
    tree_depth = int(math.log2(len(values)))
    
    optimal_value = expectimax(tree_depth, 0, True, values)
    print(f"Expected value: {optimal_value}")