# import datetime
from datetime import datetime

user_input = input("Enter your goal with the deadline:\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

# deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%y")
deadline_date = datetime.strptime(deadline, "%d.%m.%y")
# today_date = datetime.datetime.today()
today_date = datetime.today()
time_till = deadline_date - today_date

# print(type(datetime.datetime.strptime(deadline_date, "%d.%m.%y")))

print(f"Time remaining for your {goal} is {time_till}")
print(f"Time remaining for your {goal} is {time_till.days} days")
print(f"Time remaining for your {goal} is {int(time_till.total_seconds() / 60 / 60)} hours")

