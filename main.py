calcution_to_units: int = 24 * 60

print("20 days is " + str(20 * calcution_to_units) + " minutes")
print(f"20 days is {20 * calcution_to_units} minutes") # f = format
print(f"30 days is {30 * calcution_to_units} minutes")

name_of_unit: str = "minutes"

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days is {num_of_days * calcution_to_units} {name_of_unit}")
    print(custom_message)

days_to_units(567, "Test 1")
days_to_units(12, "Test 2")

