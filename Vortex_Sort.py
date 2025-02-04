from concurrent.futures import ThreadPoolExecutor
import heapq

# Helper function to find the highest set bit in a number
def highest_set_bit(x):
    """
    Returns the position of the highest set bit in a number.
    For example, highest_set_bit(12) returns 3 because 12 is 1100 in binary.
    """
    if x == 0:
        return 0
    return x.bit_length() - 1

# Insertion sort for small datasets
def insertion_sort(arr):
    """
    Sorts a small array using insertion sort.
    Insertion sort is efficient for very small datasets due to its low overhead.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Quicksort for mid-sized datasets
def quicksort(arr):
    """
    Sorts an array using quicksort.
    Quicksort is efficient for mid-sized datasets due to its O(n log n) average-case complexity.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose a pivot element
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    return quicksort(left) + middle + quicksort(right)  # Recursively sort and combine

# Heapsort for large datasets
def heapsort(arr):
    """
    Sorts an array using heapsort.
    Heapsort is efficient for large datasets due to its consistent O(n log n) performance.
    """
    heapq.heapify(arr)  # Convert the array into a heap
    return [heapq.heappop(arr) for _ in range(len(arr))]  # Extract elements in sorted order

# Function to sort a group of numbers using the appropriate algorithm
def sort_group(numbers):
    """
    Sorts a group of numbers using the most appropriate algorithm based on its size.
    - For very small groups (≤16 elements), use insertion sort.
    - For mid-sized groups (17–150 elements), use quicksort.
    - For large groups (> 150 elements), use heapsort.
    """
    size = len(numbers)
    if size <= 16:
        return insertion_sort(numbers)
    elif size <= 150:
        return quicksort(numbers)
    else:
        return heapsort(numbers)

# Vortex Sort: Main sorting function
def vortex_sort(arr):
    """
    Sorts an array using the Vortex Sort algorithm.
    - For small datasets (≤ 1000 elements), bypass parallel processing and sort directly.
    - For larger datasets, group numbers by their highest set bit, sort each group in parallel,
      and then combine the sorted groups.
    """
    # Bypass parallel processing for small datasets
    if len(arr) <= 1000:
        return sort_group(arr)
    
    # Step 1: Group numbers based on their highest set bit
    groups = {}
    for num in arr:
        bit_pos = highest_set_bit(num)
        bit_range = bit_pos // 2  # Group numbers into ranges of 2 bit positions
        if bit_range not in groups:
            groups[bit_range] = []
        groups[bit_range].append(num)
    
    sorted_groups = {}
    
    # Step 2: Sort each group in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        # Submit sorting tasks for each group
        future_to_group = {executor.submit(sort_group, v): k for k, v in groups.items()}
        # Collect the sorted results
        for future in future_to_group:
            sorted_groups[future_to_group[future]] = future.result()
    
    # Step 3: Flatten the sorted groups into a single sorted array
    sorted_arr = []
    for key in sorted(sorted_groups.keys()):  # Maintain order of bit ranges
        sorted_arr.extend(sorted_groups[key])
    
    return sorted_arr

# Example usage
data = [15, 3, 10, 4, 12, 1, 7]
print("Original data:", data)
print("Sorted data:", vortex_sort(data))