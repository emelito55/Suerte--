# Assessment 3.1 - Stack
# Last Name: SUERTE

stack = []

# Push letters
for letter in "SUERTE":
    stack.append(letter)

print("Stack:", stack)

# Pop letters
while stack:
    removed = stack.pop()

    print("Popped:", removed)
    print("Remaining:", stack)

print("Stack is now empty.")