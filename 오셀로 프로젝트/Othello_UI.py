import pygame
import sys
import time
import os
from pygame.transform import scale
import pygame_menu
#import Othello_Main
import Othello_Board
from pygame.locals import *
from Othello_config import EMPTY_stone, WHITE_stone, BLACK_stone, player_turn, player1, player2, BLACK, WHITE, GREEN


class GUI:
    def __init__(self):
        pygame.init()

        #color
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (192, 255, 192)
        self.GREY = (192, 192, 192)

        #display
        self.screen_size = (800, 480)
        self.board_POS = (203, 43)
        self.board = (201, 41)
        self.board_size = 400
        self.square_size = 50
        self.screen = pygame.display.set_mode(self.screen_size)

        #message
        self.font = pygame.font.SysFont("malgungothic", 30, bold=True)
        self.score_font = pygame.font.SysFont("Times New Roman", 22, bold=True)

        #image
        current_path = os.path.dirname(__file__)
        self.board_image = pygame.image.load(os.path.join(current_path, "board.bmp")).convert_alpha()
        self.empty_image = pygame.image.load(os.path.join(current_path, "smallboard.bmp")).convert_alpha()
        self.black_image = pygame.image.load(os.path.join(current_path, "black.bmp")).convert_alpha()
        self.white_image = pygame.image.load(os.path.join(current_path, "white.bmp")).convert_alpha()
        
    def show_menu(self, startg):
        self.menu = pygame_menu.Menu(300, 400, 'Othello', theme = pygame_menu.themes.THEME_GREEN)
        self.about_menu = pygame_menu.Menu("How to Play", 400, 450)
        self.menu.add_button("Play", lambda : startg(1, 2, 3) )
        self.menu.add_button(self.about_menu.get_title(), self.about_menu, False, False)
        self.menu.add_button("EXIT", pygame_menu.events.EXIT)
        self.about_menu.add.image(image_path= "test.png", angle=0, scale=(0.95, 0.95))
        self.menu.mainloop(self.screen)

    def reset_menu(self):
        self.menu.disable()
        self.menu.reset(1)

    def show_game(self):
        print("show game...")
        self.reset_menu()

        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(self.GREEN)
        self.score_size = 50
        self.score1 = pygame.Surface((self.score_size, self.score_size))
        self.score2 = pygame.Surface((self.score_size, self.score_size))
        self.screen.blit(self.background, (0, 0), self.background.get_rect())
        self.screen.blit(self.board_image, self.board_POS, self.board_image.get_rect())
        self.put_stone((3, 3), WHITE_stone)
        self.put_stone((4, 4), WHITE_stone)
        self.put_stone((3, 4), BLACK_stone)
        self.put_stone((4, 3), BLACK_stone)
        pygame.display.flip()

    #board에 돌 넣기
    def put_stone(self, pos, color):
        if pos == None:
            return

        pos = (pos[1],pos[0])

        if color == WHITE_stone:
            image = self.white_image
        elif color == BLACK_stone:
            image = self.black_image
        elif color == EMPTY_stone:
            image = self.empty_image

        x = pos[0] * self.square_size + self.board[0]
        y = pos[1] * self.square_size + self.board[1]

        self.screen.blit(image,(x,y))

    #화면 갱신
    def update(self, board, whites, blacks, player_color):
        for i in range(8):
            for j in range(8):
                if board[i][j] != EMPTY_stone:
                    self.put_stone((i,j),board[i][j])
                    
        blacks_score = '%02d ' % int(blacks)
        whites_score = '%02d ' % int(whites)
        self.show_score(blacks_score, whites_score, player_color)
        pygame.display.flip()

    #마우스 입력
    def mouse_click(self):
        global player_turn, pass_turn
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("mouse click...")
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    for i in range(8):
                        for j in range(8):
                            if (201 + (i *50)) < mouse[0] < (251 + (i *50)) and (41 + (j *50)) < mouse[1] < (91 + (j *50)) and ( self.board[i][j] == 0 ):
                                if click[0] and player_turn == 1:
                                    if self.check_possible(i,j,1,2):
                                        pass_turn = 0
                                        self.board[i][j] = 1
                                        player_turn = 2
                                elif click[0] and player_turn == 2:
                                    if self.check_possible(i,j,2,1):
                                        self.board[i][j] = 2
                                        player_turn = 1

    #턴 알려주기
    def check_turn(self):
        pass

    #score 계산
    def show_score(self, blackscore, whitescore, player_turn):
        
        #white_background
        #black_background

        WStxt = self.score_font.render(whitescore, True, self.WHITE, self.GREY)#white_background)
        BStxt = self.score_font.render(blackscore, True, self.BLACK, self.GREY)#black_background)
        self.screen.blit(WStxt,(700,40))
        self.screen.blit(BStxt,(100,40))
        

    #승리자 보여주기
    def show_winner(self):
        pass    

    def check_possible(self,x,y,player,opponent):
        check = False  # 놓을 수 없다고 가정
        if x > 0 and y > 0 and self.board[x - 1][y - 1] == opponent:  # 좌상단
            temp_x = x - 1
            temp_y = y - 1
            while temp_x >= 0 and temp_y >= 0:
                if self.board[temp_x][temp_y] == opponent:
                    temp_x -= 1
                    temp_y -= 1
                elif self.board[temp_x][temp_y] == player:
                    check = True
                    temp_x += 1
                    temp_y += 1
                    while self.board[temp_x][temp_y] == opponent:
                        self.board[temp_x][temp_y] = player
                        temp_x += 1
                        temp_y += 1
                    break
                else:
                    break
        if y > 0 and self.board[x][y - 1] == opponent:  # 상단
            temp_x = x
            temp_y = y - 1
            while temp_y >= 0:
                if self.board[temp_x][temp_y] == opponent:
                    temp_y -= 1
                elif self.board[temp_x][temp_y] == player:
                    check = True
                    temp_y += 1
                    while self.board[temp_x][temp_y] == opponent:
                        self.board[temp_x][temp_y] = player
                        temp_y += 1
                    break
                else:
                    break
        if x < 7 and y > 0 and self.board[x + 1][y - 1] == opponent:  # 우상단
            temp_x = x + 1
            temp_y = y - 1
            while temp_x <= 7 and temp_y >= 0:
                if self.board[temp_x][temp_y] == opponent:
                    temp_x += 1
                    temp_y -= 1
                elif self.board[temp_x][temp_y] == player:
                    check = True
                    temp_x -= 1
                    temp_y += 1
                    while self.board[temp_x][temp_y] == opponent:
                        self.board[temp_x][temp_y] = player
                        temp_x -= 1
                        temp_y += 1
                    break
                else:
                    break
        if x < 7 and self.board[x + 1][y] == opponent:  # 우측
            temp_x = x + 1
            temp_y = y
            while temp_x <= 7:
                if self.board[temp_x][temp_y] == opponent:
                    temp_x += 1
                elif self.board[temp_x][temp_y] == player:
                    check = True
                    temp_x -= 1
                    while self.board[temp_x][temp_y] == opponent:
                        self.board[temp_x][temp_y] = player
                        temp_x -= 1
                    break
                else:
                    break
        if x < 7 and y < 7 and self.board[x + 1][y + 1] == opponent:  # 우하단
            temp_x = x + 1
            temp_y = y + 1
            while temp_x <= 7 and temp_y <= 7:
                if self.board[temp_x][temp_y] == opponent:
                    temp_x += 1
                    temp_y += 1
                elif self.board[temp_x][temp_y] == player:
                    check = True
                    temp_x -= 1
                    temp_y -= 1
                    while self.board[temp_x][temp_y] == opponent:
                        self.board[temp_x][temp_y] = player
                        temp_x -= 1
                        temp_y -= 1
                    break
                else:
                    break
        if y < 7 and self.board[x][y + 1] == opponent:  # 하단
            temp_x = x
            temp_y = y + 1
            while temp_y <= 7:
                if self.board[temp_x][temp_y] == opponent:
                    temp_y += 1
                elif self.board[temp_x][temp_y] == player:
                    check = True
                    temp_y -= 1
                    while self.board[temp_x][temp_y] == opponent:
                        self.board[temp_x][temp_y] = player
                        temp_y -= 1
                    break
                else:
                    break
        if x > 0 and y < 7 and self.board[x - 1][y + 1] == opponent:  # 좌하단
            temp_x = x - 1
            temp_y = y + 1
            while temp_x >= 0 and temp_y <= 7:
                if self.board[temp_x][temp_y] == opponent:
                    temp_x -= 1
                    temp_y += 1
                elif self.board[temp_x][temp_y] == player:
                    check = True
                    temp_x += 1
                    temp_y -= 1
                    while self.board[temp_x][temp_y] == opponent:
                        self.board[temp_x][temp_y] = player
                        temp_x += 1
                        temp_y -= 1
                    break
                else:
                    break
        if x > 0 and self.board[x - 1][y] == opponent:  # 좌측
            temp_x = x - 1
            temp_y = y
            while temp_x >= 0:
                if self.board[temp_x][temp_y] == opponent:
                    temp_x -= 1
                elif self.board[temp_x][temp_y] == player:
                    check = True
                    temp_x += 1
                    while self.board[temp_x][temp_y] == opponent:
                        self.board[temp_x][temp_y] = player
                        temp_x += 1
                    break
                else:
                    break
        return check
