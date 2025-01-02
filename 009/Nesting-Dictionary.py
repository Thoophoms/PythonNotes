# Dictionary
# {Key: Value, Key2: Value2}

# Todo: Nesting Dictionary
# {
#   Key: [List],
#   Key2: {Dict},
# }

# Normal Dictionary
capitals = {
    "France" : "Paris",
    "USA" : "Washington DC",
    "Thailand" : "Bangkok",
}

# Print the entire dictionary
print(capitals)

# Print only key in the dictionary
for key in capitals:
    print(key)
# Output
# France
# USA
# Thailand


# Todo: Nested List in Dictionary
travel_log = {
    "Thailand" : ["Bangkok", "Nakhon Pathom", "Samuthsongkarm", "Chaing Mai"],
    "USA" : {
        "New Jersey" : ["Denville", "Morristown", "Montclair"],
        "New York" : ["Staten Island", "Manhattan"]
    },
}
# Print the entire dictionary
print(travel_log)

# Todo: Print Bangkok - Thailand in dictionary
print(travel_log["Thailand"][0])

# Todo: Print Montclair from USA in New Jersey dictionary
print(travel_log["USA"]["New Jersey"][2])

for key1 in travel_log:
    print(key1)
# output
# Thailand
# USA

# Todo: Nested List
nested_list = ["a", "b", ["c", "d"]]

# print the entire list
print(nested_list)

# print item index 0 from the list
print(nested_list[0])

# Todo: print "d" from the nested_list
print(nested_list[2][1])

# Todo: Change the dictionary name
# Change capitals to capital_cities
print(capitals)
capital_cities = capitals
print(capital_cities)
