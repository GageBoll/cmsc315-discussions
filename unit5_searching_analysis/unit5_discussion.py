"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================
INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

def linear_search(lst, target):
    """
    Implement a linear search algorithm.
    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search examines every element one-by-one until the target
    # is found or the end of the list is reached.
    # In the worst case we look at all n elements → O(n) time complexity.
    for i in range(len(lst)):
        if lst[i] == target:
            return i          # target found – return its index
    return -1                 # target not present


def binary_search(lst, target):
    """
    Implement a binary search algorithm.
    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Binary search only works on a sorted list.
    # Each iteration discards half of the remaining elements,
    # so the search space shrinks exponentially → O(log n) time.
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2          # middle index of current range

        if lst[mid] == target:
            return mid                   # target found
        elif lst[mid] < target:
            low = mid + 1                # discard left half (all values ≤ mid)
        else:
            high = mid - 1               # discard right half (all values ≥ mid)

    return -1                            # target not present


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================
    # A small sorted list lets us clearly see both algorithms
    # working and verify correct results by hand.
    print("\n=== SMALL DATASET TEST ===")
    small_data = [3, 8, 12, 17, 25, 31, 42, 56]
    print(f"Dataset: {small_data}")

    # Search for a value that exists
    target_found = 25
    lin_idx = linear_search(small_data, target_found)
    bin_idx = binary_search(small_data, target_found)
    print(f"Looking for {target_found}:")
    print(f"  Linear search index: {lin_idx}")
    print(f"  Binary search index: {bin_idx}")
    # Both return the same correct index (4).

    # Search for a value that does not exist
    target_missing = 20
    lin_idx = linear_search(small_data, target_missing)
    bin_idx = binary_search(small_data, target_missing)
    print(f"Looking for {target_missing}:")
    print(f"  Linear search index: {lin_idx}")
    print(f"  Binary search index: {bin_idx}")
    # Both correctly return -1.


    # ===============================
    # LARGE DATASET
    # ===============================
    # With a much larger sorted list the difference in efficiency
    # becomes obvious: linear search may examine thousands of
    # elements while binary search examines only ~13-14.
    print("\n=== LARGE DATASET TEST ===")
    large_data = list(range(0, 10000, 2))   # 5000 even numbers, already sorted
    print(f"Large dataset size: {len(large_data)} elements")

    target_large = 8764                     # exists in the list
    lin_idx = linear_search(large_data, target_large)
    bin_idx = binary_search(large_data, target_large)
    print(f"Looking for {target_large}:")
    print(f"  Linear search index: {lin_idx}")
    print(f"  Binary search index: {bin_idx}")

    target_large_missing = 8765             # odd number – not present
    lin_idx = linear_search(large_data, target_large_missing)
    bin_idx = binary_search(large_data, target_large_missing)
    print(f"Looking for {target_large_missing}:")
    print(f"  Linear search index: {lin_idx}")
    print(f"  Binary search index: {bin_idx}")

    # Why binary search becomes more efficient as datasets grow:
    # Linear search always checks up to n elements (O(n)).
    # Binary search halves the remaining space each step (O(log n)).
    # For n = 5000, log₂(5000) ≈ 12–13 comparisons vs. up to 5000.


    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # 1. Empty list
    empty = []
    print("Empty list:")
    print(f"  Linear search for 5 → {linear_search(empty, 5)}")
    print(f"  Binary search for 5 → {binary_search(empty, 5)}")
    # Both correctly return -1 because there are no elements to examine.

    # 2. Single-element list – target present
    single = [42]
    print("Single-element list (target present):")
    print(f"  Linear search for 42 → {linear_search(single, 42)}")
    print(f"  Binary search for 42 → {binary_search(single, 42)}")

    # 3. Single-element list – target absent
    print("Single-element list (target absent):")
    print(f"  Linear search for 7 → {linear_search(single, 7)}")
    print(f"  Binary search for 7 → {binary_search(single, 7)}")

    # 4. Target at the first position
    first = [10, 20, 30, 40, 50]
    print("Target at first position:")
    print(f"  Linear search for 10 → {linear_search(first, 10)}")
    print(f"  Binary search for 10 → {binary_search(first, 10)}")

    # 5. Target at the last position
    print("Target at last position:")
    print(f"  Linear search for 50 → {linear_search(first, 50)}")
    print(f"  Binary search for 50 → {binary_search(first, 50)}")


if __name__ == "__main__":
    main()