import random

# num = random.randint(1, 3)
# print(num)
#
# # Create a random floating point number from 0 to 1 that will include 0 and may not include 1
# floatingNum = random.random()
# print(floatingNum)
#
# # When * 10, you will get random number with floating point numbers from 0 to 10 and may not include 10
# print(floatingNum * 10)
#
# # Random number depends on the upperbound. So you may or may not get the upperbound depends on the rounding
# # Recommend using random.random() instead of random.uniform(a, b)
# random_float = random.uniform(1, 10)
# print(random_float)

random_num = random.randint(1, 2)
print(random_num)

if random_num == 1:
    print("Head")
else:
    print("Tail")

# use random.choice(list)
names = ["Johnnie", "Tiana", "Bowie", "Trisha"]
print(random.choice(names))
