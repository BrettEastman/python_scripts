# The syntax for a lambda function is:

# lambda arguments: expression

# - `arguments`: These are the input parameters for the lambda function.
# - `expression`: This is a single expression that is evaluated and returned.

# Key Characteristics

# 1. Anonymous: Lambda functions do not have a name. They are defined and used in a single line of code.
# 2. Single Expression: The body of a lambda function is a single expression, not a block of statements.
# 3. Immediate Use: Lambda functions are often used for short, simple operations and are typically used immediately where they are defined.

# Examples

# Basic Example

# A simple lambda function that adds two numbers:

from functools import reduce
def add(x, y): return x + y


print(add(2, 3))  # Output: 5

# Using Lambda with `sorted`

# Lambda functions are often used with higher-order functions like `sorted`, `map`, `filter`, and `reduce`.

# Sorting a list of tuples based on the second element
data = [(1, 2), (3, 1), (5, 4)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(3, 1), (1, 2), (5, 4)]

# Using Lambda with `map`

# The `map` function applies a given function to each item of an iterable (such as a list) and returns a list of the results.

# Squaring each number in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Using Lambda with `filter`

# The `filter` function constructs an iterator from elements of an iterable for which a function returns true.

# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Using Lambda with `reduce`

# The `reduce` function applies a rolling computation to sequential pairs of values in a list.


# Summing all numbers in a list
numbers = [1, 2, 3, 4]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Output: 10

# When to Use Lambda Functions

# - Short, Simple Operations: Use lambda functions for short, simple operations where defining a full function would be overkill.
# - Inline Use: Use lambda functions when you need a quick, throwaway function for a specific task, such as sorting or filtering.
# - Readability: Use lambda functions when they enhance readability and conciseness. For more complex operations, a named function is often more readable and maintainable.

# When Not to Use Lambda Functions

# - Complex Logic: Avoid using lambda functions for complex logic that requires multiple statements or conditions.
# - Reusability: If a function needs to be reused in multiple places, define it as a named function instead of a lambda function.
# - Readability: If the lambda function becomes too complex or hard to read, it's better to define a named function.

# Summary

# Lambda functions in Python are a powerful tool for creating short, anonymous functions that can be used for simple operations and passed as arguments to higher-order functions. They are particularly useful for tasks like sorting, mapping, filtering, and reducing, but should be used judiciously to maintain code readability and simplicity.
