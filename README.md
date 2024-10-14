# MSCS-532-Final-Project

# Loop Unrolling Performance Tester

This program allows users to test the performance impact of loop unrolling. Users can input various parameters, such as the unrolling factor, the number of elements processed per iteration, and the range size (total iterations), and the program will calculate and compare the execution time for both regular loops and unrolled loops. It also generates a 3D scatter plot to visualize the results, which can be saved as an image.

## Features

- **Interactive User Input**: Users can input different test cases with varying loop unrolling factors, the number of elements per iteration, and the total range of iterations.
- **Regular vs Unrolled Loop Comparison**: The program measures execution times for both regular loops and unrolled loops, helping to identify performance improvements.
- **3D Visualization**: Execution times are plotted in a 3D scatter plot, with comparisons between regular and unrolled loops.
- **Save Plot**: The generated 3D plot is saved as an image file (`execution_times.png`).

## Requirements

- Python 3.x
- Matplotlib library
- Numpy library

## Installation

To install the required packages, use the following command:

```bash
pip install matplotlib numpy
```
## How to Run the Program

- Clone or download the code from this repository.
- Ensure Python 3.x is installed on your machine.
- Install the required dependencies (Matplotlib and Numpy) using the command shown above.
- Run the program by executing the following command in your terminal:
python loop_unrolling.py or python3 loop_unrolling.py depending on your configuration
- The program will prompt you to input the following:
The unrolling factor
The number of elements processed per iteration
The range size (total iterations)
The number of scenarios you would like to test
- The program will then compute the execution times for both regular and unrolled loops and display the results.
- A 3D scatter plot comparing execution times will be generated and saved as execution_times.png

## Example Usage

How many different scenarios would you like to test? 2

Scenario 1:
Enter the unrolling factor: 10
Enter the number of elements processed per iteration: 5
Enter the range size (total iterations): 1000000

Scenario 2:
Enter the unrolling factor: 20
Enter the number of elements processed per iteration: 10
Enter the range size (total iterations): 2000000

Regular loop time for Scenario 1: 1.234567 seconds
Unrolled loop time for Scenario 1: 0.456789 seconds
Regular loop time for Scenario 2: 2.345678 seconds
Unrolled loop time for Scenario 2: 0.987654 seconds
Execution time plot saved as 'execution_times.png'.


## Output
- The program will print the execution times for both the regular and unrolled loops.
- A 3D scatter plot will be saved as execution_times.png to visually compare the performance results.

## License

