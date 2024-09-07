# Define a string
s = "Hello, welcome to my world."

# Test cases
try:
    # Find the first occurrence of 'e'
    print(s.index('e'))  # Output: 1

    # Find the first occurrence of 'e' starting from index 5
    print(s.index('e', 5))  # Output: 8

    # Find the first occurrence of 'e' between index 5 and 10
    print(s.index('e', 5, 10))  # Output: 8

    # This will raise a ValueError because 'z' is not in the string
    print(s.index('z'))
except ValueError as e:
    print(e)