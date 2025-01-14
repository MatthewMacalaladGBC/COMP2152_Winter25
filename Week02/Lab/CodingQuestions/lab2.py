# Coding Questions Week 02
# Matthew Macalalad, 101510305

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

