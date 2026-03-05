student = {
    "John": 81,
    "Alice": 92,
    "Bob": 78
}

value_to_find = 92
for key, value in student.items():
    if value == value_to_find:
        print("Key for value", value_to_find, "is:", key)
