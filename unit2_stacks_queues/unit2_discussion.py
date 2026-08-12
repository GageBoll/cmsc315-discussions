"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================
OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []  # Using a list; the end of the list is the top of the stack

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)  # Appends to the end so the newest item is always on top (LIFO)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            print("Error: Cannot pop from an empty stack.")
            return None
        return self.items.pop()  # Removes and returns the last item added (top of stack)

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            print("Error: Cannot peek at an empty stack.")
            return None
        return self.items[-1]  # Returns the top item without removing it

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()  # Using deque for O(1) enqueue and dequeue

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)  # Adds to the right end so the oldest item stays at the left (FIFO)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            print("Error: Cannot dequeue from an empty queue.")
            return None
        return self.items.popleft()  # Removes from the left (front) – the oldest item

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            print("Error: Cannot view front of an empty queue.")
            return None
        return self.items[0]  # Returns the oldest item (front) without removing it

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")
    stack = Stack()

    print("Pushing four pages onto the browser history stack...")
    stack.push("home.html")
    stack.push("products.html")
    stack.push("cart.html")
    stack.push("checkout.html")
    print("Current top of stack (most recent page):", stack.peek())

    print("\nDemonstrating LIFO behavior (Back button):")
    print("Popped:", stack.pop())   # checkout.html
    print("Popped:", stack.pop())   # cart.html
    print("Popped:", stack.pop())   # products.html
    print("Popped:", stack.pop())   # home.html

    print("\n--- Edge Cases ---")
    print("Trying to pop from an empty stack:")
    stack.pop()

    print("Trying to peek at an empty stack:")
    stack.peek()

    print("\nCreating a single-item stack and removing it...")
    stack.push("single_page.html")
    print("Top:", stack.peek())
    stack.pop()
    print("Is stack empty after removing the only item?", stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")
    queue = Queue()

    print("Adding four print jobs to the queue...")
    queue.enqueue("Document_A.pdf")
    queue.enqueue("Photo_B.jpg")
    queue.enqueue("Report_C.docx")
    queue.enqueue("Invoice_D.xlsx")
    print("Front of queue (next to print):", queue.front())

    print("\nDemonstrating FIFO behavior (print jobs processed in arrival order):")
    print("Dequeued:", queue.dequeue())  # Document_A.pdf
    print("Dequeued:", queue.dequeue())  # Photo_B.jpg
    print("Dequeued:", queue.dequeue())  # Report_C.docx
    print("Dequeued:", queue.dequeue())  # Invoice_D.xlsx

    print("\n--- Edge Cases ---")
    print("Trying to dequeue from an empty queue:")
    queue.dequeue()

    print("Trying to view front of an empty queue:")
    queue.front()

    print("\nCreating a single-item queue and removing it...")
    queue.enqueue("Last_Job.pdf")
    print("Front:", queue.front())
    queue.dequeue()
    print("Is queue empty after removing the only item?", queue.is_empty())


if __name__ == "__main__":
    main()