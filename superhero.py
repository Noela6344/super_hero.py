# ----------------------------
# Assignment 1: Superhero Class
# ----------------------------

class Superhero:
    def _init_(self, name, superpower, strength, city):
        self.name = name
        self.superpower = superpower
        self.strength = strength
        self.city = city

    def introduce(self):
        print("Hi! I am {}, justice defender of {}.".format(self.name, self.city))
        print("My superpower is: {} (Strength: {}/100)".format(self.superpower, self.strength))
        print("I use my powers in court to protect the innocent and expose the guilty.")
        print("But sometimes... oops, I hear embarrassing thoughts too!")

    def fight(self, villain):
        print("{} is facing {} in the courtroom!".format(self.name, villain))
        if self.strength > 60:
            print("{} reads {}'s mind: 'I DID commit the crime!'".format(self.name, villain))
            print("Justice served! {} is exposed in court!".format(villain))
        else:
            print("{} tries to focus... but only hears 'I want nyama choma'".format(self.name))
            print("{} walks free... but the fight continues!".format(villain))

    def save_people(self):
        print("{} rushes to court to defend the innocent!".format(self.name))
        print("The judge says: 'With your mind-reading powers, justice will be fair!'")

# Create and test your superhero
hero = Superhero("MindReader", "Reading people's minds to reveal the truth", 90, "Kenya")
hero.introduce()
hero.fight("Corrupt Politician")
hero.save_people()

print("\n==============================\n")

# ----------------------------
# Activity 2: Polymorphism Challenge
# ----------------------------

class Animal:
    def move(self):
        print("This animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs, chasing its tail!")

class Bird(Animal):
    def move(self):
        print("The bird flies high in the sky, singing happily!")

class Fish(Animal):
    def move(self):
        print("The fish swims smoothly in the water!")

# Test polymorphism
animals = [Dog(), Bird(), Fish()]

print("Polymorphism Demonstration:\n")
for animal in animals:
    animal.move()