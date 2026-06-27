# Example 1 ---- Generating all permutations
def permutations(lst):
    """Generate all ordering of lst. Makes len(lst) recursive calls"""

    if len(lst) <= 1:
        return [lst[:]]     # base case: only one ordering
    
    result = []

    for i in range(len(lst)):
        # pick element i as the first, permute the rest

        first = lst[i]
        rest = lst[:i] + lst[i+1:]

        for perm in permutations(rest):   # recursive call for each choice
            result.append([first] + perm)

    return result

print(permutations([1, 2, 3]))

# Example 2 ---- Power set(all subsets)
def power_set(lst):
    """Generates 2^n subsets"""

    if not lst:
        return [[]]   # base case : only the empty set
    
    first = lst[0]
    rest = power_set(lst[1:])      # recursive call
    with_first = [[first] + s for s in rest]
    without_first = rest
    return with_first + without_first

print(power_set([1, 2, 3]))



# Multiple recursion can be expensive — permutations of n elements requires O(n!) calls.