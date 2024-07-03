import Board

def MoveFinder(board, Activepiece):

    #tempboard = board.copy()

    # finding out what the colours are
    if Activepiece.colour == 'white':
        attacking_colour = 'black'
    else:
        attacking_colour = 'white'

    Acceptable_moves = possiblesquares(board, Activepiece)[0]  # array of possible moves for ActivePiece

    for TrialMove in Acceptable_moves:
        trialboard = tempboard(board, Activepiece, TrialMove)
        if check_king_attack(trialboard, attacking_colour) is True:
            Acceptable_moves.remove(TrialMove)



# need function that returns tempboard with the move made:
def tempboard(board, ActivePiece, TrialSquare):
    for square in board.squares:
        if square.rect.collidepoint(ActivePiece.rect.center):
            TrialSquare.piece = ActivePiece
            square.piece = None

    return board


def colourattackedsquares(self, colour):
    attackedsquares = []
    for piece in self.pieces:
        if piece.colour == colour:
            tempattackedsquares = Board.acceptablesquares(self, piece)[1]
            if tempattackedsquares is not None:
                for square in tempattackedsquares:
                    attackedsquares.append(square)
    return attackedsquares


def check_king_attack(tempboard, attackingcolour):
    for piece in tempboard.pieces:
        if piece.name == 6 and piece.colour != attackingcolour:  # Find king
            for square in tempboard.squares:
                if square.rect.collidepoint(piece.rect.center):
                    if square in colourattackedsquares(attackingcolour):
                        return True
                    else:
                        return False





