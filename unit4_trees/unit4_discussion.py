"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================
INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).
You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""

class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value          # The data stored in this node
        self.left = None            # Reference to left child (smaller values)
        self.right = None           # Reference to right child (larger values)


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None            # Root starts as None (empty tree)

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.
        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Start the recursive insertion from the root.
        # If the tree is empty, the first value becomes the root.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.
        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: we have found an empty spot → create a new node
        if node is None:
            return Node(value)

        # Insertion decision depends on comparison with current node:
        # - Smaller values always go left  → keeps the BST property
        # - Larger values always go right  → keeps the BST property
        # This ordering is what later allows efficient searching.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # If value == node.value we do nothing (ignore duplicates)

        return node   # Return the (possibly updated) subtree root

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.
        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is typically O(log n) on average because each
        # comparison discards roughly half of the remaining nodes
        # (the left or right subtree).  Linear search is always O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base cases
        if node is None:
            return False                # Reached a leaf → value not present
        if node.value == value:
            return True                 # Found the value

        # Decide which half of the tree to explore next
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.
        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # 1. Fully process the left subtree (all smaller values)
            self._inorder_recursive(node.left, values)

            # 2. Visit the current node
            values.append(node.value)

            # 3. Fully process the right subtree (all larger values)
            self._inorder_recursive(node.right, values)

            # Because every left child is smaller and every right child
            # is larger than its parent, the sequence left → node → right
            # always yields values in ascending sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    # and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.
    print("\n=== TREE CONSTRUCTION ===")

    # Create an empty Binary Search Tree
    tree = BST()

    # Insert values chosen so the tree is reasonably balanced.
    # Starting near the middle reduces the chance of a skewed tree.
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    print("Inserting the following values:", values_to_insert)

    for v in values_to_insert:
        tree.insert(v)
        # Each insertion walks down a single path, comparing the new
        # value with successive nodes.  At every step the search space
        # is halved (on average), which is why BST insertion/search
        # is efficient compared with a linear scan of an unsorted list.

    print("Tree constructed successfully.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    # sorted output in a BST.
    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_values = tree.inorder()
    print("In-order traversal result:", sorted_values)
    # The list is sorted because the in-order algorithm always
    # visits left subtree → node → right subtree, and the BST
    # property guarantees left < node < right.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.
    print("\n=== SEARCH TESTS ===")

    # Values that exist
    print("Search for 40 (exists):", tree.search(40))   # True
    print("Search for 70 (exists):", tree.search(70))   # True

    # Values that do not exist
    print("Search for 25 (missing):", tree.search(25))  # False
    print("Search for 100 (missing):", tree.search(100))# False

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.
    print("\n=== EDGE CASES ===")

    # 1. Empty tree
    empty_tree = BST()
    print("In-order of empty tree:", empty_tree.inorder())          # []
    print("Search in empty tree for 10:", empty_tree.search(10))    # False

    # 2. Single-node tree
    single = BST()
    single.insert(42)
    print("In-order of single-node tree:", single.inorder())        # [42]
    print("Search for 42 in single-node tree:", single.search(42))  # True
    print("Search for 99 in single-node tree:", single.search(99))  # False

    # 3. Duplicate insertion (ignored by our implementation)
    tree.insert(50)   # already present
    print("After attempting to insert duplicate 50, in-order is still:", tree.inorder())
    # The tree structure did not change because we deliberately skip equals.


if __name__ == "__main__":
    main()