# Coding Questions Week 02
# Matthew Macalalad, 101510305

import random

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print("Elements: ", elements)

# git add . && git commit -m "add elements array" && git push

# def func_name():
#        return True

# def say_greeting(name, message = "Hi"):
#     print(f"{message}, {name}")

# say_greeting("Matthew")
# say_greeting("Matthew", "Hello")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer")
            continue

try:
    elements_selected = get_valid_int_input("Enter the index of the element you like: ")
    # Roll dice
    element_roll = random.randint(1, 6)
    totalNum = elements_selected + element_roll
    # Print the result based on the totalNum
    if element_roll <= 2:
        print("You rolled a weak element, friend.")
    elif element_roll <= 4:
        print("Your element is moderately strong.")
    else:
        print("Nice element.")
except Exception as e:
    print("")
