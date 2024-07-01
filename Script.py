import pygame
from Board import Board

# Setting screen and square dimensions
Dimensions = Window_Width = Window_Height = 800
BlockSize = int(Dimensions/8)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((Dimensions, Dimensions))
clock = pygame.time.Clock()
pygame.display.set_caption("LiterallyUnplayableChess")
running = True

# Switch setup
ActivePiece = None
ColourToPlay = 'white'

# Board setup
ActiveBoard = Board()
Board.init_piece_setup(ActiveBoard)

while running:

    # Board maintenance
    ActiveBoard.draw(screen)
    ActiveBoard.pieces.draw(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Selecting ActivePiece
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                # Troubleshoot code for update Board.update
                for square in ActiveBoard.squares:
                    if square.rect.collidepoint(pygame.mouse.get_pos()):
                        print(square.number)
                        print(square.piece)
                        if square.piece is not None:
                            print(square.piece.colour)
                            print(square.piece.name)

                for it, piece in enumerate(ActiveBoard.pieces):
                    if piece.colour == ColourToPlay:
                        if piece.rect.collidepoint(event.pos):

                            # Activating ActivePiece
                            ActivePiece = piece

                            # Note original rect position
                            OriginalCoordinate = ActivePiece.rect.center

                            # Acceptable squares setup
                            AcceptableSquares = Board.acceptablesquares(ActiveBoard, ActivePiece)

                            # Deactivate Acceptable squares colour shift
                            for square in AcceptableSquares:
                                square.printcolour = square.activecolour

        # Moving ActivePiece.rect
        if event.type == pygame.MOUSEMOTION:
            if ActivePiece is not None:
                ActivePiece.rect.center = (pygame.mouse.get_pos())

        # Deselecting ActivePiece
        if event.type == pygame.MOUSEBUTTONUP:
            if ActivePiece is not None:
                if event.button == 1:
                    for square in AcceptableSquares:
                        if square.rect.collidepoint(ActivePiece.rect.center):

                            # Checks if there is a piece to take and then takes it
                            Board.takes(ActiveBoard, ActivePiece)

                            # Update ActiveBoard with new piece positions
                            Board.update(ActiveBoard)

                            # Updating ColourToPlay
                            if ActivePiece.colour == 'white':
                                ColourToPlay = 'black'
                            else:
                                ColourToPlay = 'white'

                            break

                    else:
                        # Reset piece location
                        ActivePiece.rect.center = OriginalCoordinate

                        # Revert ActiveBoard with old piece positions
                        Board.update(ActiveBoard)

                    # Deactivate Acceptable squares colour shift
                    for square in AcceptableSquares:
                        square.printcolour = square.basecolour


                    # Deactivate ActivePiece
                    ActivePiece = None

    clock.tick(60)  # Set fps to 60
    pygame.display.flip()  # Update screen

pygame.quit()
