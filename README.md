Overview

This project contains two main activities that demonstrate Object-Oriented Programming (OOP) concepts in Python:

Superhero Class (Assignment 1)

A superhero with attributes and abilities like introducing themselves, fighting villains, and saving people.

Demonstrates class creation, constructors, attributes, and methods.

Polymorphism Challenge (Activity 2)

A simple Animal class with multiple subclasses (Dog, Bird, Fish).

Shows how different subclasses can override the same method (move()) to provide unique behavior.

🦸‍♀️ Assignment 1: Superhero Class

The Superhero class models a hero with the following attributes:

name: Hero’s name

superpower: Unique ability

strength: Power level (0–100)

city: City the superhero protects

Methods

introduce(): Introduces the superhero and their abilities.

fight(villain): Simulates a battle with a villain based on the hero’s strength.

save_people(): Shows the hero saving innocent people in court.

Example Usage
hero = Superhero("MindReader", "Reading people's minds to reveal the truth", 90, "Kenya")
hero.introduce()
hero.fight("Corrupt Politician")
hero.save_people()


✅ Output shows how the superhero interacts with villains and protects justice.

🐾 Activity 2: Polymorphism Challenge

This part demonstrates polymorphism by creating an Animal base class and multiple subclasses that override the move() method.

Classes

Animal: Base class with a generic move() method.

Dog: Runs on four legs.

Bird: Flies in the sky.

Fish: Swims in water.

Example Usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()


✅ Each animal outputs a different movement style, showcasing polymorphism.

🛠️ Key Concepts Demonstrated

Classes & Objects

Constructors (__init__) (note: in your code it should be __init__, not _init_)

Attributes & Methods

Encapsulation

Polymorphism through method overriding

🚀 How to Run

Copy the code into a file named superhero.py.

Run the program with:

python superhero.py
