month_number = input("Please provide the number of the month: ")

while True:
    try:
        month_number = int(month_number)
        break
    except ValueError:
        print("That's not an integer number")
        month_number = input("Please provide the number of the month: ")

if month_number not in range(1, 13):
    print("Wrong number, your month number is 1!")
    month_number = 1

list_month = [["January", "Winter"], ["February", "Winter"], ["March", "Spring"], ["April", "Spring"],
              ["May", "Spring"], ["June", "Summer"], ["July", "Summer"], ["August", "Summer"],
              ["September", "Autumn"], ["October", "Autumn"], ["November", "Autumn"], ["December", "Winter"]]

print(f"{list_month[month_number-1][0]} is {list_month[month_number-1][1]}")

month_number_2 = input("Please provide the number of the month again: ")

while True:
    try:
        month_number_2 = int(month_number)
        break
    except ValueError:
        print("That's not an integer number")
        month_number_2 = input("Please provide the number of the month: ")

if month_number_2 not in range(1, 13):
    print("Wrong number, your month number is 1!")
    month_number_2 = 1

dict_month = {1: ["January", "Winter"],
              2: ["February", "Winter"],
              3: ["March", "Spring"],
              4: ["April", "Spring"],
              5: ["May", "Spring"],
              6: ["June", "Summer"],
              7: ["July", "Summer"],
              8: ["August", "Summer"],
              9: ["September", "Autumn"],
              10: ["October", "Autumn"],
              11: ["November", "Autumn"],
              12: ["December", "Winter"]}

print(f"{dict_month[month_number_2][0]} is {dict_month[month_number_2][1]}")
