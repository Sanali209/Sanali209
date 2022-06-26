# snake game

#main imports
import pygame
import sys
import random
import time
import os

#snake class
class Snake:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_x = 1
        self.velocity_y = 1
        self.body = [] #list of coordinates
        self.body.append(self.x)
        self.body.append(self.y)
        self.score = 0


    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.body.append(self.x)
        self.body.append(self.y)
        self.body.pop(0)
        self.body.pop(0)
    # draw snake on screen
    def draw(self, surface):
        for i in range(len(self.body)-1):
            pygame.draw.rect(surface, (0,0,255), (self.body[i], self.body[i+1], 10, 10))


    def check_collision(self):
        if self.x > self.width or self.x < 0 or self.y > self.height or self.y < 0:
            return True
        for i in range(len(self.body)):
            if self.x == self.body[i] and self.y == self.body[i+1]:
                return True
        return False

# food class
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,640),random.randint(0,480))
        self.value = 1

    def update(self):
        self.rect.center = (random.randint(0,640),random.randint(0,480))

    def draw(self, surface):
        surface.blit(self.image, self.rect)



#game board class
class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(320,240,10,10)
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.game_over_text = pygame.font.SysFont("comicsansms", 100)

    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.game_over = True
        if self.snake.x == self.food.rect.centerx and self.snake.y == self.food.rect.centery:
            self.score += self.food.value
            self.food.update()
            self.snake.body.append(self.snake.x)
            self.snake.body.append(self.snake.y)

    def draw(self, surface):
        self.food.draw(surface)
        self.snake.draw(surface)
        if self.game_over:
            game_over_text = self.game_over_text.render("Game Over", True, (255,255,255))
            surface.blit(game_over_text, (320,240))



#main game class
class Game:




    #initialize game
    def __init__(self):
        # deain variables
        self.width = 1024
        self.height = 768

        #initialize pygame
        pygame.init()
        #set up screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        #set up caption
        pygame.display.set_caption("Snake")
        #set up clock
        self.clock = pygame.time.Clock()
        #set up font
        self.font = pygame.font.SysFont("comicsans", 30)

        #set up game board
        self.game_board = GameBoard(640,480)



     #main game loop
    def game_loop(self):
        while True:
            #check for events
            self.check_events()
            #update game
            self.update()
            #draw game
            self.draw()
            #wait
            self.clock.tick(60)

    #check for events
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game_board.snake.velocity_x = -1
                    self.game_board.snake.velocity_y = 0
                if event.key == pygame.K_RIGHT:
                    self.game_board.snake.velocity_x = 1
                    self.game_board.snake.velocity_y = 0
                if event.key == pygame.K_UP:
                    self.game_board.snake.velocity_y = -1
                    self.game_board.snake.velocity_x = 0
                if event.key == pygame.K_DOWN:
                    self.game_board.snake.velocity_y = 1
                    self.game_board.snake.velocity_x = 0

    #update game
    def update(self):
        self.game_board.update()

    #define game over function
    def game_over(self):
        self.game_board.game_over = True
        self.game_board.snake.velocity_x = 0
        self.game_board.snake.velocity_y = 0
        self.game_board.snake.x = 320
        self.game_board.snake.y = 240
        self.game_board.snake.body = []
        self.game_board.snake.body.append(self.game_board.snake.x)
        self.game_board.snake.body.append(self.game_board.snake.y)
        self.game_board.score = 0
        self.game_board.food.value = 1
        self.game_board.food.rect.center = (random.randint(0,640),random.randint(0,480))


    #draw game
    def draw(self):
        self.screen.fill((0,0,0))
        self.game_board.draw(self.screen)
        pygame.display.flip()

    #default draw text function
    def draw_text(self, text, surface, x, y):
        textobj = self.font.render(text, 1, (0,0,0))
        textrect = textobj.get_rect()
        textrect.center = (x,y)
        surface.blit(textobj, textrect)

#start game
game = Game()
game.game_loop()



