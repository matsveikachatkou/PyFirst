from sys import argv

script_name, hours_worked, hour_wage, bonus = argv
print(f'Your salary is {float(hour_wage) * float(hours_worked) + float(bonus)}$')
