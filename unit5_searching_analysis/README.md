`# Unit 5 Discussion: Search Algorithms
`
## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implemented linear search
- Implemented binary search
- Compared performance
- Analyzed algorithm efficiency

## Requirements

1. Both algorithms were tested on a small sorted dataset. A list of eight integers was created and searched for values that exist and values that do not exist. Both linear and binary search returned the correct index when the target was present and returned -1 when the target was absent.
2. Both algorithms were tested on a large sorted dataset. A list of 5,000 even numbers was created and searched for existing and missing values. The results confirmed correctness while illustrating that binary search becomes significantly more efficient as the dataset size increases.
3. Edge cases were demonstrated. The program handled an empty list, a single-element list, a target at the first position, and a target at the last position. Both algorithms produced the expected results in every case.
4. Performance was analyzed. Linear search examines elements sequentially and therefore has O(n) time complexity. Binary search repeatedly halves the search space and therefore has O(log n) time complexity. The advantage of binary search grows as the collection becomes larger.
5. A real-world search scenario was created. Linear search remains the better choice when data is unsorted or changes frequently. Binary search is preferred for large, static, sorted collections such as a dictionary or a sorted music library.


## Discussion Board Reflection

I implemented classic iterative linear search and iterative binary search. The program creates a small sorted list and a large sorted list so the performance difference is visible. Both algorithms are exercised on existing values, missing values, and several edge cases. Binary search is faster because each comparison discards half of the remaining elements, giving O(log n) time versus the O(n) of linear search. Linear search is the better choice when the data is unsorted or changes frequently. Real-world examples are searching for a contact in a small, unsorted phone contact list or looking for a specific item in a short shopping list. Binary search requires the collection to be sorted. It is unusable on unsorted data.