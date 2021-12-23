from sys import argv


def salary():
    try:
        hours_worked, hour_wage, bonus = argv[1:]
        print(f'Your salary is {float(hour_wage) * float(hours_worked) + float(bonus)}$')
    except ValueError:
        print("Please enter numbers!")


salary()
