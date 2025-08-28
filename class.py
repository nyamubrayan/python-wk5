# Base class
class ChessPiece:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        return f"{self.color} {self.name}"


# PlayerPiece with encapsulation
class PlayerPiece(ChessPiece):
    def __init__(self, name, color, position):
        super().__init__(name, color)
        self.__position = position  # private attribute

    def move(self, new_position):
        self.__position = new_position
        return f"{self.info()} moved to {self.__position}"

    def get_position(self):
        return f"{self.info()} is at {self.__position}"


# SpecialPiece with polymorphic move
class SpecialPiece(ChessPiece):
    def __init__(self, name, color, position=None):
        super().__init__(name, color)
        self.__position = position

    def move(self):
        # Special pieces have unique movements
        return f"{self.info()} moves differently based on strategy!"


# Mini Chess Board Simulation
def main():
    # Create pieces
    white_pawn = PlayerPiece("Pawn", "White", "A2")
    black_queen = SpecialPiece("Queen", "Black", "D8")
    
    print("=== Initial Positions ===")
    print(white_pawn.get_position())
    print(black_queen.move())  # polymorphic behavior

    print("\n=== Move Simulation ===")
    new_pos = input("Enter new position for White Pawn (e.g., A4): ").upper()
    print(white_pawn.move(new_pos))

    print("\n=== Final State ===")
    print(white_pawn.get_position())
    print(black_queen.move())  # still polymorphic

if __name__ == "__main__":
    main()
