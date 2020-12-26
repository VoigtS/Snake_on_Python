import sys, pygame
import random
from pygame import *

class player:
    x = [0]
    y = [50]
    playerWidth = 0
    playerHeight = 0
    direction = 0
    gameSpeed = 200
    playerWait = 0

    def __init__(self, length):
        self.length = length
        self.image = pygame.image.load("block.jpg")
        self.playerWidth = self.image.get_rect().size[0]
        self.playerHeight = self.image.get_rect().size[1]

        for i in range(self.length - 1):
            self.x.append(0)
            self.y.append(50)
            self.x[i] = (self.length - i - 1) * self.playerWidth

    def playerAutoMove(self):
        self.playerWait += 1
        
        if (self.playerWait >= self.gameSpeed):

            #for i in range(len(self.x)):
              #  print(self.x[i], self.y[i])
            #print("xxxx" * 10)

            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
            
            if(self.direction == 0  and self.x[0] < app.windowWidth - self.playerWidth):
                self.x[0] += self.playerWidth
            elif(self.direction == 1 and self.x[0] > 0):
                self.x[0] -= self.playerWidth
            elif(self.direction == 2 and self.y[0] > 0):
                self.y[0] -= self.playerHeight
            elif(self.direction == 3  and self.y[0] < app.windowHeight - self.playerHeight):
                self.y[0] += self.playerHeight
                
            self.playerWait = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def growPlayer(self, screen):
        self.y.append(self.y[-1])
        self.x.append(self.x[-1])

        self.length += 1
        
    def drawPlayer(self, screen):
        for i in range(self.length):
            screen.blit(self.image, (self.x[i], self.y[i]))
        
        
class apple:
    x = 0
    y = 0
    appleWidth = 0
    appleHeight = 0
    appleCounter = 0
    
    def __init__(self):
        self.image = pygame.image.load("apple.png")
        self.appleWidth = self.image.get_rect().size[0]
        self.appleHeight = self.image.get_rect().size[1]
        self.positioning()

    def positioning(self):
        self.x = random.randrange(app.windowWidth - self.appleWidth)
        self.y = random.randrange(app.windowHeight - self.appleHeight)


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
        self.score = self.font1.render('Score: ' + str(apple.appleCounter), True, (0, 0, 0))
        self.screen.blit(self.score, (0,0))
        self.player.drawPlayer(self.screen)
        self.screen.blit(self.apple.image, (self.apple.x, self.apple.y))
        pygame.display.flip()

    def checkCollision(self, x1, y1, x2, y2, objectWidth, objectHeight):
        
        if(x1 + self.player.playerWidth >= x2 and x1 <= x2 + objectWidth):
            if(y1 + self.player.playerHeight >= y2 and y1 <= y2 + objectHeight):
                apple.appleCounter += 1
                self.player.growPlayer(self.screen)
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
            
            if(self.checkCollision(self.player.x[0], self.player.y[0], self.apple.x, self.apple.y, self.apple.appleWidth, self.apple.appleHeight)):
                self.apple.positioning()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitEvent(event)

    def quitEvent(self, event):
        self.running = False
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app.windowWidth = 800
    app.windowHeight = 600
    game = app()
    game.execute()

    
