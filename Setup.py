import pygame
import Pieces
from Board import Square


def initsetup(squares):
    pieces = pygame.sprite.Group()

    # Pawn setup
    for i in range(8):
        whitepawn = Pieces.Pawn('white')
        squares[8 + i] = Square(8 + i, whitepawn)
        pieces.add(whitepawn)

        blackpawn = Pieces.Pawn('black')
        squares[48 + i] = Square(48 + i, blackpawn)
        pieces.add(blackpawn)

    for i in range(2):

        # Knight Setup
        whiteknight = Pieces.Knight('white')
        squares[1 + i*5] = Square(1 + i*5, whiteknight)
        pieces.add(whiteknight)

        blackknight = Pieces.Knight('black')
        squares[57 + i*5] = Square(57 + i*5, blackknight)
        pieces.add(blackknight)

        # Rook setup
        whiterook = Pieces.Rook('white')
        squares[0 + i*7] = Square(0 + i*7, whiterook)
        pieces.add(whiterook)

        blackrook = Pieces.Rook('black')
        squares[56 + i*7] = Square(56 + i*7, blackrook)
        pieces.add(blackrook)


        # Bishop Setup
        whitebishop = Pieces.Bishop('white')
        squares[2 + i*3] = Square(2 + i*3, whitebishop)
        pieces.add(whitebishop)

        blackbishop = Pieces.Bishop('black')
        squares[58 + i*3] = Square(58 + i*3, blackbishop)
        pieces.add(blackbishop)

    # King Setup
    whiteking = Pieces.King('white')
    squares[4] = Square(4, whiteking)
    pieces.add(whiteking)

    blackking = Pieces.King('black')
    squares[60] = Square(60, blackking)
    pieces.add(blackking)

    # Queen Setup
    whitequeen = Pieces.Queen('white')
    squares[3] = Square(3, whitequeen)
    pieces.add(whitequeen)

    blackqueen = Pieces.Queen('black')
    squares[59] = Square(59, blackqueen)
    pieces.add(blackqueen)

    return squares, pieces
