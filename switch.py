# Requires Python 3.10

direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "east":
        print("Right")
    case "west":
        print("Left")
    case _:
        print("Not a valid direction.")

# age = input("What did you have for dinner? ").lower()

# match age:
#     case "burger":
#         print("That sounds really good.")
#     case _:
#         print("Have you thought about burgers?")
        