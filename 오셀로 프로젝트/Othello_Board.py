from Othello_config import BLACK_stone, EMPTY_stone, WHITE, WHITE_stone
import pygame
import Othello_UI

class Board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]

        self.board[3][4] = BLACK_stone
        self.board[4][3] = BLACK_stone
        self.board[3][3] = WHITE_stone
        self.board[4][4] = WHITE_stone
    
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

    
    #돌 개수 계산
    def count_stones(self):
        whites = 0
        blacks = 0
        emptys = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == WHITE_stone:
                    whites += 1
                elif self.board[i][j] == BLACK_stone:
                    blacks += 1
                elif self.board[i][j] == EMPTY_stone:
                    emptys += 1