calculation_to_units: int = 24 * 60
name_of_unit: str = "minutes"

def days_to_units(number_of_days: int) -> int:
    return number_of_days * calculation_to_units

def validate_and_execute(input_value):
    # Validate input and execute the conversion
    try:
        user_input_int = int(input_value)
        if user_input_int > 0:
            print(f"{user_input_int} days is {days_to_units(user_input_int)} {name_of_unit}")
        elif user_input_int == 0:
            print("You entered 0 days, which is not valid.")
        else:
            print("Please enter a positive number of days.")
        """
        else:
            print("Please enter a positive number of days.")
        """
    except ValueError:
        print("Please enter an integer value.")

user_input = ""
while user_input != "exit":
    number_of_days_list = input("Enter a list of number of days separated by a comma:\n")
    print(type(number_of_days_list.split(", ")))
    print(number_of_days_list.split(", "))
    for number_of_days in number_of_days_list.split(", "):
        validate_and_execute(number_of_days)