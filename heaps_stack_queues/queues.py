from collections import deque

queue = deque()

# Enqueue elements
queue.append('Alice')
queue.append('Bob')
queue.append('Charlie')
print(f"Queue after enqueues: {queue}")  # deque(['Alice', 'Bob', 'Charlie'])

# Dequeue elements
first_person = queue.popleft()
print(f"Dequeued: {first_person}")       # 'Alice'
print(f"Queue after dequeue: {queue}")   # deque(['Bob', 'Charlie'])