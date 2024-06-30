import Functions
import pygame
import Pieces

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
        self.pieces = None

    def draw(self, screen):
        for square in self.squares:
            pygame.draw.rect(screen, square.printcolour, square.rect)

    def takes(self, ActivePiece):
        for piece in self.pieces:
            if piece.colour != ActivePiece.colour:
                if piece.rect.collidepoint(ActivePiece.rect.center):
                    piece.kill()

    def update(self):  # Updates square information
        for square in self.squares:
            for piece in self.pieces:
                if square.rect.collidepoint(piece.rect.center):  # Checks if piece collides with square
                    piece.rect.center = square.position  # Snap rect to center of square
                    square.piece = piece  # Update Square.piece
                    break
                if not square.rect.collidepoint(piece.rect.center):  # If no collisions, No piece
                    square.piece = None  # Update Square.piece

    def init_piece_setup(self):
        pieces = pygame.sprite.Group()

        # Pawn setup
        for i in range(8):
            whitepawn = Pieces.Pawn('white')
            self.squares[8 + i] = Square(8 + i, whitepawn)
            pieces.add(whitepawn)

            blackpawn = Pieces.Pawn('black')
            self.squares[48 + i] = Square(48 + i, blackpawn)
            pieces.add(blackpawn)

        for i in range(2):
            # Knight Setup
            whiteknight = Pieces.Knight('white')
            self.squares[1 + i * 5] = Square(1 + i * 5, whiteknight)
            pieces.add(whiteknight)

            blackknight = Pieces.Knight('black')
            self.squares[57 + i * 5] = Square(57 + i * 5, blackknight)
            pieces.add(blackknight)

            # Rook setup
            whiterook = Pieces.Rook('white')
            self.squares[0 + i * 7] = Square(0 + i * 7, whiterook)
            pieces.add(whiterook)

            blackrook = Pieces.Rook('black')
            self.squares[56 + i * 7] = Square(56 + i * 7, blackrook)
            pieces.add(blackrook)

            # Bishop Setup
            whitebishop = Pieces.Bishop('white')
            self.squares[2 + i * 3] = Square(2 + i * 3, whitebishop)
            pieces.add(whitebishop)

            blackbishop = Pieces.Bishop('black')
            self.squares[58 + i * 3] = Square(58 + i * 3, blackbishop)
            pieces.add(blackbishop)

        # King Setup
        whiteking = Pieces.King('white')
        self.squares[4] = Square(4, whiteking)
        pieces.add(whiteking)

        blackking = Pieces.King('black')
        self.squares[60] = Square(60, blackking)
        pieces.add(blackking)

        # Queen Setup
        whitequeen = Pieces.Queen('white')
        self.squares[3] = Square(3, whitequeen)
        pieces.add(whitequeen)

        blackqueen = Pieces.Queen('black')
        self.squares[59] = Square(59, blackqueen)
        pieces.add(blackqueen)

        self.pieces = pieces
