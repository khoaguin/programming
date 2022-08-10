# Input: The first line of the input contains the number n of items 
# and the capacity W of a knapsack. The next n lines define the values 
# and weights of the items. The i-th line contains integers v_i and w_i — the
# value and the weight of i-th item, respectively.
# Output: the maximal value of fractions of items that fit into the knapsack. 
# The absolute value of the difference between the answer of your program and 
# the optimal value should be at most 1e−3. To ensure this, output your answer 
# with at least four digits after the decimal point (otherwise your answer, 
# while being computed correctly, can turn out to be wrong because of rounding issues).


def most_expensive_index(weights, values) -> int:
    """
    Get the index of the most expensive item
    """
    max_index = 0
    max_cost = -1
    for i in range(len(weights)):
        cost: float = values[i] / weights[i]
        if cost > max_cost:
            max_cost = cost
            max_index = i

    return max_index


def get_optimal_value(capacity, weights, values):
    """
    Strategy: Get the most expensive item first
    """
    # base case
    if capacity == 0 or len(weights) == 0:
        return 0
    # recursive case
    m = most_expensive_index(weights, values)
    amount_taken = min(capacity, weights[m])
    value: float = float(amount_taken * float(values[m] / weights[m]))
    # remove the taken item 
    capacity = capacity - amount_taken
    del weights[m]
    del values[m]

    return value + get_optimal_value(capacity, weights, values)   


if __name__ == "__main__":
    # get user input
    data = list(map(int, input().split()))
    n, capacity = data
    values = []
    weights = []
    for i in range(n):
        v, w = list(map(int, input().split()))
        values.append(v)
        weights.append(w)
    # get the optimal 
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
