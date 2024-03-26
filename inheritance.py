import random

class Animal:
    info = "a living organism that feeds on organic matter"

    def __init__(self, name):
        print("An animal is created.")
        self.name = name

class Dog(Animal):
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."

    def __init__(self, name):
        super().__init__(name)
        print("A dog is created.")
        self.lucky_number = random.randint(1, 10)
        self.fur = ""
        

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")
        
        
class Bulldog(Dog):
    
    def __init__(self, name):
        super().__init__(name)
        print("A bulldog is created.")


dog1 = Bulldog("Fido")



# class Electronics():
    
#     def __init__(self):
#         print("Don't mix with water.")

# class PC(Electronics):
#     gpu = "RTX 3080ti"
#     cpu = "Core i9-13900K"
    
#     def __init__(self):
#         super().__init__()
    
#     def specs(self):
#         print(f"My PC has a {self.gpu}, a {self.cpu}, with {self.ram} of memory.")


# pc1 = PC()

# pc1.ram = "64 gb"

# pc1.specs()
