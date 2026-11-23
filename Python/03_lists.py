
"""
File Name: 04_lists.py
Chapter: Python Fundamentals
Topic: Python Lists

This program demonstrates:
1. Creating Lists
2. Accessing List Items
3. Positive and Negative Indexing
4. List Slicing
5. Updating List Items
6. Adding Items
7. Removing Items
8. List Methods
9. Membership Operators
10. Looping Through Lists
11. List Comprehension
12. Nested Lists
13. List Copying
14. List Sorting
15. List Operations
"""

# ==========================================================
# 1. CREATING LISTS
# Lists can store multiple values in a single variable.
# ==========================================================

print("\n========== 1. CREATING LISTS ==========")

# List of strings
skills = ["Python", "AWS", "Docker", "Kubernetes"]

# List of integers
numbers = [10, 20, 30, 40, 50]

# List of floats
prices = [100.50, 200.75, 300.25]

# Mixed data types
employee = ["Nagesh", 28, "DevOps Engineer", 5, True]

# Empty list
empty_list = []

# Using the list constructor
languages = ["Python", "Java", "Go"]

print("Skills:", skills)
print("Numbers:", numbers)
print("Prices:", prices)
print("Employee:", employee)
print("Empty List:", empty_list)
print("Languages:", languages)

# Check list data type
print("Data Type:", type(skills))


# ==========================================================
# 2. ACCESSING LIST ITEMS
# Positive indexing starts from 0.
# Negative indexing starts from -1.
# ==========================================================

print("\n========== 2. ACCESSING LIST ITEMS ==========")

print("First Skill:", skills[0])
print("Second Skill:", skills[1])
print("Last Skill:", skills[-1])
print("Second Last Skill:", skills[-2])


# ==========================================================
# 3. LIST SLICING
# Syntax: list[start:end:step]
# End index is excluded.
# ==========================================================

print("\n========== 3. LIST SLICING ==========")

print("First Three Skills:", skills[:3])
print("From Index 2:", skills[2:])
print("Index 1 to 2:", skills[1:3])
print("Every Second Item:", skills[::2])
print("Reverse List:", skills[::-1])


# ==========================================================
# 4. UPDATING LIST ITEMS
# Lists are mutable, so their values can be changed.
# ==========================================================

print("\n========== 4. UPDATING LIST ITEMS ==========")

skills[1] = "Azure"

print("Updated Skills:", skills)

# Update multiple elements using slicing.
skills[1:3] = ["AWS", "Terraform"]

print("Updated Multiple Items:", skills)


# ==========================================================
# 5. ADDING ITEMS TO A LIST
# append() adds one item.
# insert() adds an item at a specific index.
# extend() adds multiple items.
# ==========================================================

print("\n========== 5. ADDING ITEMS ==========")

skills.append("GitHub Actions")
print("After Append:", skills)

skills.insert(1, "Linux")
print("After Insert:", skills)

skills.extend(["Jenkins", "Ansible"])
print("After Extend:", skills)


# ==========================================================
# 6. REMOVING ITEMS FROM A LIST
# remove() removes the first matching value.
# pop() removes and returns an item.
# del removes an item by index.
# clear() removes all items.
# ==========================================================

print("\n========== 6. REMOVING ITEMS ==========")

remove_skills = ["Python", "AWS", "Docker", "Java"]

remove_skills.remove("AWS")
print("After Remove:", remove_skills)

removed_item = remove_skills.pop(1)
print("Popped Item:", removed_item)
print("After Pop:", remove_skills)

del remove_skills[0]
print("After Del:", remove_skills)

# Demonstrate clear() on a separate list.
temporary_list = [10, 20, 30]
temporary_list.clear()

print("After Clear:", temporary_list)


# ==========================================================
# 7. IMPORTANT LIST METHODS
# index(), count(), sort(), reverse(), copy()
# ==========================================================

print("\n========== 7. LIST METHODS ==========")

numbers = [30, 10, 20, 10, 40]

# Find the index of an element.
print("Index of 20:", numbers.index(20))

# Count occurrences of an element.
print("Count of 10:", numbers.count(10))

# Sort the list in ascending order.
numbers.sort()
print("Ascending Order:", numbers)

