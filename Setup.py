import pygame
import Pieces
from Board import Square


def initsetup(squares):
    pieces = pygame.sprite.Group()
    for i in range(8):
        whitepawn = Pieces.Pawn('white')
        squares[8 + i] = Square(8 + i, whitepawn)
        pieces.add(whitepawn)

        blackpawn = Pieces.Pawn('black')
        squares[48 + i] = Square(48 + i, blackpawn)
        pieces.add(blackpawn)

    return squares, pieces
