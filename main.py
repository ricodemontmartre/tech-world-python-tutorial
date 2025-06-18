# import helpers
# import helpers as h
# from helpers import validate_and_execute, user_input_message

import os
import logging

print(os.name)

logger = logging.getLogger("MAIN")
logger.error("This is an error message")

"""
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    day_and_unit_dictionnary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(day_and_unit_dictionnary)
    # helpers.validate_and_execute(day_and_unit_dictionnary)
    validate_and_execute(day_and_unit_dictionnary)
"""