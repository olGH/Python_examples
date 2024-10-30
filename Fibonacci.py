# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. Mathematically, it can be expressed as:
#           F(n)=F(n−1)+F(n−2)
# with initial conditions: F(0)=0,F(1)=1

#The Fibonacci sequence appears in many different areas of mathematics and nature,
# such as in the branching of trees, the arrangement of leaves on a stem, the fruit sprouts of a pineapple, and many more.

#This will display a graph with the Fibonacci numbers plotted against their indices.

import matplotlib.pyplot as plt
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
n = 10  # Change this value to generate more or fewer Fibonacci numbers


print(fibonacci(20))
# Generate Fibonacci sequence
fib_sequence = fibonacci(n)

# Plotting the Fibonacci sequence
plt.figure(figsize=(10, 5))
plt.plot(fib_sequence, marker='*', linestyle='-', color='r')
plt.title(f'Fibonacci Sequence up to {n} terms')
plt.xlabel('Index')
plt.ylabel('Fibonacci Number')
plt.grid(True)
plt.show()