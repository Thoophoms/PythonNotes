def greet(name, location):
    print(f"Hi, {'Sabo' if name == 'Trish' else 'Soba'}")
    print(f"Hello {name}")
    print(f"How is the weather in {location}?")

greet(name="Trish", location="Thailand")

# name = parameter
# "Trish" = argument

def life_in_weeks(age):
    life = (90 - age) * 52
    print(f"You have {life} weeks left.")

life_in_weeks(56)


