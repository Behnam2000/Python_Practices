# Initialize an empty stack
stack = []

# Push elements onto the stack
stack.append('B')
stack.append('C')
stack.append('E')
print(f"stack after pushes: {stack}")

# Pop elements off the stack
top_element = stack.pop()
print(f"popped: {top_element}")
print(f"stack after pop: {stack}")

# Peek the top element without removing it
print(f"top element: {stack[-1]}")