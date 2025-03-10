#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name = "fido", breed = "Mutt"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    
    def set_name(self,name):
        if  not isinstance(name,str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self._name = "fido"
        else:
            self._name = name


    def get_breed(self):
        return self._breed

    def set_breed(self,breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self._breed = "Mutt"
        else:
            self._breed = breed


    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

doggy = Dog()
doggy.name = ""
doggy.breed = "Poodle"
print(doggy.name)
print(doggy.breed)






            
