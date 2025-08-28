Assignment 1: Design Your Own Class(class.py)
Description

This  demonstrates Object-Oriented Programming (OOP) concepts using a chess-themed class hierarchy.
It includes:

Inheritance: PlayerPiece and SpecialPiece inherit from ChessPiece.

Encapsulation: Private attribute __position in PlayerPiece.

Polymorphism: move() behaves differently in PlayerPiece and SpecialPiece.

Constructors: Each piece is initialized with unique values (name, color, position).

Features

Create chess pieces with attributes like name, color, and position.

Move pieces safely using encapsulated methods.

Special pieces have unique movement behavior.

Example Usage
pawn = PlayerPiece("Pawn", "White", "A2")
queen = SpecialPiece("Queen", "Black", "D8")

print(pawn.get_position())
pawn.move("A4")
print(queen.move())

Assignment 2: Polymorphism Challenge(move.py)
Description

This  demonstrates polymorphism in Python using vehicles with the same method move(), but each class defines it differently.

Features

Classes: Car, Plane, Boat, Bike

Each class implements move() differently, showcasing polymorphism.

Optional base class Vehicle for better structure and inheritance.

Example Usage
vehicles = [Car(), Plane(), Boat(), Bike()]

for vehicle in vehicles:
    vehicle.move()


Output:

Driving on the road 
Flying in the sky 
Sailing on the water 
Riding on the path 

How to Run

Ensure you have Python 3.x installed.

Copy the Python files 

Run each file using:
bash
class.py
move.py


python assignment1.py
python assignment2.py
