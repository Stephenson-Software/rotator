# Challenge: Rotate a list by k elements
Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 

Try solving this without creating a copy of the list. How many swap or move operations do you need?

## Solution
`Rotator` in `rotator.py` rotates a list to the left, in place, without creating a copy of it.

- `rotate(inputList)` shifts every element one position to the left and moves the original first element to the end. The caller's list is mutated and nothing is returned.
- `rotateRepeat(inputList, numRotations)` calls `rotate` on the list `numRotations` times.

### Move count
`rotate` saves the first element, shifts the remaining `n - 1` elements one position to the left, and then writes the saved element into the last position — `n` moves for a list of `n` elements. `rotateRepeat` repeats that, so rotating by `k` costs `n * k` moves.

## Running the demo
```
python3 main.py
```

`main.py` rotates `[1, 2, 3, 4, 5, 6]` once and prints the list before and after:

```
Num rotations: 1

Before:
[1, 2, 3, 4, 5, 6]

After:
[2, 3, 4, 5, 6, 1]
```

## Running the tests
The tests are written for pytest and must be run from the repository root, since `test_rotator.py` and `test_main.py` import `rotator` and `main` as top-level modules and the repository has no packaging or `conftest.py` to place them on the import path.

```
python3 -m pytest
```
