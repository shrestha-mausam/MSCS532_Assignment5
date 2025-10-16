"""
Quicksort Implementation
Assignment 5: MSCS 532
Author: Mausam Shrestha
Date: 15th Oct, 2025
"""

import random
import time
import sys
from typing import List, Tuple, Callable
import matplotlib.pyplot as plt
import numpy as np


class QuicksortAnalyzer:
    
    def __init__(self):
        self.comparison_count = 0
        self.swap_count = 0
    
    def reset_counters(self):
        self.comparison_count = 0
        self.swap_count = 0
    
    def partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            self.comparison_count += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swap_count += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swap_count += 1
        
        return i + 1
    
    def quicksort_deterministic(self, arr: List[int], low: int = 0, high: int = None) -> List[int]:
        if high is None:
            high = len(arr) - 1
        
        if low < high:
            pivot_index = self.partition(arr, low, high)
            self.quicksort_deterministic(arr, low, pivot_index - 1)
            self.quicksort_deterministic(arr, pivot_index + 1, high)
        
        return arr
    
    def randomized_partition(self, arr: List[int], low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        self.swap_count += 1
        return self.partition(arr, low, high)
    
    def quicksort_randomized(self, arr: List[int], low: int = 0, high: int = None) -> List[int]:
        if high is None:
            high = len(arr) - 1
        
        if low < high:
            # Use randomized partition
            pivot_index = self.randomized_partition(arr, low, high)
            
            # Recursively sort elements before and after partition
            self.quicksort_randomized(arr, low, pivot_index - 1)
            self.quicksort_randomized(arr, pivot_index + 1, high)
        
        return arr


def generate_test_data(size: int, data_type: str = 'random') -> List[int]:
    """
    Generate test data of different types for empirical analysis.
    
    Args:
        size: Size of the array to generate
        data_type: Type of data ('random', 'sorted', 'reverse_sorted', 'nearly_sorted')
        
    Returns:
        A list of integers for testing
    """
    if data_type == 'random':
        return [random.randint(1, 1000) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(1, size + 1))
    elif data_type == 'reverse_sorted':
        return list(range(size, 0, -1))
    elif data_type == 'nearly_sorted':
        arr = list(range(1, size + 1))
        # Randomly swap 5% of elements
        num_swaps = max(1, size // 20)
        for _ in range(num_swaps):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    else:
        raise ValueError("Invalid data_type. Use 'random', 'sorted', 'reverse_sorted', or 'nearly_sorted'")


def measure_performance(analyzer: QuicksortAnalyzer, sort_func: Callable, arr: List[int], iterations: int = 5) -> Tuple[float, int, int]:
    times = []
    total_comparisons = 0
    total_swaps = 0
    
    for _ in range(iterations):
        test_arr = arr.copy()
        analyzer.reset_counters()
        
        start_time = time.time()
        sort_func(test_arr)
        end_time = time.time()
        
        times.append(end_time - start_time)
        total_comparisons += analyzer.comparison_count
        total_swaps += analyzer.swap_count
    
    avg_time = sum(times) / len(times)
    avg_comparisons = total_comparisons // iterations
    avg_swaps = total_swaps // iterations
    
    return avg_time, avg_comparisons, avg_swaps


def empirical_analysis():
    print("=" * 80)
    print("EMPIRICAL ANALYSIS: DETERMINISTIC vs RANDOMIZED QUICKSORT")
    print("=" * 80)
    
    sizes = [100, 500, 1000, 2000, 5000]
    data_types = ['random', 'sorted', 'reverse_sorted', 'nearly_sorted']
    
    for data_type in data_types:
        print(f"\n{data_type.upper().replace('_', ' ')} DATA:")
        print("-" * 50)
        print(f"{'Size':<8} {'Det. Time':<12} {'Rand. Time':<12} {'Det. Comp':<10} {'Rand. Comp':<10}")
        print("-" * 50)
        
        for size in sizes:
            test_data = generate_test_data(size, data_type)
            
            det_analyzer = QuicksortAnalyzer()
            det_time, det_comp, det_swaps = measure_performance(
                det_analyzer, det_analyzer.quicksort_deterministic, test_data
            )
            
            rand_analyzer = QuicksortAnalyzer()
            rand_time, rand_comp, rand_swaps = measure_performance(
                rand_analyzer, rand_analyzer.quicksort_randomized, test_data
            )
            
            print(f"{size:<8} {det_time:<12.6f} {rand_time:<12.6f} {det_comp:<10} {rand_comp:<10}")


def theoretical_analysis():
    print("\n" + "=" * 80)
    print("THEORETICAL ANALYSIS OF QUICKSORT")
    print("=" * 80)
    
    analysis = """
TIME COMPLEXITY ANALYSIS:

1. BEST CASE: O(n log n)
   - Occurs when the pivot always divides the array into two equal halves
   - Recurrence relation: T(n) = 2T(n/2) + O(n)
   - Using Master Theorem: T(n) = O(n log n)
   - Example: Array where pivot is always the median

2. AVERAGE CASE: O(n log n)
   - Expected case with random data
   - Each pivot has equal probability of being selected
   - Expected number of comparisons: n log n
   - Mathematical proof involves solving the recurrence:
     T(n) = (1/n) * Σ[T(i-1) + T(n-i)] + O(n) for i=1 to n
     This simplifies to T(n) = O(n log n)

3. WORST CASE: O(n²)
   - Occurs when pivot is always the smallest or largest element
   - Recurrence relation: T(n) = T(n-1) + O(n)
   - Solution: T(n) = O(n²)
   - Example: Already sorted array with last element as pivot (deterministic)
   - Example: Already sorted array in reverse order with last element as pivot

SPACE COMPLEXITY:
- Best/Average case: O(log n) - height of recursion tree
- Worst case: O(n) - skewed recursion tree
- In-place partitioning: O(1) additional space
- Total space: O(log n) to O(n) depending on pivot selection

RANDOMIZATION BENEFITS:
- Eliminates worst-case scenarios for any specific input pattern
- Reduces probability of worst-case from 1 to 1/n! for random inputs
- Provides expected O(n log n) performance regardless of input
- Makes algorithm robust against adversarial inputs
    """
    
    print(analysis)


def demonstrate_algorithms():
    print("\n" + "=" * 80)
    print("QUICKSORT ALGORITHM DEMONSTRATION")
    print("=" * 80)
    
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    
    analyzer = QuicksortAnalyzer()
    det_array = test_array.copy()
    analyzer.reset_counters()
    
    print(f"\nDeterministic Quicksort:")
    print(f"Before sorting: {det_array}")
    analyzer.quicksort_deterministic(det_array)
    print(f"After sorting:  {det_array}")
    print(f"Comparisons: {analyzer.comparison_count}, Swaps: {analyzer.swap_count}")
    
    analyzer.reset_counters()
    rand_array = test_array.copy()
    
    print(f"\nRandomized Quicksort:")
    print(f"Before sorting: {rand_array}")
    analyzer.quicksort_randomized(rand_array)
    print(f"After sorting:  {rand_array}")
    print(f"Comparisons: {analyzer.comparison_count}, Swaps: {analyzer.swap_count}")


def main():
    sys.setrecursionlimit(10000)
    
    print("QUICKSORT ALGORITHM: IMPLEMENTATION, ANALYSIS, AND RANDOMIZATION")
    print("Assignment 5 - MSCS 532")
    print("=" * 80)
    
    demonstrate_algorithms()
    theoretical_analysis()
    empirical_analysis()
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
