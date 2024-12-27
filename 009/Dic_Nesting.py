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

