# unit3_lists.py
# CMSC 315 – Unit 3 Discussion: Lists
# Demonstrates the use of a Python list (array-based dynamic array)
# Real-world scenario: Streaming service "Continue Watching" list

from typing import List, Optional


class ContinueWatchingList:
    """
    A simple ordered list that stores the titles a user is currently watching.
    Uses Python's built-in list (array-based implementation).
    """

    def __init__(self) -> None:
        # The underlying list that stores the titles in order
        self._titles: List[str] = []

    # ------------------------------------------------------------------
    # Core list operations
    # ------------------------------------------------------------------

    def add_title(self, title: str) -> None:
        """
        Append a new title to the end of the list (most recent).
        TODO: Implement append operation
        """
        if not title or not title.strip():
            print("Error: Title cannot be empty.")
            return
        self._titles.append(title.strip())
        print(f"Added: '{title.strip()}'")

    def insert_title(self, index: int, title: str) -> None:
        """
        Insert a title at a specific position.
        TODO: Implement insert operation with bounds checking
        """
        if not title or not title.strip():
            print("Error: Title cannot be empty.")
            return
        if index < 0 or index > len(self._titles):
            print(f"Error: Index {index} is out of range (0 to {len(self._titles)}).")
            return
        self._titles.insert(index, title.strip())
        print(f"Inserted '{title.strip()}' at position {index}")

    def remove_title(self, title: str) -> bool:
        """
        Remove the first occurrence of a title.
        TODO: Implement remove with edge-case handling
        """
        if not self._titles:
            print("Error: List is empty – nothing to remove.")
            return False
        try:
            self._titles.remove(title)
            print(f"Removed: '{title}'")
            return True
        except ValueError:
            print(f"Error: '{title}' not found in the list.")
            return False

    def remove_at(self, index: int) -> Optional[str]:
        """
        Remove and return the title at the given index.
        TODO: Implement pop / remove-by-index with bounds checking
        """
        if not self._titles:
            print("Error: List is empty – cannot remove.")
            return None
        if index < 0 or index >= len(self._titles):
            print(f"Error: Index {index} is out of range.")
            return None
        removed = self._titles.pop(index)
        print(f"Removed at index {index}: '{removed}'")
        return removed

    def search(self, title: str) -> int:
        """
        Return the index of the title, or -1 if not found.
        TODO: Implement linear search
        """
        try:
            return self._titles.index(title)
        except ValueError:
            return -1

    def display(self) -> None:
        """
        Print the current list in order.
        TODO: Implement display / traversal
        """
        if not self._titles:
            print("Continue Watching list is empty.")
            return
        print("\n--- Continue Watching ---")
        for i, title in enumerate(self._titles, start=1):
            print(f"{i}. {title}")
        print("-------------------------\n")

    def size(self) -> int:
        """Return the number of titles currently in the list."""
        return len(self._titles)

    def is_empty(self) -> bool:
        """Return True if the list contains no titles."""
        return len(self._titles) == 0


# ------------------------------------------------------------------
# Demonstration / Test Driver
# ------------------------------------------------------------------
def main() -> None:
    print("=== CMSC 315 Unit 3 – List Demonstration ===\n")

    watch_list = ContinueWatchingList()

    # 1. Adding titles (append)
    watch_list.add_title("Stranger Things S4")
    watch_list.add_title("The Mandalorian S3")
    watch_list.add_title("Wednesday")
    watch_list.add_title("The Last of Us")

    watch_list.display()

    # 2. Inserting in the middle
    watch_list.insert_title(1, "House of the Dragon")
    watch_list.display()

    # 3. Searching
    idx = watch_list.search("Wednesday")
    print(f"Search for 'Wednesday': found at index {idx}")
    idx = watch_list.search("Non-existent Show")
    print(f"Search for 'Non-existent Show': {idx} (not found)\n")

    # 4. Removing by value and by index
    watch_list.remove_title("The Mandalorian S3")
    watch_list.remove_at(0)          # remove first item
    watch_list.display()

    # 5. Edge-case testing
    print("--- Edge Case Tests ---")
    empty_list = ContinueWatchingList()
    empty_list.remove_title("Anything")          # empty remove
    empty_list.remove_at(0)                      # empty pop
    empty_list.insert_title(5, "Invalid")        # out-of-range insert
    empty_list.add_title("")                     # empty title
    empty_list.add_title("   ")                  # whitespace-only title

    # Single-item list becoming empty
    single = ContinueWatchingList()
    single.add_title("Only One Show")
    single.display()
    single.remove_at(0)
    single.display()

    print("All tests completed.")


if __name__ == "__main__":
    main()