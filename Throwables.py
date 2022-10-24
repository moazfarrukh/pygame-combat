import pygame
class throwables():
    def __init__(self):
        self.Rect = pygame.Rect(0,0,40,40)
        self.active = False
        self.Direction = 0
        self.timer = pygame.time.get_ticks()


    #called when a throwable is thrown
    def AttackWithThrowables(self,x,y,direction):
        if(pygame.time.get_ticks() - self.timer > 5000):
            self.active=False
        if(self.active==True):
            return
        #direction for the attack
        self.Direction=direction
        self.Rect.x = x
        self.Rect.y = y
        self.timer = pygame.time.get_ticks()
        self.active  = True




    #for moving the throwable
    def move(self,screen,screenWidth,Target):
        if(self.Direction==0):
            return
        if self.Rect.colliderect(Target.RECT) : 
            Target.health-=25
            self.Direction=0
            return
        if self.Direction==1:
            self.Rect.x+=15
        elif self.Direction==2:
            self.Rect.x-=15
        
        #out of bound check
        if(self.Rect.right < 0) or (self.Rect.x > screenWidth):
            self.Direction=0
        self.DrawThrowables(screen)
    #Drawing the Throwable
    def DrawThrowables(self,screen):
        if(self.active==False):
            return
        pygame.draw.rect(screen,(0,255,0),self.Rect)
