
"""
File: 01_variables.py
Topic: Python Variables
Purpose: Learn all important variable concepts with examples.
"""

# ==========================================================
# 1. STRING VARIABLES (str)
# Used to store text values.
# ==========================================================

first_name = "Nagesh"
last_name = "Pandey"
profession = "DevOps Engineer"
city = "Bengaluru"

# ==========================================================
# 2. INTEGER VARIABLES (int)
# Used to store whole numbers.
# ==========================================================

age = 25
experience = 5
year = 2026

# ==========================================================
# 3. FLOAT VARIABLES (float)
# Used to store decimal numbers.
# ==========================================================

salary = 1250.50
percentage = 85.5
height = 5.9

# ==========================================================
# 4. BOOLEAN VARIABLES (bool)
# Used to store True or False values.
# ==========================================================

is_employed = True
is_learning_python = True
is_learning_ai = False

# ==========================================================
# 5. NONE VARIABLE (NoneType)
# Represents the absence of a value.
# ==========================================================

middle_name = None

# ==========================================================
# 6. LIST VARIABLE (list)
# Ordered and changeable collection of values.
# ==========================================================

skills = ["Python", "AWS", "Docker", "Kubernetes"]

# ==========================================================
# 7. TUPLE VARIABLE (tuple)
# Ordered collection that cannot be changed.
# ==========================================================

coordinates = (12.97, 77.59)

# ==========================================================
# 8. SET VARIABLE (set)
# Stores unique values without duplicates.
# ==========================================================

certifications = {"AWS", "CKA", "Terraform", "AWS"}

# ==========================================================
# 9. DICTIONARY VARIABLE (dict)
# Stores data in key-value pairs.
# ==========================================================

employee = {
    "name": "Nagesh",
    "role": "DevOps Engineer",
    "experience": 5,
    "location": "Bengaluru"
}

# ==========================================================
# 10. MULTIPLE VARIABLE ASSIGNMENT
# Assign multiple values in a single statement.
# ==========================================================

country, language = "India", "Python"

# Assign the same value to multiple variables.
x = y = z = 100

# ==========================================================
# 11. VARIABLE REASSIGNMENT
# A variable can reference a different value.
# ==========================================================

score = 50
score = 100

# ==========================================================
# 12. DYNAMIC TYPING
# Python allows a variable to reference different data types.
# ==========================================================

value = 100          # Initially an integer
value = "Python"     # Now a string

# ==========================================================
# 13. CONSTANT VARIABLES
# Python uses uppercase naming by convention for constants.
# ==========================================================

PI = 3.14159
MAX_RETRIES = 3
APP_NAME = "AI Learning Platform"

# ==========================================================
# 14. VARIABLE TYPE CHECKING
# type() identifies the data type of a variable.
# ==========================================================

print("\n========== VARIABLE DATA TYPES ==========")

print("First Name:", first_name, "| Type:", type(first_name).__name__)
print("Age:", age, "| Type:", type(age).__name__)
print("Salary:", salary, "| Type:", type(salary).__name__)
print("Employed:", is_employed, "| Type:", type(is_employed).__name__)
print("Middle Name:", middle_name, "| Type:", type(middle_name).__name__)
print("Skills:", skills, "| Type:", type(skills).__name__)
print("Coordinates:", coordinates, "| Type:", type(coordinates).__name__)
print("Certifications:", certifications, "| Type:", type(certifications).__name__)
print("Employee:", employee, "| Type:", type(employee).__name__)

# ==========================================================
# 15. PRINT ALL VARIABLES
# Display our employee information.
# ==========================================================

print("\n========== EMPLOYEE INFORMATION ==========")

print("Full Name:", first_name, last_name)
print("Age:", age)
print("Profession:", profession)
print("Experience:", experience, "years")
print("City:", city)
print("Country:", country)
print("Salary:", salary)
print("Skills:", skills)
print("Learning Python:", is_learning_python)
print("Learning AI:", is_learning_ai)

# ==========================================================
# 16. VARIABLE OPERATIONS
# Variables can be used in calculations.
# ==========================================================

total_experience = experience + 2
monthly_salary = salary / 12

print("\n========== VARIABLE OPERATIONS ==========")

print("Future Experience:", total_experience, "years")
print("Monthly Salary:", monthly_salary)

# ==========================================================
# 17. FINAL SUMMARY
# ==========================================================

print("\n========== LEARNING SUMMARY ==========")

print("Application:", APP_NAME)
print("Python Year:", year)
print("Updated Score:", score)
print("Dynamic Variable:", value)
print("PI Constant:", PI)
print("Maximum Retries:", MAX_RETRIES)

print("\nHello Nagesh! Your Python learning journey continues!")
