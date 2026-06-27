# DANGER : no base case — runs forever (until Python raises RecursionError)
def infinite_sum(n):
    return n + infinite_sum(n - 1)   # Will never stop

# Safe version with base case
def sum_down(n):

    if n == 0:    # Base case
        return 0
    
    return n + sum_down(n - 1)   # Recursive case

print(sum_down(10))

# A function can also have multiple base cases:
def is_palindrome(s) -> bool:

    if len(s) <= 1:         # Base case 1 : empty string or single char
        return True
    
    if s[0] != s[-1]:       # Base case 2 : mismatch found
        return False
    
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar")) # True
print(is_palindrome("saippuakivikauppias"))
print(is_palindrome("Behnam"))  # False