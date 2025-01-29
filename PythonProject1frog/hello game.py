

import pygame
from pygame.locals import *
from pygame import KEYDOWN, K_SPACE, K_ESCAPE
from pygame.locals import QUIT
import time
import random




size=40

class apple:
    def __init__(self,surface,length):
        self.parent_screen = surface
        self.image= pygame.image.load('resources/snake g r/apple.jpg').convert()
        self.x = size*3
        self.y = size*3
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 25) * size
        self.y = random.randint(1, 20) * size

class snake:
    def __init__(self,surface,length):
        pass
        self.length= length
        self.parent_screen = surface
        self.block = pygame.image.load('resources/snake g r/block.jpg').convert()
        self.block_x = [size]*length
        self.block_y = [size]*length
        self.direction = 'down'



    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)

    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def move_up(self):
        if self.direction != 'down':
         self.direction = 'up'

    def move_down(self):
        if self.direction != 'up':
            self.direction = 'down'

    def walk(self):
        for i in range (self.length -1,0,-1):
            self.block_x[i]=self.block_x[i-1]
            self.block_y[i]=self.block_y[i-1]

        if self.direction == 'left':
           self.block_x[0] -= 40
        if self.direction == 'right':
           self.block_x[0]  += 40
        if self.direction == 'up':
           self.block_y[0]  -= 40
        if self.direction == 'down':
           self.block_y[0]  += 40

        self.draw()

    def draw(self):

        self.parent_screen.fill((0, 54, 54))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x [i], self.block_y [i]))
        pygame.display.flip()

class game:
    def __init__(self):
        pass
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((0, 54, 54))
        self.snake = snake(self.surface,2)
        self.snake.draw()
        self.apple= apple(self.surface,1)
        self.apple.draw()



    def is_collision(self, x1, y1, x2, y2):
            if x1 >= x2 and x1 < x2 + size:
                if y1 >= y2 and y1 < y2 + size:
                    return True
            return False

            # snake colliding with itself

            for i in range(2, self.snake.length):
                if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                 raise "Collision Occured"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        self.surface.fill((0,54,54))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()


        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()





    def run(self):
         running = True

         while running:
             for event in pygame.event.get():
                if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                     running = False

                  if event.key == K_UP:
                      self.snake.move_up()


                  if event.key == K_DOWN:
                      self.snake.move_down()


                  if event.key == K_RIGHT:
                      self.snake.move_right()

                  if event.key == K_LEFT:
                      self.snake.move_left()

                elif event.type == QUIT:
                      running = False


             self.play()




             time.sleep(.3)



if __name__ == "__main__":
    game= game()
    game.run()

