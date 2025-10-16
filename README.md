# Assignment 5: Quicksort Algorithm Implementation and Analysis

## Overview

This project implements and analyzes both deterministic and randomized versions of the Quicksort algorithm. It includes comprehensive performance analysis, theoretical complexity analysis, and empirical testing across different data types and sizes.

## Files

- `quicksort.py` - Main implementation with both deterministic and randomized Quicksort algorithms
- `Assignment5_Report.md` - Detailed analysis report and findings
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Requirements

- Python 3.7+
- matplotlib >= 3.5.0
- numpy >= 1.21.0

## Installation

### Using Virtual Environment (Recommended)

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Deactivate the virtual environment when done:
```bash
deactivate
```

### Alternative: Direct Installation

If you prefer not to use a virtual environment:
```bash
pip install -r requirements.txt
```

## Usage

### Full Analysis (with all features)

Run the complete analysis with empirical testing and detailed reporting:
```bash
python quicksort.py
```

### Simple Testing (no external dependencies required)

For basic functionality testing without matplotlib/numpy:
```bash
python test_quicksort.py
```

This will execute:
1. Algorithm demonstration with sample data
2. Theoretical complexity analysis
3. Empirical performance comparison
4. Results summary

## Implementation Features

### Deterministic Quicksort
- Uses last element as pivot
- Lomuto partitioning scheme
- In-place sorting
- Performance counters for analysis

### Randomized Quicksort
- Random pivot selection
- Same partitioning scheme as deterministic
- Improved average-case performance
- Consistent behavior across data types

### Analysis Tools
- Performance measurement with timing and operation counting
- Multiple data type testing (random, sorted, reverse-sorted, nearly-sorted)
- Statistical analysis across multiple iterations
- Comprehensive reporting

## Key Findings

1. **Random Data**: Both algorithms perform similarly with O(n log n) behavior
2. **Sorted Data**: Deterministic version shows O(n²) worst-case behavior
3. **Randomized Advantage**: Consistent O(n log n) performance regardless of input
4. **Scalability**: Performance gap widens significantly with larger datasets

## Sample Output

```
RANDOM DATA:
Size     Det. Time    Rand. Time   Det. Comp  Rand. Comp
100      0.000052     0.000065     725        623       
500      0.000357     0.000480     4936       4867      
1000     0.000852     0.001062     12508      11547     

SORTED DATA (Worst case for deterministic):
Size     Det. Time    Rand. Time   Det. Comp  Rand. Comp
100      0.000328     0.000060     4950       659       
500      0.008298     0.000418     124750     4773      
1000     0.034872     0.000935     499500     10870     
```

## Educational Value

This implementation demonstrates:
- Algorithm design principles
- Complexity analysis techniques
- Randomized algorithm benefits
- Empirical performance evaluation
- Real-world algorithm selection criteria

Perfect for understanding the practical implications of algorithm choice in software development and system design.
