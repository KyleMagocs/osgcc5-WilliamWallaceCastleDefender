import pygame, os, random



class PowerUp(pygame.sprite.Sprite):


    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = 0
        self.images = [pygame.image.load(os.path.join(os.curdir, 'box1.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'box2.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'box3.png')).convert_alpha(),
                    pygame.image.load(os.path.join(os.curdir, 'box4.png')).convert_alpha()]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect = self.rect.move(x,y)
        self.type = random.randint(0,2)
        #0 = MaxArrows + 10
        #1 = Multi Shot
        #2 = Rapid Fire (Infinite Arrows)
    
    def updateBoxSprite(self):
        self.framenumber += 0.33
        self.image = (int(self.framenumber)) % 4