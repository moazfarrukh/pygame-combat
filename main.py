from tkinter import W
from turtle import window_width
import pygame
from character import Character
# initialize modules
pygame.init()
pygame.font.init()
pygame.mixer.init()

# pygame window setup
WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Combat")

# fonts setup
title_font = pygame.font.SysFont('comicsans', 70)
smallfont = pygame.font.SysFont('Corbel', 50)

#clock
clock = pygame.time.Clock()
fps = 60

#defining Colors
RED = (255,0,0)


#drawing HealthBars
def Draw_HealthBars(health,x,y,var):
    pygame.draw.rect(WINDOW,(255,255,255),(x-3,y-3,406, 36 ))
    pygame.draw.rect(WINDOW,(255,0,0),(x,y,400, 30 ))
    size = health/100 * 400
    disp =400 - health/100 * 400
    if(var==1):
        pygame.draw.rect(WINDOW,(0,255,0),(x,y,size, 30 ))
    else:
        pygame.draw.rect(WINDOW,(0,255,0),(x + disp,y,size, 30 ))


# texts render
game_title = title_font.render("pygame combat", True, (187, 0, 0))
text = smallfont.render('Start', True, (255, 255, 255))
quit_text = smallfont.render('Quit', True, (255, 255, 255))

#loading the background image
bg_image = pygame.image.load("Assets/images/background/bgimage.gif").convert_alpha()

#creating players
player1 = Character(1,200)
player2 = Character(2,700)

def DrawBackground():
    bg_image_new = pygame.transform.scale(bg_image,(WIDTH,HEIGHT))
    WINDOW.blit(bg_image_new,(0,0))


def game():
    ingame = True
    while ingame:
        clock.tick(fps)
        DrawBackground()
        #Drawing HealthBars
        Draw_HealthBars(player1.health,30,30,player1.id)
        Draw_HealthBars(player2.health,570,30,player2.id)
        #moving players



        #player1.moveCharacter(WIDTH,WINDOW,player2)
        player2.moveCharacter(WIDTH,WINDOW,player1)


        #drawing players
        player1.DrawCharacter(WINDOW)
        player2.DrawCharacter(WINDOW)
        #WINDOW.fill((0, 0, 0))
        for event in pygame.event.get():
            # handle events that happen on in game screen
            if event.type == pygame.QUIT:
                ingame = False
                exit()
        pygame.display.update()


def start():
    intro = True
    while intro:
        # display game title in the center
        WINDOW.blit(game_title, (WIDTH/2 - game_title.get_width() / 2, 40))

        # display start button
        button = pygame.draw.rect(WINDOW, (100, 100, 100), [420, 315, 160, 60])
        WINDOW.blit(text, (460, 330))

        # display quit button
        button2 = pygame.draw.rect(
            WINDOW, (100, 100, 100), [420, 415, 160, 60])
        WINDOW.blit(quit_text, (460, 430))

        for event in pygame.event.get():
            # handle events that happen on intro screen
            if event.type == pygame.QUIT:
                intro = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(pygame.mouse.get_pos()):
                    # mouseclick on  start button
                    intro = False
                    game()

                if button2.collidepoint(pygame.mouse.get_pos()):
                    # mouseclick on  quit button
                    intro = False
                    exit()

        pygame.display.update()


if __name__ == "__main__":
    start()





