import pygame
from Board import Board
import Setup

Dimensions = Window_Width = Window_Height = 800
BlockSize = int(Dimensions/8)

pygame.init()
screen = pygame.display.set_mode((Dimensions, Dimensions))
clock = pygame.time.Clock()
pygame.display.set_caption("LiterallyUnplayableChess")
running = True

ActivePiece = None
ColourToPlay = 'white'

# Board setup
ActiveBoard = Board()
ActiveBoard.squares, ActivePieces = Setup.initsetup(ActiveBoard.squares)

while running:

    # Board maintenance
    ActiveBoard.drawboard(screen)
    ActivePieces.draw(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Implement picking up of pieces
            if event.button == 1:
                for it, piece in enumerate(ActivePieces):
                    if piece.colour == ColourToPlay:
                        if piece.rect.collidepoint(event.pos):
                            ActivePiece = piece

        if event.type == pygame.MOUSEMOTION:  # Implement mouse motion
            if ActivePiece is not None:
                ActivePiece.rect.move_ip(event.rel)

        if event.type == pygame.MOUSEBUTTONUP:  # Implement snapping and letting go of pieces
            if ActivePiece is not None:
                if event.button == 1:
                    ActivePiece = None

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
