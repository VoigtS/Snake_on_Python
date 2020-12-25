import sys, pygame
import random
from pygame import *



class apple:
    appleCounter = 0
    
    def __init__(self):
        self.pos = position()
        self.image = pygame.image.load("apple.png")
        self.positioning()

    def positioning(self):
        self.pos.x = random.randrange(App.windowWidth - self.image.get_rect().size[0])
        self.pos.y = random.randrange(App.windowHeight - self.image.get_rect().size[1])

class position:
    x = 0
    y = 50

    def moveUp(self):
        self.y -= 1
    
    def moveDown(self):
        self.y += 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1


class App:
    windowWidth = 800
    windowHeight = 800
    color = 255,255,255
    
    def __init__(self):
        self.running = True
        self.pos = position()
        self.apple = apple()
        self.screen = pygame.display.set_mode((App.windowWidth, App.windowHeight))
        self.block = pygame.image.load("block.jpg")
        pygame.display.set_caption("Template")

    def on_init(self):
        pygame.init()
        self.running = True
        pygame.font.init()
        self.font1 = pygame.font.SysFont('Open Sans', 30)

    def renderField(self):
        self.screen.fill(self.color)
        self.score = self.font1.render('Score: ' + str(self.apple.appleCounter), True, (0, 0, 0))
        self.screen.blit(self.score, (0,0))
        self.screen.blit(self.block, (self.pos.x, self.pos.y))
        self.screen.blit(self.apple.image, (self.apple.pos.x, self.apple.pos.y))
        pygame.display.flip()

    def quitEvent(self, event):
        self.running = False
        pygame.quit()
        sys.exit()

    def checkCollision(self, x1, y1, x2, y2):
        playerSizeX = self.block.get_rect().size[0]
        playerSizeY = self.block.get_rect().size[1]
        appleSizeX = self.apple.image.get_rect().size[0]
        appleSizeY = self.apple.image.get_rect().size[1]
        
        if(x1 + playerSizeX >= x2 and x1 <= x2 + appleSizeX):
            if(y1 + playerSizeY >= y2 and y1 <= y2 + appleSizeY):
                self.apple.appleCounter += 1
                return(True)
            
        return(False)

    def execute(self):
        if self.on_init() == False:
            self.running = False

        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if(keys[K_RIGHT] and self.pos.x < self.windowWidth - self.block.get_rect().size[0]):
                self.pos.moveRight()
            elif(keys[K_LEFT] and self.pos.x > 0):
                self.pos.moveLeft()
            elif(keys[K_UP] and self.pos.y > 0):
                self.pos.moveUp()
            elif(keys[K_DOWN] and self.pos.y < self.windowHeight - self.block.get_rect().size[1]):
                self.pos.moveDown()

            self.renderField()
            
            if(self.checkCollision(self.pos.x, self.pos.y, self.apple.pos.x, self.apple.pos.y)):
                self.apple.positioning()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitEvent(event)


if __name__ == "__main__":
    App.windowWidth = 800
    App.windowHeight = 600
    app = App()
    app.execute()

    
