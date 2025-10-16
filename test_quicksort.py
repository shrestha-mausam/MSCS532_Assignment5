#!/usr/bin/env python3
"""
Author: Mausam Shrestha
Date: 15th Oct, 2025
Simple test script for Quicksort implementations.
"""

import random
import time
import sys
from typing import List, Tuple, Callable

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
            # Partition the array
            pivot_index = self.partition(arr, low, high)
            
            # Recursively sort elements before and after partition
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


def test_sorting_correctness():
    print("Testing sorting correctness...")
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    analyzer = QuicksortAnalyzer()
    
    for i, test_case in enumerate(test_cases):
        if not test_case:
            continue
            
        det_result = test_case.copy()
        analyzer.quicksort_deterministic(det_result)
        
        rand_result = test_case.copy()
        analyzer.quicksort_randomized(rand_result)
        expected = sorted(test_case)
        
        if det_result == expected and rand_result == expected:
            print(f"✓ Test case {i+1} passed")
        else:
            print(f"✗ Test case {i+1} failed")
            print(f"  Input: {test_case}")
            print(f"  Expected: {expected}")
            print(f"  Deterministic: {det_result}")
            print(f"  Randomized: {rand_result}")


def simple_performance_test():
    print("\nRunning simple performance test...")
    
    sizes = [100, 500, 1000]
    analyzer = QuicksortAnalyzer()
    
    print(f"{'Size':<8} {'Det. Time':<12} {'Rand. Time':<12}")
    print("-" * 35)
    
    for size in sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        det_data = test_data.copy()
        analyzer.reset_counters()
        start_time = time.time()
        analyzer.quicksort_deterministic(det_data)
        det_time = time.time() - start_time
        
        rand_data = test_data.copy()
        analyzer.reset_counters()
        start_time = time.time()
        analyzer.quicksort_randomized(rand_data)
        rand_time = time.time() - start_time
        
        print(f"{size:<8} {det_time:<12.6f} {rand_time:<12.6f}")


def main():
    print("Quicksort Algorithm Test Suite")
    print("=" * 40)
    
    sys.setrecursionlimit(10000)
    
    test_sorting_correctness()
    simple_performance_test()
    
    print("\nTest completed successfully!")
    print("\nTo run the full analysis with detailed results:")
    print("1. Activate your virtual environment (if using one):")
    print("   source venv/bin/activate  # macOS/Linux")
    print("   venv\\Scripts\\activate     # Windows")
    print("2. Run the complete analysis:")
    print("   python quicksort.py")


if __name__ == "__main__":
    main()
