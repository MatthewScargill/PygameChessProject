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
ActivePieces = Setup.initsetup(ActiveBoard.squares)[1]
ActiveBoard.squares = Setup.initsetup(ActiveBoard.squares)[0]

while running:

    # Board maintenance
    ActiveBoard.drawboard(screen)
    ActivePieces.draw(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
