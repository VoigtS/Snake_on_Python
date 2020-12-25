import sys, pygame
import random
from pygame import *

class player:
    direction = 0
    gameSpeed = 5
    playerWait = 0

    def __init__(self, length):
        self.pos = position()
        self.length = length
        self.image = pygame.image.load("block.jpg")

    def playerAutoMove(self):
        self.playerWait += 1
        
        if (self.playerWait >= self.gameSpeed):
            if(self.direction == 0  and self.pos.x < app.windowWidth - self.image.get_rect().size[0]):
                self.pos.moveRight()
            elif(self.direction == 1 and self.pos.x > 0):
                self.pos.moveLeft()
            elif(self.direction == 2 and self.pos.y > 0):
                self.pos.moveUp()
            elif(self.direction == 3  and self.pos.y < app.windowHeight - self.image.get_rect().size[1]):
                self.pos.moveDown()
            self.playerWait = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    #def playerGrow(self):
        
        

class apple:
    appleCounter = 0
    
    def __init__(self):
        self.pos = position()
        self.image = pygame.image.load("apple.png")
        self.positioning()

    def positioning(self):
        self.pos.x = random.randrange(app.windowWidth - self.image.get_rect().size[0])
        self.pos.y = random.randrange(app.windowHeight - self.image.get_rect().size[1])

class position:
    x = 0
    y = 50

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def moveUp(self):
        self.y -= 1
    
    def moveDown(self):
        self.y += 1


class app:
    windowWidth = 800
    windowHeight = 600
    color = 255,255,255
    
    def __init__(self):
        self.running = True
        self.player = player(3)
        self.apple = apple()
        self.screen = pygame.display.set_mode((app.windowWidth, app.windowHeight))
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
        self.screen.blit(self.player.image, (self.player.pos.x, self.player.pos.y))
        self.screen.blit(self.apple.image, (self.apple.pos.x, self.apple.pos.y))
        pygame.display.flip()

    def quitEvent(self, event):
        self.running = False
        pygame.quit()
        sys.exit()

    def checkCollision(self, x1, y1, x2, y2):
        playerSizeX = self.player.image.get_rect().size[0]
        playerSizeY = self.player.image.get_rect().size[1]
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
            
            if(keys[K_RIGHT]):
                self.player.moveRight()
            elif(keys[K_LEFT] ):
                self.player.moveLeft()
            elif(keys[K_UP] ):
                self.player.moveUp()
            elif(keys[K_DOWN]):
                self.player.moveDown()

            self.renderField()
            self.player.playerAutoMove()
            
            if(self.checkCollision(self.player.pos.x, self.player.pos.y, self.apple.pos.x, self.apple.pos.y)):
                self.apple.positioning()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitEvent(event)


if __name__ == "__main__":
    app.windowWidth = 800
    app.windowHeight = 600
    game = app()
    game.execute()

    
