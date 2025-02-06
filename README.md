# Vortex Sort: A Hybrid Parallel Sorting Algorithm

## Project Overview

**Vortex Sort** is an innovative hybrid sorting algorithm that combines **bit-based grouping**, **dynamic algorithm selection**, and **parallel processing** to efficiently sort large datasets. It is designed to choose the best sorting strategy (insertion sort, quicksort, or heapsort) based on the size of the data, ensuring optimal performance across a wide range of inputs. This project demonstrates the implementation of Vortex Sort in Python, showcasing its unique approach to sorting.

---

## Features

- **Bit-Based Grouping**: Groups numbers based on their highest set bit for efficient partitioning.
- **Hybrid Sorting**: Dynamically selects the best sorting algorithm (insertion sort, quicksort, or heapsort) for each group.
- **Parallel Processing**: Sorts groups in parallel using Python's `ThreadPoolExecutor` for improved performance on large datasets.
- **Adaptive Thresholds**: Uses intelligent thresholds to switch between sorting algorithms and bypass parallel processing for small datasets.

---

## Project Structure

The project consists of the following key components:

- **`vortex_sort.py`**: The main Python script containing the Vortex Sort algorithm.
- **`README.md`**: This file, providing an overview and documentation for the project.
- **`LICENSE`**: The MIT License file, outlining the terms of use for this project.

---

## Goals

1. **Efficient Sorting**: Provide a fast and adaptive sorting algorithm for diverse datasets.
2. **Parallel Processing**: Leverage multi-core processors to improve performance on large datasets.
3. **Dynamic Algorithm Selection**: Use the most appropriate sorting algorithm based on the size of the data.
4. **Bit-Based Optimization**: Group numbers based on their highest set bit to improve partitioning efficiency.

---

## Prerequisites

To run this project, you will need:

- **Python 3.8 or above**
- **Git** (for cloning the repository)

---

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/vortex-sort.git
cd vortex-sort
```

### Step 2: Run the Algorithm
```python
from vortex_sort import vortex_sort

data = [15, 3, 10, 4, 12, 1, 7]
sorted_data = vortex_sort(data)
print("Sorted data:", sorted_data)
```

## How it Works

**1. Grouping:** Numbers are grouped based on their highest set bit.

**2. Sorting:** Each group is sorted using the most appropriate algorithm:
  - **Insertion:** Sort for small groups (≤16 elements).
  - **Quicksort:** for mid-sized groups (17–150 elements).
  - **Heapsort:** for large groups (>150 elements).

**3. Parallel Processing:** Groups are sorted in parallel using multi-threading.

**4. Combining:** The sorted groups are merged into a single sorted array.

## Performance Comparison

Below is a comparison of Vortex Sort with other popular sorting algorithms:

| Algorithm      | Time Complexity (Average) | Best Use Case          |
|----------------|---------------------------|------------------------|
| Vortex Sort    | O(n log n)                | Large, diverse datasets|
| Quicksort      | O(n log n)                | General-purpose        |
| Merge Sort     | O(n log n)                | Stable sorting         |
| Insertion Sort | O(n^2)                    | Small datasets         |

## Future Improvements

- **Optimize Grouping Strategy**: Experiment with different bit-range grouping strategies to improve performance.

- **Handle Edge Cases:** Extend the algorithm to handle negative numbers, floating-point numbers, strings and other edge cases.

- **Benchmarking:** Conduct extensive benchmarking on real-world datasets to validate performance.

- **Distributed Sorting:** Explore distributed computing techniques to handle even larger datasets.

##  License

This project is licensed under the MIT License.




