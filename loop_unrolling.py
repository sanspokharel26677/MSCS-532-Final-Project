import timeit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Multi-line comment to explain the program
"""
This program interacts with the user to test various loop unrolling scenarios.
The user provides inputs for the unrolling factor, number of elements processed per iteration,
and range size (total iterations). It calculates execution times for both the regular and unrolled loops.
Finally, it generates a 3D plot to compare execution times and saves the plot as an image.
"""

# Function for the regular loop (no unrolling)
"""
This function simulates a regular loop without any unrolling.
It sums integers up to the specified range size.
"""
def regular_loop(range_size):
    total = 0
    # Standard loop iterating through the range size
    for i in range(range_size):
        total += i  # Add each value to the total
    return total

# Function with loop unrolling using nested loop
"""
This function performs loop unrolling based on user-specified factor and number of elements per iteration.
It sums up values while skipping iterations according to the unrolling factor.
"""
def unrolled_loop(factor, num_elements, range_size):
    total = 0
    # Nested loop for unrolling with user-specified factor and elements
    for i in range(0, range_size, factor):  # Outer loop with step size = factor
        for j in range(num_elements):  # Inner loop processing num_elements elements per iteration
            total += i + j  # Add i+j to the total in each iteration
    return total

# Helper function to get valid integer input from user
"""
This helper function prompts the user for an integer input.
If the input is not an integer, it shows an error message and asks again.
"""
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))  # Attempt to convert input to an integer
            return value
        except ValueError:
            # Inform the user about invalid input and prompt again
            print("Invalid input. Please enter a valid integer.")

# Main function to interact with user and visualize data
"""
The main function handles interaction with the user.
It collects multiple test scenarios, runs both regular and unrolled loops,
and plots the execution times in a 3D scatter plot.
"""
def main():
    # Ask how many different scenarios the user wants to test
    num_tests = get_valid_int("How many different scenarios would you like to test? ")

    results = []  # List to store execution times and corresponding input parameters

    # Loop through the number of test cases
    for test_num in range(1, num_tests + 1):
        print(f"\nScenario {test_num}:")

        # Get valid user inputs for this scenario
        factor = get_valid_int("Enter the unrolling factor: ")
        num_elements = get_valid_int("Enter the number of elements processed per iteration: ")
        range_size = get_valid_int("Enter the range size (total iterations): ")

        # Time the regular loop
        start_time = timeit.default_timer()  # Start the timer for the regular loop
        regular_loop(range_size)
        regular_time = timeit.default_timer() - start_time  # Calculate the execution time

        # Time the unrolled loop for the user-specified parameters
        start_time = timeit.default_timer()  # Start the timer for the unrolled loop
        unrolled_loop(factor, num_elements, range_size)
        unrolled_time = timeit.default_timer() - start_time  # Calculate the execution time

        # Store the results for plotting later
        results.append((factor, num_elements, range_size, regular_time, unrolled_time))

        # Print execution times for both loops
        print(f"Regular loop time for Scenario {test_num}: {regular_time:.6f} seconds")
        print(f"Unrolled loop time for Scenario {test_num}: {unrolled_time:.6f} seconds")

    # Generate a visual representation of the data
    plot_results(results)

# Function to plot results as a 3D plot and save the image
"""
This function creates a 3D scatter plot to compare the execution times of the regular and unrolled loops.
The x-axis represents the unrolling factor, the y-axis shows the number of elements processed,
and the z-axis displays the execution time. The plot is saved as an image.
"""
def plot_results(results):
    # Extracting data from results for plotting
    factors = [result[0] for result in results]  # Unrolling factors
    num_elements = [result[1] for result in results]  # Number of elements processed per iteration
    range_sizes = [result[2] for result in results]  # Range sizes (total iterations)
    regular_times = [result[3] for result in results]  # Regular loop times
    unrolled_times = [result[4] for result in results]  # Unrolled loop times

    fig = plt.figure(figsize=(12, 8))  # Set figure size for the plot

    # Create 3D scatter plot
    ax = fig.add_subplot(111, projection='3d')

    # Plot regular loop times as red circles
    ax.scatter(factors, num_elements, regular_times, c='r', marker='o', label='Regular Loop')

    # Plot unrolled loop times as blue triangles
    ax.scatter(factors, num_elements, unrolled_times, c='b', marker='^', label='Unrolled Loop')

    # Set labels and title for the plot
    ax.set_xlabel('Unrolling Factor')
    ax.set_ylabel('Num Elements per Iteration')
    ax.set_zlabel('Execution Time (seconds)')
    ax.set_title('Execution Time Comparison: Regular vs Unrolled Loops')
    ax.legend()  # Add a legend to differentiate between regular and unrolled loops

    # Save the plot to a file
    plt.savefig('execution_times.png')
    print("Execution time plot saved as 'execution_times.png'.")

    # Show the plot on screen
    plt.show()

if __name__ == "__main__":
    main()

