import pygame
from constants import LENGTH, HEIGHT
from board import Board


# Sets the max fps to 60 so that there is little to no variation to 
# play from system to system
MAXFPS = 60

Window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Checkers Game")

def main():
    running = True
    clock = pygame.time.Clock()
    board = Board()

    while running:


        clock.tick(MAXFPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event .type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(Window)
        pygame.display.update()

    pygame.quit()

main()
