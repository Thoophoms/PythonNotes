import random

pay_the_bill_today = ["Johnnie", "Tiana", "Bowie", "Trisha"]
random_num = random.randint(0,3)

print(f"Congratulations!!! {pay_the_bill_today[random_num]} will pay the bill today. YAY!!!!")

# Or using random.choice(list)
print(f"{random.choice(pay_the_bill_today)} will help you pay too!!")


# Nested LISTS
fruits = ["Strawberries", "Apple", "Watermelon", "Mango"]
vegetables = ["Onions", "Carrot"]

mix = [fruits, vegetables]

print(mix)
print(fruits)
print(vegetables)


# us_states = [
#     "Delaware",
#     "Pennsylvania",
#     "New Jersey",
#     "Georgia",
#     "Connecticut",
#     "Massachusetts",
#     "Maryland",
#     "South Carolina",
#     "New Hampshire",
#     "Virginia",
#     "New York",
#     "North Carolina",
#     "Rhode Island",
#     "Vermont",
#     "Kentucky",
#     "Tennessee",
#     "Ohio",
#     "Louisiana",
#     "Indiana",
#     "Mississippi",
#     "Illinois",
#     "Alabama",
#     "Maine",
#     "Missouri",
#     "Arkansas",
#     "Michigan",
#     "Florida",
#     "Texas",
#     "Iowa",
#     "Wisconsin",
#     "California",
#     "Minnesota",
#     "Oregon",
#     "Kansas",
#     "West Virginia",
#     "Nevada",
#     "Nebraska",
#     "Colorado",
#     "North Dakota",
#     "South Dakota",
#     "Montana",
#     "Washington",
#     "Idaho",
#     "Wyoming",
#     "Utah",
#     "Oklahoma",
#     "New Mexico",
#     "Arizona",
#     "Alaska",
#     "Hawaii"
# ]
#
# print(us_states[0])
# print(us_states[-1])
#
# # Add item into the list
# us_states.append("Trisha")
# print(us_states[-1])
#
# # Delete item in the list
# us_states.pop(-1)
# print(us_states[-1])
#
# # Delete item with name
# us_states.remove("Hawaii")
# print(us_states[-1])
#
# # Change the item in the list using index number
# us_states[-1] = "Not Alaska"
# print(us_states[-1])
#
# # Adding more than one item into the list
# us_states.extend(["Alaska Maybe", "Hello Alaska"])
# print(us_states[-2], us_states[-1])
