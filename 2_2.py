number_of_elements = input("How many elements do you want to provide? ")

while True:
    try:
        number_of_elements = int(number_of_elements)
        break
    except ValueError:
        print("That's not an integer number")
        number_of_elements = input("How many elements do you want to provide? ")

if number_of_elements < 0:
    number_of_elements = 0
list_of_elements = []
counter = 0

while counter < number_of_elements:
    element_of_the_list = input("Please provide element of the list: ")
    list_of_elements.append(element_of_the_list)
    counter += 1

new_list = []

if len(list_of_elements) % 2 == 0:
    for index in range(0, len(list_of_elements), 2):
        new_list.append(list_of_elements[index+1])
        new_list.append(list_of_elements[index])
elif len(list_of_elements) == 1:
    new_list = list_of_elements
else:
    for index in range(0, len(list_of_elements)-1, 2):
        new_list.append(list_of_elements[index + 1])
        new_list.append(list_of_elements[index])
    new_list.append(list_of_elements[-1])


print(new_list)
