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
            self.basecolour = (0, 141, 94)
            self.activecolour = (250, 51, 4)
            self.printcolour = self.basecolour
        else:
            self.colour = 'white'
            self.basecolour = (250, 250, 250)
            self.activecolour = (250, 100, 100)
            self.printcolour = self.basecolour

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
            for square in self.squares:
                if square.rect.collidepoint(piece.rect.center):
                    if piece.colour != ActivePiece.colour:
                        if square.rect.collidepoint(ActivePiece.rect.center):
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

    '''
    def unacceptablesquares(self):
        UnacceptableKingSquares = []
        for piece in self.pieces:
            for square in self.pieces:
                if square.rect.collidepoint(piece.rect.center):
                    if piece.colour != ActivePiece.colour:
                        UnacceptableKingSquares.append(square)
                        
    '''
    def acceptablesquares(self, ActivePiece):

        AcceptableSquares = []

        if ActivePiece.name == 1:  # Pawn
            for square in self.squares:
                if square.rect.collidepoint(ActivePiece.rect.center):
                    if ActivePiece.colour == 'white':
                        if self.squares[square.number + 8].piece is None:  # Standard movement
                            AcceptableSquares.append(self.squares[square.number + 8])
                            if self.squares[square.number + 16].piece is None and square.rank == 1:  # Double move
                                AcceptableSquares.append(self.squares[square.number + 16])

                        # Pawn attacks
                        if (self.squares[square.number + 7].piece is not None and self.squares[square.number + 7].piece.
                                colour == 'black'):
                            AcceptableSquares.append(self.squares[square.number + 7])
                        if (self.squares[square.number + 9].piece is not None and self.squares[square.number + 9].piece.
                                colour == 'black'):
                            AcceptableSquares.append(self.squares[square.number + 9])

                    if ActivePiece.colour == 'black':
                        if self.squares[square.number - 8].piece is None:
                            AcceptableSquares.append(self.squares[square.number - 8])
                            if self.squares[square.number - 16].piece is None and square.rank == 6:
                                AcceptableSquares.append(self.squares[square.number - 16])

                        # Pawn attacks
                        if (self.squares[square.number - 7].piece is not None and self.squares[square.number - 7].piece.
                                colour == 'white'):
                            AcceptableSquares.append(self.squares[square.number - 7])
                        if (self.squares[square.number - 9].piece is not None and self.squares[square.number - 9].piece.
                                colour == 'white'):
                            AcceptableSquares.append(self.squares[square.number - 9])

        if ActivePiece.name == 2 or ActivePiece.name == 6:  # Vertical and Horizontal Moves (Rook and half of Queen)
            for square in self.squares:
                if square.rect.collidepoint(ActivePiece.rect.center):

                    for i in range(1, 8):  # Right
                        if int(square.number + i) <= 63:  # Check still in range
                            if self.squares[square.number + i].rank == square.rank:
                                if self.squares[square.number + i].piece is None:
                                    AcceptableSquares.append(self.squares[square.number + i])
                                if self.squares[square.number + i].piece is not None:
                                    if self.squares[square.number + i].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number + i])
                                        break
                                    else:
                                        break

                    for i in range(1, 8):  # Left
                        if int(square.number - i) >= 0:  # Check still in range
                            if self.squares[square.number - i].rank == square.rank:
                                if self.squares[square.number - i].piece is None:
                                    AcceptableSquares.append(self.squares[square.number - i])
                                if self.squares[square.number - i].piece is not None:
                                    if self.squares[square.number - i].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number - i])
                                        break
                                    else:
                                        break

                    for i in range(1, 8):  # Down
                        if int(square.number - i * 8) >= 0:  # Check still in range
                            if self.squares[square.number - i * 8].file == square.file:
                                if self.squares[square.number - i * 8].piece is None:
                                    AcceptableSquares.append(self.squares[square.number - i * 8])
                                if self.squares[square.number - i * 8].piece is not None:
                                    if self.squares[square.number - i * 8].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number - i * 8])
                                        break
                                    else:
                                        break

                    for i in range(1, 8):  # Up
                        if int(square.number + i * 8) <= 63:  # Check still in range
                            if self.squares[square.number + i * 8].file == square.file:
                                if self.squares[square.number + i * 8].piece is None:
                                    AcceptableSquares.append(self.squares[square.number + i * 8])
                                if self.squares[square.number + i * 8].piece is not None:
                                    if self.squares[square.number + i * 8].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number + i * 8])
                                        break
                                    else:
                                        break

        if ActivePiece.name == 3:  # Knight Moves
            for square in self.squares:
                if square.rect.collidepoint(ActivePiece.rect.center):
                    knightmoves = [-17, -15, -6, -10, 10, 6, 15, 17]
                    for i in knightmoves:
                        if int(square.number + i) in range(63):
                            if abs(self.squares[square.number + i].rank - square.rank) == 2 and abs(
                                    self.squares[square.number +i].file - square.file) == 1:
                                if self.squares[square.number + i].piece is None:
                                    AcceptableSquares.append(self.squares[square.number + i])
                                if self.squares[square.number + i].piece is not None:
                                    if self.squares[square.number + i].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number + i])
                            elif abs(self.squares[square.number + i].rank - square.rank) == 1 and abs(
                                self.squares[square.number + i].file - square.file) == 2:
                                if self.squares[square.number + i].piece is None:
                                    AcceptableSquares.append(self.squares[square.number + i])
                                if self.squares[square.number + i].piece is not None:
                                    if self.squares[square.number + i].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number + i])

        if ActivePiece.name == 4 or ActivePiece.name == 6:  # Diagonal Movements (Bishop and half of Queen)
            for square in self.squares:
                if square.rect.collidepoint(ActivePiece.rect.center):

                    for i in range(1, min(7 - square.rank, square.file) + 1):  # Top Left
                        if int(square.number + i * 7) <= 63:  # Check still in range
                            if (self.squares[square.number + i * 7].file == square.file - i
                                    and self.squares[square.number + i * 7].rank == square.rank + i):
                                if self.squares[square.number + i * 7].piece is None:
                                    AcceptableSquares.append(self.squares[square.number + i * 7])
                                if self.squares[square.number + i * 7].piece is not None:
                                    if self.squares[square.number + i * 7].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number + i * 7])
                                        break
                                    else:
                                        break

                    for i in range(1, min(7 - square.rank, 7 - square.file) + 1):  # Top Right
                        if int(square.number + i * 7) <= 63:  # Check still in range
                            if (self.squares[square.number + i * 9].file == square.file + i
                                    and self.squares[square.number + i * 9].rank == square.rank + i):
                                if self.squares[square.number + i * 9].piece is None:
                                    AcceptableSquares.append(self.squares[square.number + i * 9])
                                if self.squares[square.number + i * 9].piece is not None:
                                    if self.squares[square.number + i * 9].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number + i * 9])
                                        break
                                    else:
                                        break

                    for i in range(1, min(square.rank, square.file) + 1):  # Bottom Left
                        if int(square.number - i * 9) >= 0:  # Check still in range
                            if (self.squares[square.number - i * 9].file == square.file - i
                                    and self.squares[square.number - i * 9].rank == square.rank - i):
                                if self.squares[square.number - i * 9].piece is None:
                                    AcceptableSquares.append(self.squares[square.number - i * 9])
                                if self.squares[square.number - i * 9].piece is not None:
                                    if self.squares[square.number - i * 9].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number - i * 9])
                                        break
                                    else:
                                        break

                    for i in range(1, min(square.rank, 7 - square.file) + 1):  # Bottom Right
                        if int(square.number - i * 7) >= 0:  # Check still in range
                            if (self.squares[square.number - i * 7].file == square.file + i
                                    and self.squares[square.number - i * 7].rank == square.rank - i):
                                if self.squares[square.number - i * 7].piece is None:
                                    AcceptableSquares.append(self.squares[square.number - i * 7])
                                if self.squares[square.number - i * 7].piece is not None:
                                    if self.squares[square.number - i * 7].piece.colour != square.piece.colour:
                                        AcceptableSquares.append(self.squares[square.number - i * 7])
                                        break
                                    else:
                                        break

        if ActivePiece.name == 5:  # King
            for square in self.squares:
                if square.rect.collidepoint(ActivePiece.rect.center):
                    kingmoves = [-9, -8, -7, -1, 1, 7, 8, 9]
                    for i in kingmoves:
                        if int(square.number + i) in range(63):
                            if self.squares[square.number + i].piece is None:
                                AcceptableSquares.append(self.squares[square.number + i])
                            if self.squares[square.number + i].piece is not None:
                                if self.squares[square.number + i].piece.colour != square.piece.colour:
                                    AcceptableSquares.append(self.squares[square.number + i])

        return AcceptableSquares

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
