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
    def __init__(self, name="Fido", breed="Mutt"):
        self.name = name
        self.breed = breed

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    # breed property
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS or value == "Mutt":
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    # example behavior methods
    def bark(self):
        print("Woof!")

    def sit(self):
        print(f"{self.name} is sitting.")