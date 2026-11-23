
"""
File Name: 03_operators.py
Chapter: Python Fundamentals
Topic: All Seven Types of Python Operators

This program demonstrates:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
"""


# ==========================================================
# 1. ARITHMETIC OPERATORS
# Used to perform mathematical calculations.
# ==========================================================

print("\n========== 1. ARITHMETIC OPERATORS ==========")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)


# ==========================================================
# 2. ASSIGNMENT OPERATORS
# Used to assign or update variable values.
# ==========================================================

print("\n========== 2. ASSIGNMENT OPERATORS ==========")

x = 10
print("Initial Value:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x = 10
x %= 3
print("After %= 3:", x)

x = 10
x //= 3
print("After //= 3:", x)

x = 2
x **= 3
print("After **= 3:", x)

# Bitwise assignment operators
x = 5
x &= 3
print("After &= 3:", x)

x = 5
x |= 3
print("After |= 3:", x)

x = 5
x ^= 3
print("After ^= 3:", x)

x = 5
x <<= 1
print("After <<= 1:", x)

x = 5
x >>= 1
print("After >>= 1:", x)


# ==========================================================
# 3. COMPARISON OPERATORS
# Used to compare two values.
# Results are always Boolean: True or False.
# ==========================================================

print("\n========== 3. COMPARISON OPERATORS ==========")

a = 10
b = 5

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# ==========================================================
# 4. LOGICAL OPERATORS
# Used to combine or reverse conditions.
# ==========================================================

print("\n========== 4. LOGICAL OPERATORS ==========")

age = 25
has_id = True
is_employed = False

# AND: Both conditions must be True.
print("AND:", age >= 18 and has_id)

# OR: At least one condition must be True.
print("OR:", has_id or is_employed)

# NOT: Reverses the Boolean result.
print("NOT:", not has_id)


# ==========================================================
# 5. IDENTITY OPERATORS
# Check whether variables refer to the same object.
# ==========================================================

print("\n========== 5. IDENTITY OPERATORS ==========")

list_a = [10, 20, 30]

# Both variables refer to the same list object.
list_b = list_a

# This creates a separate list object.
list_c = [10, 20, 30]

# IS: Checks whether both refer to the same object.
print("list_a is list_b:", list_a is list_b)

# IS NOT: Checks whether they are different objects.
print("list_a is not list_c:", list_a is not list_c)

# == checks whether the contents are equal.
print("list_a == list_c:", list_a == list_c)

# Checking None using identity.
result = None
print("Result is None:", result is None)


# ==========================================================
# 6. MEMBERSHIP OPERATORS
# Check whether a value exists in a collection.
# ==========================================================

print("\n========== 6. MEMBERSHIP OPERATORS ==========")

skills = ["Python", "AWS", "Docker", "Kubernetes"]

# IN: Checks whether an element exists.
print("Python in skills:", "Python" in skills)

# NOT IN: Checks whether an element does not exist.
print("Java not in skills:", "Java" not in skills)

# Membership in a string.
message = "Welcome to Python"

print("Python in message:", "Python" in message)

# Membership in a dictionary checks keys.
employee = {
    "name": "Nagesh",
    "role": "DevOps Engineer"
}

print("name in employee:", "name" in employee)


# ==========================================================
# 7. BITWISE OPERATORS
# Perform operations on binary representations of integers.
# ==========================================================

print("\n========== 7. BITWISE OPERATORS ==========")

a = 5
b = 3

# Display decimal and binary values.
print("A:", a, "| Binary:", format(a, "04b"))
print("B:", b, "| Binary:", format(b, "04b"))

# AND: Both corresponding bits must be 1.
print("Bitwise AND:", a & b)

# OR: At least one corresponding bit must be 1.
print("Bitwise OR:", a | b)

# XOR: Corresponding bits must be different.
print("Bitwise XOR:", a ^ b)

# NOT: Inverts the integer bits.
print("Bitwise NOT:", ~a)

# LEFT SHIFT: Shifts bits to the left.
print("Left Shift:", a << 1)

# RIGHT SHIFT: Shifts bits to the right.
print("Right Shift:", a >> 1)


# ==========================================================
# 8. REAL-WORLD PRACTICAL EXAMPLE
# Combining multiple operators in one application.
# ==========================================================

print("\n========== PRACTICAL EXAMPLE ==========")

# Employee information.
employee_name = "Nagesh"
experience = 5
python_score = 85
has_completed_training = True

# Comparison and logical operators.
is_eligible = (
    experience >= 3
    and python_score >= 70
    and has_completed_training
)

# Display eligibility result.
print("Employee:", employee_name)
print("Experience:", experience, "years")
print("Python Score:", python_score)

if is_eligible:
    print("Result: Eligible for AI Engineering Training")
else:
    print("Result: Not Eligible Yet")


# ==========================================================
# END OF PROGRAM
# ==========================================================

