import random


class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1, 10)
        self.name = name


dog1 = Dog("Fido")
dog2 = Dog("Sarah")

print(dog1.name)
print(dog2.name)

# class PC:
#     gpu = "RTX 3080ti"
#     cpu = "Core i9-13900K"


# pc1 = PC()

# pc1.ram = "64 gb"

# print(pc1.ram)
