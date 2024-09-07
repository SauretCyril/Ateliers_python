def test_slice(s, i, j):
    return s[i:j]

# Example usage
s = "Hello, World!"
i = 7
j = 12
result = test_slice(s, i, j)
print(f"Slice of '{s}' from index {i} to {j} is: '{result}'")