#dog.py

class Dog:
    # Required properties that are defined in the __init__ constructor method
    def __init__(self,dog_name,dog_breed):
        self.name = dog_name
        self.breed = dog_breed
        # print('Dog Initiliazed!')

    def bark(self):
        print(f'{self.name} says woooooof!')

    def sit(self):
        print(f'{self.name} sits.')

    def roll(self):
        print(f'{self.name} rolls over.')

