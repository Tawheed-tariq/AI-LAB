import sys
def totalCost(mask, pos, n, cost):
  
    # Base case: if all cities are visited, return the
    # cost to return to the starting city (0)
    if mask == (1 << n) - 1:
        return cost[pos][0]

    ans = sys.maxsize   

    for i in range(n):
        if (mask & (1 << i)) == 0: 
  
            # If city i is not visited, visit it and 
             #  update the mask
            ans = min(ans, cost[pos][i] +
                      totalCost(mask | (1 << i), i, n, cost))

    return ans
 

def tsp(cost):
    n = len(cost)
    
    return totalCost(1, 0, n, cost)
 
if __name__ == "__main__":
    
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    result = tsp(cost)
    print(result)

    # Explanation of 1 << 10:
    # The expression 1 << 10 means shifting the binary representation of 1 to the left by 10 positions.
    # In binary, 1 is represented as 0000000001. After shifting left by 10 positions, it becomes:
    # 10000000000, which is equivalent to 2^10 or 1024 in decimal.


