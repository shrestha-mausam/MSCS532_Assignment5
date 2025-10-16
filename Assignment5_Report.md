# Assignment 5: Quicksort Implementation and Analysis

**Course:** MSCS-532
**Author:** Mausam Shrestha 
**Date:** 15th Oct, 2025

## Overview

This project explores the Quicksort algorithm through two different approaches - deterministic and randomized versions. I implemented both algorithms and tested them across various scenarios to understand how pivot selection affects performance. The results show clear differences between the two approaches, especially when dealing with sorted data.

## 1. Implementation Details

### 1.1 Deterministic Quicksort

I started with the basic Quicksort that always picks the last element as the pivot. This is the most straightforward version:

- Uses the last element as pivot every time
- Implements Lomuto partitioning 
- Recursively sorts both halves

```python
def quicksort_deterministic(self, arr: List[int], low: int = 0, high: int = None) -> List[int]:
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = self.partition(arr, low, high)
        self.quicksort_deterministic(arr, low, pivot_index - 1)
        self.quicksort_deterministic(arr, pivot_index + 1, high)
    
    return arr
```

### 1.2 Randomized Version

For the randomized approach, I changed how the pivot gets selected. Instead of always using the last element, it picks a random position:

```python
def randomized_partition(self, arr: List[int], low: int, high: int) -> int:
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return self.partition(arr, low, high)
```

### 1.3 Partitioning Logic

Both versions use the same partitioning method. The code moves smaller elements to the left and larger ones to the right of the pivot:

