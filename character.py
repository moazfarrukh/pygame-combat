import pygame
from Throwables import throwables
yCoord =480
maxjumplimit = 180

class Character():
    #constructor
    def __init__(self,id,x,y = yCoord):
        self.id=id
        self.RECT = pygame.Rect(x,y,70,150)
        self.up=-1
        self.velocity =0
        self.AttackType = 0
        self.health = 100
        self.Attacked = 0
        self.throw= throwables()
        self.direction =id

    #jumping fucntionality
    def jump(self):
        Grav =0.1
        if self.up==1:
            self.RECT.y -=self.velocity
            self.velocity -=self.velocity*Grav
        if self.up==0:
            self.RECT.y +=self.velocity
            self.velocity +=self.velocity*Grav
        if self.RECT.y <= yCoord-maxjumplimit:
            self.RECT.y=yCoord-maxjumplimit
            self.up=0
        if self.RECT.y >= yCoord:
            self.RECT.y = yCoord
            self.up=-1
            self.velocity = 0




    #Type of Attack
    def Attack(self,key,screen,Target):
        #moving the throwable if any
        if(pygame.time.get_ticks() - self.Attacked < 750):
            return

        damage = 0
        if key[pygame.K_z]:
            self.AttackType=1
            damage = 10
        if key[pygame.K_x]:
            self.AttackType=2
            damage = 13
        if key[pygame.K_c]:
            self.AttackType=3
            damage = 30
        
        #if no attack then return
        if self.AttackType==0:
            return
        #if the throwbable then do the following
        if(self.AttackType==3):
            self.throw.AttackWithThrowables(self.RECT.centerx,self.RECT.centery + (self.RECT.y - self.RECT.centery),self.direction)
        
        self.Attacked = True
        # else create a Rectanle for collision Detection
        AttackRect = pygame.Rect(self.RECT.centerx,self.RECT.y , 2* self.RECT.width,self.RECT.height)
        if(self.direction == 2):
            AttackRect =pygame.Rect(self.RECT.centerx-2* self.RECT.width,self.RECT.y , 2* self.RECT.width,self.RECT.height)
        pygame.draw.rect(screen,(0,255,0),AttackRect)


        if AttackRect.colliderect(Target.RECT) and not self.AttackType==3:
            #do Damage
            Target.health-=damage
            print(Target.health)
            #draw Range
            pygame.draw.rect(screen,(0,255,0),AttackRect)
        else:
            pygame.draw.rect(screen,(255,255,0),AttackRect)

        self.Attacked=pygame.time.get_ticks()
        self.AttackType=0

    #moving character
    def moveCharacter(self,s_width,scren,Target):
        Grav = 0.1
        speed = 10
        delx,dely =0,0
        
        key = pygame.key.get_pressed()

        #moving the throwbales if any
        self.throw.move(scren,s_width,Target)


        #dealing with keyboard inputs
        if key[pygame.K_LEFT]:
            delx = -speed
            self.direction=2
        if key[pygame.K_RIGHT]:
            delx = speed
            self.direction=1
        if key[pygame.K_UP] and self.up == -1:
            self.up = 1
            self.velocity =18
        if key[pygame.K_DOWN]:
            self.up = 0 
            self.velocity=20


        #defining boundaries
        if self.RECT.x+delx<0:
            delx=-self.RECT.left
        if self.RECT.right+delx > s_width:
            delx= s_width - self.RECT.right  
        self.RECT.x+=delx

        #checking for an ATTack
        self.Attack(key,scren,Target)


        if self.up==-1:
            return
        # jumping
        self.jump()

    
    #drawing Character
    def DrawCharacter(self,scren):
        pygame.draw.rect(scren,(255,0,0),self.RECT)
