# For Loop
names = ["Peter", "Vanda", "Johnnie", "Tiana", "Bowie", "Trisha"]
for name in names:
    print(f"{name} Supa")
print(names)


# Adding numbers together
sum_scores = 0
scores = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
for i in scores:
    print(f"{sum_scores} + {i}")
    sum_scores += i
    print(f"The total now = {sum_scores}")


# sum() to sum the int in the list
sum_num = sum(scores)
print(sum_num)

# max function
max_score = max(scores)
print(f"The maximum score = {max_score}")

# finding max using for loop
max_num = scores[0]
print(f"Set max score to the first number on the list: {max_num}")
for i in scores:
    if i > max_num:
        max_num = i
print(f"Using For loop to find maximum score: {max_num}")


# min function
min_score = min(scores)
print(f"The minimum score = {min_score}")

# Using For Loop to find minimum score
min_num = scores[0]
print(f"Set min score to the first number on the list: {min_num}")
for i in scores:
    if i < min_num:
        min_num = i
print(f"Using For loop to find minimum score: {min_num}")

# the average score
average_score = round(float(sum_num / len(scores)), 2)
print(average_score)
# Using for loop to find Average
sum_total = 0
count = 0
for i in scores:
    sum_total += i
    count += 1
average = round((sum_total / count), 2)
print(f"Using for loop to find average score: {average}")
# ____________________________________________________

# range(a, b) will work with for loop
# This will print 0 - 9.... not including 10
for i in range(0, 10 + 1):
    print(i)


# range(a, b, step) with step
# This will not include 20
for i in range(0, 20, 2):
    print(i)

# adding 1 to 100 using range
adding_total = 0
for i in range(1, 100+1):
    adding_total += i
print(adding_total)
