import pygame 
from SG_snake import*

pygame.init()
bounds = (500, 500)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Hungry Snake")

block_size = 20
Snake = snake(block_size, bounds)

run = True
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  window.fill((0,0,0))
  snake.draw(pygame, window)
  pygame.display.flip()