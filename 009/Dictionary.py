this_is_dictionary = {
    "this": "this is value of 'this' key",
    "is": "this is value of 'is' key",
    "two": 2,
    5: "Five"
}
print(this_is_dictionary[5])
# Output = Five


# Todo: Adding new key and value into dictionary
this_is_dictionary["eight"] = 8
print(this_is_dictionary)
# Output = {'this': "this is value of 'this' key", 'is': "this is value of 'is' key", 'two': 2, 5: 'Five', 'eight': 8}


# Todo: Edit the value of the key in dictionary
this_is_dictionary[5] = "This is not number Five"
print(this_is_dictionary[5])


# Todo: Loop through the KEY in dictionary
for key in this_is_dictionary:
    print(key)


# Todo: Loop through the KEY to get value in the dictionary
for key in this_is_dictionary:
    print(f"{key} = {this_is_dictionary[key]}")


# Todo: Deleting/wiping all item in the dictionary
this_is_dictionary = {}
print(this_is_dictionary)
# Output = {}


# Todo: Write a program that converts their scores to grades.
# Write a new dictionary called student_grades that should contain student names as keys
# and their assessed grades for values.
# The final version of the student_grades dictionary will be checked.
# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    if student_scores[name] >= 91:
        student_grades[name] = "Outstanding"
    elif student_scores[name] >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] >= 71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)