# Sort the list in descending order.
numbers.sort(reverse=True)
print("Descending Order:", numbers)

# Reverse the current order.
numbers.reverse()
print("After Reverse:", numbers)

# Create a copy of the list.
copied_numbers = numbers.copy()
print("Copied List:", copied_numbers)


# ==========================================================
# 8. MEMBERSHIP OPERATORS
# in checks whether an item exists.
# not in checks whether an item does not exist.
# ==========================================================

print("\n========== 8. MEMBERSHIP OPERATORS ==========")

skills = ["Python", "AWS", "Docker", "Kubernetes"]

print("Python Exists:", "Python" in skills)
print("Java Does Not Exist:", "Java" not in skills)

if "Python" in skills:
    print("Python skill is available.")


# ==========================================================
# 9. LOOPING THROUGH A LIST
# Use for loop to access every item.
# enumerate() provides both index and value.
# ==========================================================

print("\n========== 9. LOOPING THROUGH LISTS ==========")

skills = ["Python", "AWS", "Docker", "Kubernetes"]

# Basic for loop.
for skill in skills:
    print("Skill:", skill)

# Using enumerate() to get index and value.
for index, skill in enumerate(skills, start=1):
    print(index, "-", skill)


# ==========================================================
# 10. LIST COMPREHENSION
# A concise way to create a new list.
# ==========================================================

print("\n========== 10. LIST COMPREHENSION ==========")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Create a list of squares.
squares = [number ** 2 for number in numbers]

print("Squares:", squares)

# Create a list containing only even numbers.
even_numbers = [number for number in numbers if number % 2 == 0]

print("Even Numbers:", even_numbers)

# Create a list containing only odd numbers.
odd_numbers = [number for number in numbers if number % 2 != 0]

print("Odd Numbers:", odd_numbers)


# ==========================================================
# 11. NESTED LISTS
# A list can contain other lists.
# ==========================================================

print("\n========== 11. NESTED LISTS ==========")

employees = [
    ["Nagesh", "DevOps Engineer", 5],
    ["John", "Python Developer", 3],
    ["David", "Cloud Engineer", 4]
]

print("First Employee:", employees[0])
print("Employee Name:", employees[0][0])
print("Employee Role:", employees[1][1])

# Loop through nested list.
for employee in employees:
    print(
        "Name:", employee[0],
        "| Role:", employee[1],
        "| Experience:", employee[2]
    )


# ==========================================================
# 12. LIST COPYING
# Assignment creates another reference to the same list.
# copy() creates a separate shallow copy.
# ==========================================================

print("\n========== 12. LIST COPYING ==========")

original = [10, 20, 30]

# Both variables refer to the same list.
reference_copy = original

reference_copy.append(40)

print("Original After Reference Update:", original)
print("Reference Copy:", reference_copy)

# Create a separate shallow copy.
independent_copy = original.copy()

independent_copy.append(50)

print("Original List:", original)
print("Independent Copy:", independent_copy)


# ==========================================================
# 13. LIST OPERATIONS
# Concatenation and repetition.
# ==========================================================

print("\n========== 13. LIST OPERATIONS ==========")

list_a = [10, 20, 30]
list_b = [40, 50, 60]

# Combine two lists.
combined_list = list_a + list_b

print("Combined List:", combined_list)

# Repeat list elements.
repeated_list = list_a * 2

print("Repeated List:", repeated_list)

# Find the number of items.
print("List Length:", len(combined_list))


# ==========================================================
# 14. REAL-WORLD PRACTICAL EXAMPLE
# Manage employee skills using a Python list.
# ==========================================================

print("\n========== 14. EMPLOYEE SKILL MANAGEMENT ==========")

employee_name = "Nagesh"

employee_skills = [
    "Linux",
    "AWS",
    "Docker",
    "Kubernetes",
    "Terraform"
]

# Add a new skill.
employee_skills.append("Python")

# Check whether the employee knows Python.
has_python = "Python" in employee_skills

# Display employee information.
print("Employee Name:", employee_name)
print("Total Skills:", len(employee_skills))
print("Employee Skills:")

for index, skill in enumerate(employee_skills, start=1):
    print(index, "-", skill)

if has_python:
    print("Python skill successfully added!")

print("\nHello Nagesh! You have completed Python Lists.")