```python
def partition(self, arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

## 2. Theoretical Analysis

### 2.1 Time Complexity

**Best Case: O(n log n)**
When the pivot splits the array perfectly in half every time, we get the ideal scenario. The recurrence relation becomes T(n) = 2T(n/2) + O(n), which gives us O(n log n) using the Master Theorem.

**Average Case: O(n log n)**
With random data, the algorithm typically performs well. Each element has an equal chance of being the pivot, so we expect around n log n comparisons on average.

**Worst Case: O(n²)**
This happens when the pivot is always the smallest or largest element. The recurrence becomes T(n) = T(n-1) + O(n), leading to O(n²) performance. This occurs with sorted arrays when using the last element as pivot.

### 2.2 Space Complexity

The space complexity varies based on how balanced the recursion tree is:
- Best/average case: O(log n) due to balanced recursion
- Worst case: O(n) when recursion tree is heavily skewed
- Partitioning itself only needs O(1) extra space since it works in-place

### 2.3 Why Randomization Helps

Using random pivots prevents worst-case scenarios from happening consistently. Instead of always picking the last element (which can be problematic with sorted data), randomization spreads the risk across all possible pivot choices. This means:
- No single input pattern can guarantee terrible performance
- We get expected O(n log n) performance regardless of input type
- The algorithm becomes more robust against tricky inputs

## 3. Empirical Analysis Results

### 3.1 Testing Method

I ran both algorithms on different types of data to see how they perform:
- Array sizes: 100, 500, 1000, 2000, 5000 elements
- Data types: random numbers, sorted arrays, reverse sorted, and nearly sorted
- Measured execution time and comparison counts
- Each test ran 5 times and I averaged the results

### 3.2 Test Results

#### Random Data
| Size | Det. Time (s) | Rand. Time (s) | Det. Comparisons | Rand. Comparisons |
|------|---------------|----------------|------------------|-------------------|
| 100  | 0.000052      | 0.000065       | 725              | 623               |
| 500  | 0.000357      | 0.000480       | 4,936            | 4,867             |
| 1000 | 0.000852      | 0.001062       | 12,508           | 11,547            |
| 2000 | 0.001887      | 0.002205       | 25,332           | 24,306            |
| 5000 | 0.005468      | 0.006621       | 73,317           | 72,184            |

Both algorithms performed about the same on random data. The differences are minor and likely due to the random nature of pivot selection.

#### Sorted Data (Where Standard Quicksort Struggles)
| Size | Det. Time (s) | Rand. Time (s) | Det. Comparisons | Rand. Comparisons |
|------|---------------|----------------|------------------|-------------------|
| 100  | 0.000328      | 0.000060       | 4,950            | 659               |
| 500  | 0.008298      | 0.000418       | 124,750          | 4,773             |
| 1000 | 0.034872      | 0.000935       | 499,500          | 10,870            |
| 2000 | 0.142796      | 0.002056       | 1,999,000        | 24,649            |
| 5000 | 0.915230      | 0.005645       | 12,497,500       | 72,194            |

Here's where things get interesting. The standard version really struggles with sorted data, taking much longer and doing way more comparisons. The randomized version keeps its cool and maintains good performance.

#### Reverse Sorted Data
| Size | Det. Time (s) | Rand. Time (s) | Det. Comparisons | Rand. Comparisons |
|------|---------------|----------------|------------------|-------------------|
| 100  | 0.000294      | 0.000069       | 4,950            | 648               |
| 500  | 0.006454      | 0.000455       | 124,750          | 4,864             |
| 1000 | 0.026408      | 0.000925       | 499,500          | 10,756            |
| 2000 | 0.105698      | 0.002052       | 1,999,000        | 24,590            |
| 5000 | 0.668029      | 0.005795       | 12,497,500       | 70,910            |

Same story here - reverse sorted data also causes problems for the standard version.

#### Nearly Sorted Data
| Size | Det. Time (s) | Rand. Time (s) | Det. Comparisons | Rand. Comparisons |
|------|---------------|----------------|------------------|-------------------|
| 100  | 0.000226      | 0.000070       | 3,550            | 636               |
| 500  | 0.001650      | 0.000418       | 29,416           | 4,795             |
| 1000 | 0.002753      | 0.001012       | 49,239           | 11,348            |
| 2000 | 0.004167      | 0.002153       | 77,212           | 24,232            |
| 5000 | 0.023063      | 0.005714       | 362,176          | 70,490            |

Even with nearly sorted data, the standard version doesn't do as well as the randomized one.

### 3.3 Key Observations

The testing revealed some clear patterns:
- Random data: both algorithms work fine
- Sorted data: standard version struggles badly, randomized version stays fast
- The performance gap gets worse as arrays get bigger
- Randomization really does help avoid worst-case scenarios

## 4. Real-World Impact

### 4.1 Where This Matters

Understanding these differences is important for:

- **Databases**: Sorting query results efficiently
- **Web applications**: Processing user data quickly  
- **Mobile apps**: Handling limited processing power
- **Big data tools**: Sorting massive datasets
- **Embedded systems**: Working with constrained resources

### 4.2 Choosing the Right Approach

**Standard Quicksort** works well when:
- You know your data is random
- Worst-case performance isn't a big concern
- You want the simplest implementation

**Randomized Quicksort** is better when:
- You're not sure what kind of data you'll get
- Consistent performance matters
- You need to avoid worst-case scenarios
- Someone might try to give you tricky inputs

### 4.3 Performance Optimization Strategies

There are other ways to improve Quicksort:
- Switch to Insertion Sort for small arrays
- Use median-of-three for pivot selection
- Convert to iterative instead of recursive
- Optimize memory usage

## 5. Final Thoughts

Working through this project taught me several important lessons:

1. **Standard Quicksort** is simple and works great on random data, but can really struggle with sorted inputs.

2. **Randomized Quicksort** trades a bit of simplicity for much more consistent performance across different data types.

3. **The testing results** backed up what the theory predicted - the standard version was up to 100x slower on sorted data with 5000 elements.

4. **In practice**, randomized algorithms are usually the safer choice when you don't know what kind of data you'll be working with.

This project gave me a better understanding of why algorithm choice matters in real software development. The differences aren't just theoretical - they can have a huge impact on how fast your code runs.

## 6. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

2. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley Professional.

3. Hoare, C. A. R. (1962). Quicksort. *The Computer Journal*, 5(1), 10-16.

4. Blum, M., Floyd, R. W., Pratt, V., Rivest, R. L., & Tarjan, R. E. (1973). Time bounds for selection. *Journal of Computer and System Sciences*, 7(4), 448-461.

## 7. Code Files

All the code is in `quicksort.py`:
- Both sorting implementations
- Performance testing tools
- Analysis framework
- Test script in `test_quicksort.py`
