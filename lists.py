months_list = ["January", "February", "March", "April", "May", "June", "January"]
print(months_list[2])

for month in months_list:
    print(month)

months_list.append("July")
print(months_list)

# print(months_list[10])

months_list.remove("January")
print(months_list)