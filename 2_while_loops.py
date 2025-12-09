# Given:
# while loop = execute some code WHILE some condition remains true

# name = input("enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

# while name == "":
#     print("you did not enter your name")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# favorite_food = []

# while not food == "q":
#     print(f"You like {food}")
#     favorite_food.append(food)
#     food = input("Enter another food you like (q tp quit): ")

# print("bye")

# num = int(input("Enter a # betwwen 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num is not valid}")
#     num = int(input("Enter a # betwwen 1-10: "))

# print(f"Your number is {num}")

colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

index = 0 

while index < len(colors): 
    current_color = colors[index] 
    if current_color == "yellow": 
        break 
    print(current_color) 
    index += 1 