# Example 1 ---- Factorial
def factorial(n):

    if n == 0:
        return 1
    
    return n * factorial(n - 1)  # exactly one recursive call


# Example 2 ----- Summing a list
def sum_list(lst):
    if not lst:        # base case : empty list
        return 0
    
    return lst[0] + sum_list(lst[1:])   # one recursive call

print(sum_list([3, 7, 1, 9]))


# Example 3 ----- Reversing a string
def reverse(s):
    if len(s) <= 1:
        return s
    
    return reverse(s[1:]) + s[0]

# Linear recursion generally has O(n) time and O(n) space (one frame per call).