# Assessment 3.1 - Linked List
# Last Name: SUERTE

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, letter):
        new_node = Node(letter)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def remove_first(self):
        if self.head is not None:
            removed = self.head.data
            self.head = self.head.next
            return removed

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("Empty" if self.head is None else "None")


linked_list = LinkedList()

# Add letters
for letter in "SUERTE":
    linked_list.add(letter)

print("Linked List:")
linked_list.display()

# Remove letters
while linked_list.head is not None:
    removed = linked_list.remove_first()

    print("Removed:", removed)
    linked_list.display()

print("Linked List is now empty.")