# Assessment 3.1 - Queue
# Last Name: SUERTE

from collections import deque

queue = deque()

# Add letters
for letter in "SUERTE":
    queue.append(letter)

print("Queue:", list(queue))

# Remove letters
while queue:
    removed = queue.popleft()

    print("Dequeued:", removed)
    print("Remaining:", list(queue))

print("Queue is now empty.")