#The ability to callng and re-using methods in multiple classes:

class Fish:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a fish. My name is {self.name}. I am {self.age} years old.")

    def sound_making(self):
        print("swimmmm")


class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a lion. My name is {self.name}. I am {self.age} years old.")

    def sound_making(self):
        print("Rawrrrr")


fish1 = Fish("Dory", 0.5)
lion1 = Lion("King", 5)

for animal in (fish1, lion1):
    animal.sound_making()
    animal.info()
    animal.sound_making()