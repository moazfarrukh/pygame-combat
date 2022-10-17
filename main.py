import pygame

#initialize modules
pygame.init()
pygame.font.init()
pygame.mixer.init()

# pygame window setup
WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Combat")

# fonts/text setup
title_font = pygame.font.SysFont('comicsans', 70)
game_title = title_font.render("pygame combat", True, (187, 0, 0))

# quit button
color_dark = (100, 100, 100)
smallfont = pygame.font.SysFont('Corbel', 50)
text = smallfont.render('Quit', True, (255, 255, 255))


def start():
    intro = True

    while intro:
        # display text in the center
        WINDOW.blit(game_title, (WIDTH/2 - game_title.get_width() / 2, 40))

        # display quit button
        button = pygame.draw.rect(WINDOW, (100, 100, 100), [420, 315, 160, 60])
        WINDOW.blit(text, (460, 330))

        for event in pygame.event.get():
            # handle events that happen on intro screen
            if event.type == pygame.QUIT:
                intro = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(pygame.mouse.get_pos()):
                    intro = False
                    exit()
        pygame.display.update()


if __name__ == "__main__":
    start()
