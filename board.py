import pygame

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_remaining = 12
        self.white_remaining = 12
        self.red_kings = 0
        self.white_kings = 0

    def draw_squares(self, win):
        win.fill("Black")
        #for row in range