import sys
import traceback

def show_depth():
    """Returns the current call-stack depth"""
    
    frame = sys._getframe()
    depth = 0

    while frame:
        depth += 1
        frame = frame.f_back
    return depth

def factorial(n):
    print(f"  entering factorial({n}), stack depth = {show_depth()}")

    if n == 0:
        return 1
    
    result = n * factorial(n - 1)
    print(f"  leaving factorial({n}), returning {result}")
    # traceback.print_stack()
    return result


factorial(4)

# ---------------------------------
#  Visualizing the Call Stack
#----------------------------------

# Here is what the call stack looks like while computing factorial(4), just before hitting the base case:

#  ┌─────────────────────────────────────────┐
#  │  factorial(0)  — returns 1              │  ← top (most recent call)
#  ├─────────────────────────────────────────┤
#  │  factorial(1)  — suspended, n=1         │
#  ├─────────────────────────────────────────┤
#  │  factorial(2)  — suspended, n=2         │
#  ├─────────────────────────────────────────┤
#  │  factorial(3)  — suspended, n=3         │
#  ├─────────────────────────────────────────┤
#  │  factorial(4)  — suspended, n=4         │  ← bottom (original call)
#  └─────────────────────────────────────────┘

# Once factorial(0) returns 1, each suspended frame resumes in reverse order, multiplying its n with the return value from below.

# You can also use traceback.print_stack() to print the live call stack at any point during a recursive execution.