revenue = int(input("Please provide revenue: "))
costs = int(input("Please provide costs: "))

if revenue >= costs:
    print(f"Your Net Profit is {revenue - costs}$")
    print(f"Profitability is {(revenue - costs)/revenue:.2%}")
    number_employers = int(input("Please provide number of employers: "))
    print(f"Net Profit per cap: {(revenue - costs) / number_employers}$")
else:
    print(f"Your Loss is {costs - revenue}$")
