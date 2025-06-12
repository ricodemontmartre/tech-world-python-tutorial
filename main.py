def days_to_hours(number_of_days: int) -> int:
    return number_of_days * 24

def days_to_minutes(number_of_days: int) -> int:
    return number_of_days * 24 * 60

def validate_and_execute(input_dictionary: dict) -> None:
    try:
        days_number = int(input_dictionary["days"])
        if days_number > 0:
            if input_dictionary["unit"] == "minutes":
                calculated_value = days_to_minutes(days_number)
                print(f"{days_number} days is {calculated_value} minutes")
            elif input_dictionary["unit"] == "hours":
                calculated_value = days_to_hours(days_number)
                print(f"{days_number} days is {calculated_value} hours")
            else:
                print("Invalid unit. Please use 'minutes' or 'hours'.")
            print(type(input_dictionary))
        elif days_number == 0:
            print("You entered 0 days, which is not valid.")
        else:
            print("Please enter a positive number of days.")
    except ValueError:
        print("Please enter an integer value.")

user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days and unit:\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    day_and_unit_dictionnary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(day_and_unit_dictionnary)
    validate_and_execute(day_and_unit_dictionnary)