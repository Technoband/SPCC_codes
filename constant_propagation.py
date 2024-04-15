
def constant_propagation(code):
    optimized_code = []

    constants = {}  # Dictionary to store constant values

    for line in code:
        parts = line.split()
        if len(parts) == 3:
            # Assignment statement
            var_name, op, value = parts
            if value.isdigit():
                constants[var_name] = int(value)
                continue
            # Check if the value is a variable that has a constant assigned to it
            if value in constants:
                constants[var_name] = constants[value]
                continue
        # Replace variables with their constant values if available
        for i, part in enumerate(parts):
            if part in constants:
                parts[i] = str(constants[part])
        optimized_code.append(' '.join(parts))

    return optimized_code

# Example usage
code = [
    "a = 5",
    "b = a + 3",
    "c = a * 2",
    "d = c - a",
    "e = a * 4"
]

optimized_code = constant_propagation(code)
print("Optimized Code:")
for line in optimized_code:
    print(line)
