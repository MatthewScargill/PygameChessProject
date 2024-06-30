import Functions
import pygame

Dimensions = Window_Width = Window_Height = 800
BlockSize = int(Dimensions/8)


class Square:
    def __init__(self, number, piece):

        # Piece variable
        self.piece = piece

        # Position variables
        self.number = number
        self.position = Functions.IntToListCoord(number)
        self.file = self.number % 8
        self.rank = self.number // 8

        # possibly redundant rect correction code
        if self.piece is not None:
            self.piece.rect.center = self.position

        # Colour coding (could be melted into one)
        if (self.rank + self.file) % 2 == 0:
            self.colour = 'black'
            self.printcolour = (0, 141, 94)
        else:
            self.colour = 'white'
            self.printcolour = (250, 250, 250)

        # Rect setup
        rect = pygame.rect.Rect(0, 0, BlockSize, BlockSize)
        rect.center = self.position
        self.rect = rect


class Board:
    def __init__(self):
        # Empty Board Squares setup
        squares = []
        for i in range(64):
            squares.append(Square(i, None))
        self.squares = squares

    def draw(self, screen):
        for square in self.squares:
            pygame.draw.rect(screen, square.printcolour, square.rect)

    def update(self, pieces):  # Updates square information
        for square in self.squares:
            for piece in pieces:
                if square.rect.collidepoint(piece.rect.center):  # Checks if piece collides with square
                    piece.rect.center = square.position  # Snap rect to center of square
                    square.piece = piece  # Update Square.piece
                    break
                if not square.rect.collidepoint(piece.rect.center):  # If no collisions, No piece
                    square.piece = None  # Update Square.piece
