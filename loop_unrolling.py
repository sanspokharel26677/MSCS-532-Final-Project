import timeit

# Multi-line comment to explain the program
"""
This Python script demonstrates the concept of loop unrolling. 
First, we have a standard loop, and then we unroll the loop manually.
We'll measure the performance of both to show how unrolling can reduce loop overhead.
"""

# Function without loop unrolling
def regular_loop():
    total = 0
    # Standard loop iterating 10000000 times
    for i in range(100000000):
        total += i
    return total

"""
This function performs a summation using a loop unrolling factor of <any factor>.
The loop processes number of factor elements in each iteration to reduce loop control overhead.
"""
# Function with loop unrolling
def unrolled_loop():
    total = 0
    # Unrolling the loop manually to reduce overhead (processing 5 elements per iteration)
    for i in range(0, 100000000, 50):
        total += i
        total += i + 1
        total += i + 2
        total += i + 3
        total += i + 4
      
        
      
    return total

# Timing the regular loop
regular_time = timeit.timeit(regular_loop, number=1)

# Timing the unrolled loop
unrolled_time = timeit.timeit(unrolled_loop, number=1)

# Output the time difference
print(f"Regular loop time: {regular_time} seconds")
print(f"Unrolled loop time: {unrolled_time} seconds")


