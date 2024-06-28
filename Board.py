import Functions
import pygame

Dimensions = Window_Width = Window_Height = 800
BlockSize = int(Dimensions/8)


class Square:
    def __init__(self, number, piece):

        self.piece = piece
        # Position variables
        self.number = number
        self.position = Functions.IntToListCoord(number)
        self.file = self.number % 8
        self.rank = self.number // 8

        if self.piece != None:
            self.piece.rect.center = self.position

        # Colour coding (could be melted into one)
        if (self.rank + self.file) % 2 == 0:
            self.colour = 'black'
            self.printcolour = (0, 141, 94)
        else:
            self.colour = 'white'
            self.printcolour = (250, 250, 250)

        # rectangle setup
        rect = pygame.rect.Rect(0, 0, BlockSize, BlockSize)
        rect.center = self.position
        self.rect = rect

        # this is collision detection foundation



class Board:
    def __init__(self):
        squares = []
        for i in range(64):
            squares.append(Square(i, None))
        self.squares = squares

    def drawboard(self, screen):
        for square in self.squares:
            pygame.draw.rect(screen, square.printcolour, square.rect)
