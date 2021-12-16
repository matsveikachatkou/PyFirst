initial_rating = [7, 5, 3, 3, 2]
new_element = input("Please provide new rating: ")

try:
    new_element = int(new_element)
except ValueError:
    print("That's not an integer number")

initial_rating.append(new_element)
initial_rating.sort(reverse=True)
print(initial_rating)
