def factorial(n):
    # --- recursive case progression for n=4 ---
    # factorial(4) → 4 * factorial(3)
    # factorial(3) → 3 * factorial(2)
    # factorial(2) → 2 * factorial(1)
    # factorial(1) → 1 * factorial(0)
    # factorial(0) → 1  ← base case reached

    if n == 0:
        return 1
    return n * factorial(n - 1)

# The key invariant: every step reduces n by 1, so the base case n == 0 is guaranteed to be hit.
