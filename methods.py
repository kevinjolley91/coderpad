import random


class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1, 10)
        self.name = name

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")


dog1 = Dog("Fido")
dog2 = Dog("Sarah")

dog1.bark()
dog2.bark()

# class PC:
#     gpu = "RTX 3080ti"
#     cpu = "Core i9-13900K"
    
#     def specs(self):
#         print(f"My PC has a {self.gpu}, a {self.cpu}, with {self.ram} of memory.")


# pc1 = PC()

# pc1.ram = "64 gb"

# pc1.specs()