def possiblesquares(self, ActivePiece):  # All theoretically accepted moves

        AllAcceptableSquares = []
        AttackedSquares = []

        if ActivePiece.name == 1:  # Pawn
            for square in self.squares:
                if square.rect.collidepoint(ActivePiece.rect.center):
                    if ActivePiece.colour == 'white':
                        if self.squares[square.number + 8].piece is None:  # Standard movement
                            AllAcceptableSquares.append(self.squares[square.number + 8])
                            if self.squares[square.number + 16].piece is None and square.rank == 1:  # Double movement
                                AllAcceptableSquares.append(self.squares[square.number + 16])

                        # Pawn attacks
                        if (self.squares[square.number + 7].piece is not None and self.squares[square.number + 7].piece.
                                colour == 'black'):
                            AllAcceptableSquares.append(self.squares[square.number + 7])
                            AttackedSquares.append(self.squares[square.number + 7])
                        if (self.squares[square.number + 9].piece is not None and self.squares[square.number + 9].piece.
                                colour == 'black'):
                            AllAcceptableSquares.append(self.squares[square.number + 9])
                            AttackedSquares.append(self.squares[square.number + 9])

                    if ActivePiece.colour == 'black':
                        if self.squares[square.number - 8].piece is None:  # Standard movement
                            AllAcceptableSquares.append(self.squares[square.number - 8])
                            if self.squares[square.number - 16].piece is None and square.rank == 6:  # Double movement
                                AllAcceptableSquares.append(self.squares[square.number - 16])

                        # Pawn attacks
                        if (self.squares[square.number - 7].piece is not None and self.squares[square.number - 7].piece.
                                colour == 'white'):
                            AllAcceptableSquares.append(self.squares[square.number - 7])
                            AttackedSquares.append(self.squares[square.number - 7])
                        if (self.squares[square.number - 9].piece is not None and self.squares[square.number - 9].piece.
                                colour == 'white'):
                            AllAcceptableSquares.append(self.squares[square.number - 9])
                            AttackedSquares.append(self.squares[square.number - 9])

        if ActivePiece.name == 2 or ActivePiece.name == 6:  # Vertical and Horizontal Moves (Rook and half of Queen)
            for square in self.squares:
                if square.rect.collidepoint(ActivePiece.rect.center):

                    for i in range(1, 8):  # Right
                        if int(square.number + i) <= 63:  # Check still in range
                            if self.squares[square.number + i].rank == square.rank:
                                if self.squares[square.number + i].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number + i])
                                    AttackedSquares.append(self.squares[square.number + i])
                                if self.squares[square.number + i].piece is not None:
                                    if self.squares[square.number + i].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number + i])
                                        AttackedSquares.append(self.squares[square.number + i])
                                        break
                                    else:
                                        break

                    for i in range(1, 8):  # Left
                        if int(square.number - i) >= 0:  # Check still in range
                            if self.squares[square.number - i].rank == square.rank:
                                if self.squares[square.number - i].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number - i])
                                    AttackedSquares.append(self.squares[square.number - i])
                                if self.squares[square.number - i].piece is not None:
                                    if self.squares[square.number - i].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number - i])
                                        AttackedSquares.append(self.squares[square.number - i])
                                        break
                                    else:
                                        break

                    for i in range(1, 8):  # Down
                        if int(square.number - i * 8) >= 0:  # Check still in range
                            if self.squares[square.number - i * 8].file == square.file:
                                if self.squares[square.number - i * 8].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number - i * 8])
                                    AttackedSquares.append(self.squares[square.number - i * 8])
                                if self.squares[square.number - i * 8].piece is not None:
                                    if self.squares[square.number - i * 8].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number - i * 8])
                                        AttackedSquares.append(self.squares[square.number - i * 8])
                                        break
                                    else:
                                        break

                    for i in range(1, 8):  # Up
                        if int(square.number + i * 8) <= 63:  # Check still in range
                            if self.squares[square.number + i * 8].file == square.file:
                                if self.squares[square.number + i * 8].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number + i * 8])
                                    AttackedSquares.append(self.squares[square.number + i * 8])
                                if self.squares[square.number + i * 8].piece is not None:
                                    if self.squares[square.number + i * 8].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number + i * 8])
                                        AttackedSquares.append(self.squares[square.number + i * 8])
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
                                    AllAcceptableSquares.append(self.squares[square.number + i])
                                    AttackedSquares.append(self.squares[square.number + i])
                                if self.squares[square.number + i].piece is not None:
                                    if self.squares[square.number + i].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number + i])
                                        AttackedSquares.append(self.squares[square.number + i])
                            elif abs(self.squares[square.number + i].rank - square.rank) == 1 and abs(
                                self.squares[square.number + i].file - square.file) == 2:
                                if self.squares[square.number + i].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number + i])
                                    AttackedSquares.append(self.squares[square.number + i])
                                if self.squares[square.number + i].piece is not None:
                                    if self.squares[square.number + i].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number + i])
                                        AttackedSquares.append(self.squares[square.number + i])

        if ActivePiece.name == 4 or ActivePiece.name == 6:  # Diagonal Movements (Bishop and half of Queen)
            for square in self.squares:
                if square.rect.collidepoint(ActivePiece.rect.center):

                    for i in range(1, min(7 - square.rank, square.file) + 1):  # Top Left
                        if int(square.number + i * 7) <= 63:  # Check still in range
                            if (self.squares[square.number + i * 7].file == square.file - i
                                    and self.squares[square.number + i * 7].rank == square.rank + i):
                                if self.squares[square.number + i * 7].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number + i * 7])
                                    AttackedSquares.append(self.squares[square.number + i * 7])
                                if self.squares[square.number + i * 7].piece is not None:
                                    if self.squares[square.number + i * 7].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number + i * 7])
                                        AttackedSquares.append(self.squares[square.number + i * 7])
                                        break
                                    else:
                                        break

                    for i in range(1, min(7 - square.rank, 7 - square.file) + 1):  # Top Right
                        if int(square.number + i * 7) <= 63:  # Check still in range
                            if (self.squares[square.number + i * 9].file == square.file + i
                                    and self.squares[square.number + i * 9].rank == square.rank + i):
                                if self.squares[square.number + i * 9].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number + i * 9])
                                    AttackedSquares.append(self.squares[square.number + i * 9])
                                if self.squares[square.number + i * 9].piece is not None:
                                    if self.squares[square.number + i * 9].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number + i * 9])
                                        AttackedSquares.append(self.squares[square.number + i * 9])
                                        break
                                    else:
                                        break

                    for i in range(1, min(square.rank, square.file) + 1):  # Bottom Left
                        if int(square.number - i * 9) >= 0:  # Check still in range
                            if (self.squares[square.number - i * 9].file == square.file - i
                                    and self.squares[square.number - i * 9].rank == square.rank - i):
                                if self.squares[square.number - i * 9].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number - i * 9])
                                    AttackedSquares.append(self.squares[square.number - i * 9])
                                if self.squares[square.number - i * 9].piece is not None:
                                    if self.squares[square.number - i * 9].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number - i * 9])
                                        AttackedSquares.append(self.squares[square.number - i * 9])
                                        break
                                    else:
                                        break

                    for i in range(1, min(square.rank, 7 - square.file) + 1):  # Bottom Right
                        if int(square.number - i * 7) >= 0:  # Check still in range
                            if (self.squares[square.number - i * 7].file == square.file + i
                                    and self.squares[square.number - i * 7].rank == square.rank - i):
                                if self.squares[square.number - i * 7].piece is None:
                                    AllAcceptableSquares.append(self.squares[square.number - i * 7])
                                    AttackedSquares.append(self.squares[square.number - i * 7])
                                if self.squares[square.number - i * 7].piece is not None:
                                    if self.squares[square.number - i * 7].piece.colour != square.piece.colour:
                                        AllAcceptableSquares.append(self.squares[square.number - i * 7])
                                        AttackedSquares.append(self.squares[square.number - i * 7])
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
                                AllAcceptableSquares.append(self.squares[square.number + i])
                                AttackedSquares.append(self.squares[square.number + i])
                            if self.squares[square.number + i].piece is not None:
                                if self.squares[square.number + i].piece.colour != square.piece.colour:
                                    AllAcceptableSquares.append(self.squares[square.number + i])
                                    AttackedSquares.append(self.squares[square.number + i])


        return AllAcceptableSquares, AttackedSquares
