# Assessment 3.1 - Array
# Last Name: SUERTE

letters = []

# Add letters
for letter in "SUERTE":
    letters.append(letter)

print("Array:", letters)

# Remove letters one by one
while letters:
    removed = letters.pop()

    print("Removed:", removed)
    print("Remaining:", letters)

print("Array is now empty.")