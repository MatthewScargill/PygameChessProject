import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Pawn(Piece):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)

        self.name = 1

        # Colour sorting
        self.colour = colour
        if self.colour == "black":
            self.image = pygame.image.load('PieceImages/Chess_pdt60.png')
        else:
            self.image = pygame.image.load('PieceImages/Chess_plt60.png')
        self.rect = self.image.get_rect()

