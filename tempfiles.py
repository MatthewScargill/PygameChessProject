if event.type == pygame.MOUSEBUTTONDOWN:  # Implement picking up of pieces
    if event.button == 1:
        for it, piece in enumerate(pieces):
            if piece.colour == ColourToPlay:
                if piece.rect.collidepoint(event.pos):

                    # Activate the piece
                    ActivePiece = piece

                    # Keep record of original position
                    OriginalSquare = ActivePiece.square

                    # Compute available moves
                    tempAcceptableMoves = ActivePiece.AcceptableMoves

                    # Fun colours fo visual effect -- this doesn't work oops
                    for number in tempAcceptableMoves:
                        AcceptableSquare = pygame.Rect(400, 400, BlockSize, BlockSize)
                        AcceptableSquare.center = Functions.IntToListCoord(number)
                        pygame.draw.rect(screen, 'red', AcceptableSquare, 0)
                        Board.squares[number].center = 'red'

                    print(OriginalSquare.piece)
                    print(OriginalSquare.number)

if event.type == pygame.MOUSEMOTION:  # Implement mouse motion
    if ActivePiece is not None:
        ActivePiece.update(event.pos)
        # Board.squares[number].center = 'red'

if event.type == pygame.MOUSEBUTTONUP:  # Implement snapping and letting go of pieces
    if ActivePiece is not None:
        if event.button == 1:
            if ActivePiece.number in tempAcceptableMoves:

                # Finding IntPos to find acceptable positions
                IntPos = Functions.ListToIntCoord(event.pos)

                # Finding new position to snap to
                SnapPosition = Functions.SnapPosition(event.pos)

                # Snapping piece to new position
                ActivePiece.update(SnapPosition)

                # Updating ColourToPlay
                if ActivePiece.colour == 'white':
                    ColourToPlay = 'black'
                else:
                    ColourToPlay = 'white'

                # Deactivating ActivePiece
                ActivePiece = None

                Bd.Board.PieceExistence(Board, pieces)
            else:  # Move tried is not an accepted move

                # Snapping piece to old position
                ActivePiece.update(OriginalSquare.position)

                # Deactivating ActivePiece
                ActivePiece = None