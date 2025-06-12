calcution_to_units: int = 24 * 60

print("20 days is " + str(20 * calcution_to_units) + " minutes")
print(f"20 days is {20 * calcution_to_units} minutes") # f = format
print(f"30 days is {30 * calcution_to_units} minutes")

name_of_unit: str = "minutes"

def days_to_units(num_of_days, custom_message):
    print(num_of_days > 0)
    condition_check = num_of_days > 0
    print(type(condition_check))

    if num_of_days > 0:
        print(f"{num_of_days} days is {num_of_days * calcution_to_units} {name_of_unit}")
        print(custom_message)
    elif num_of_days == 0:
        print("You entered 0 days, which is not valid.")
    else:
        print("Please enter a positive number of days.")

days_to_units(567, "Test 1")
days_to_units(12, "Test 2")

def scope_check(num_of_days: int):
    my_var = "Variable inside function"
    print(name_of_unit) # function body
    print(num_of_days)
    print(my_var)

def return_value() -> str:
    return "returned value"

print(return_value())

scope_check(20)

user_input = input("Enter a number of days:\n")
print(f"Number of days: {user_input}")

def validate_input(input_value):
    if input_value.isdigit():
        user_input = int(input_value)
        days_to_units(user_input, "This is a custom message")
    else:
        print("Please enter an integer value.")

validate_input(user_input)

def validate_and_execute(input_value):
    if input_value.isdigit():
        user_input_int = int(input_value)
        if user_input_int > 0:
            print(f"{user_input_int} days is {user_input_int * calcution_to_units} {name_of_unit}")
        elif user_input_int == 0:
            print("You entered 0 days, which is not valid.")
    else:
        print("Please enter an integer value.")

validate_and_execute(user_input)

print(type("This is a string"))
print(type(22))
print(type(2.2))