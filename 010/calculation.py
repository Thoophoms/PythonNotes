# Todo 1: Write 4 functions - add, subtract, multiply, divide

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# Todo 2: Add 4 functions into a dictionary

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# # Todo 3: Test! - Use the dictionary operations to perform the calculation.
# result = operations["*"](4,8)
# print(result)

# Todo 4: Functionality
def calculator():
    continue_operations = True

    first_number = float(input("Pick the number: "))

    while continue_operations:
        # Loop through the operation symbol in operations dictionary
        for operation_key in operations:
            print(operation_key)
        user_operation = input("Pick the operation: ")
        second_number = float(input(f"Pick the number you would like to do the operation: "))

        if user_operation in operations:
            result = float(operations[user_operation](first_number, second_number))
            print(f"{first_number} {user_operation} {second_number} = {result}")

            # Ask if the user wants to continue
            continue_operation = (input(f"Would you like to continue working with {result}? \n'y' for Yes or 'n' for No: ")).lower()
            if continue_operation == "y":
                first_number = result
            else:
                continue_operations = False
        else:
            print("You put an invalid operation. Please try again")

    # Ask if the user wants to start over with the new calculation?
    start_again = (input("Would you like to start over the calculation? 'y' for Yes or 'n' for No: ")).lower()
    if start_again == "y":
        calculator()
    else:
        print("Thank you, Bye!")
        end_the_program = True

calculator()
