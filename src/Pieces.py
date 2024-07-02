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
            self.image = pygame.image.load('../rsc/Chess_pdt60.png')
        else:
            self.image = pygame.image.load('../rsc/Chess_plt60.png')
        self.rect = self.image.get_rect()


class Rook(Piece):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)

        self.name = 2

        self.colour = colour
        if self.colour == "black":
            self.image = pygame.image.load('../rsc/Chess_rdt60.png')
        else:
            self.image = pygame.image.load('../rsc/Chess_rlt60.png')
        self.rect = self.image.get_rect()


class Knight(Piece):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)

        self.name = 3

        self.colour = colour
        if self.colour == "black":
            self.image = pygame.image.load('../rsc/Chess_ndt60.png')
        else:
            self.image = pygame.image.load('../rsc/Chess_nlt60.png')
        self.rect = self.image.get_rect()


class Bishop(Piece):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)

        self.name = 4

        self.colour = colour
        if self.colour == "black":
            self.image = pygame.image.load('../rsc/Chess_bdt60.png')
        else:
            self.image = pygame.image.load('../rsc/Chess_blt60.png')
        self.rect = self.image.get_rect()


class King(Piece):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)

        self.name = 5

        self.colour = colour
        if self.colour == "black":
            self.image = pygame.image.load('../rsc/Chess_kdt60.png')
        else:
            self.image = pygame.image.load('../rsc/Chess_klt60.png')
        self.rect = self.image.get_rect()


class Queen(Piece):
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)

        self.name = 6

        self.colour = colour
        if self.colour == "black":
            self.image = pygame.image.load('../rsc/Chess_qdt60.png')
        else:
            self.image = pygame.image.load('../rsc/Chess_qlt60.png')
        self.rect = self.image.get_rect()
