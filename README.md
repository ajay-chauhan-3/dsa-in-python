# Data Structures and Algorithms in Python

A structured collection of Data Structures and Algorithms problem solutions implemented in Python. The repository is organized by core algorithmic paradigms and underlying problem-solving patterns rather than random problem IDs.

## Repository Structure

Each main directory represents an algorithmic paradigm or data structure, divided into specific pattern-based subdirectories. Eg:

```text
dsa-in-python/
├── divide_and_conquer/
│   ├── core/
│   └── sorting/
├── dynamic_programming/
│   ├── core/
│   ├── 1d_dp/
│   └── 2d_dp/
├── graphs/
│   ├── core/
│   └── dijkstra/
└── .gitignore
```

## Solution Format

Every solution file is self-contained and follows a consistent documentation standard at the top of the file:
- **Problem Link:** Direct reference to the problem statement (LeetCode / GFG / etc.).
- **Complexity Analysis:** Explicit time and space complexity breakdown, including auxiliary data structures and recursion stack overhead.
- **Core Concept:** Main concept and logical thinking used to solve the problem.

## Running the Code

- All solutions are written in standard Python 3 without external dependencies.
- If any external dependency is required, it is explicitly noted in the respective `.py` file along with the reason.

`To run any solution locally:`

```bash
python divide_and_conquer/sorting/reverse_pairs.py
```