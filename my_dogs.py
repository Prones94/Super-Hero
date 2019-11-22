# my_dogs.py
from Dog import Dog

my_dog = dog.Dog('Rex','Kryptonian')
my_other_dog = dog.Dog('Annie','Labrador')
pitbull = dog.Dog('King','Pitbull')
husky = dog.Dog('Thunder','Husky')
shitzu = dog.Dog('Mochi','Shitzu')
print(my_other_dog.name)
my_dog.bark() # each dog will make the same sound because of the function bark()
pitbull.bark()
husky.sit()
shitzu.roll()