import pygame
import Othello_Board

class Player:  # 플레이어 행동
    def __init__(self, color, turn):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.turn = turn

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                for i in range(8):
                    for j in range(8):
                        if (120 + (i *50)) < mouse[0] < (170 + (i *50)) and (40 + (j *50)) < mouse[1] < (90 + (j *50)) and ( self.board[i][j] == 0 ):
                            if click[0] and player_turn == 1:
                                if Othello_Board.check_possible(i,j,1,2):
                                    pass_turn = 0
                                    self.board[i][j] = 1
                                    player_turn = 2
                            elif click[0] and player_turn == 2:
                                if Othello_Board.check_possible(i,j,2,1):
                                    self.board[i][j] = 2
                                    player_turn = 1
                        elif 20 < mouse[0] < 100 and 395 < mouse[1] < 435:
                            if click[0] and player_turn == 1:
                                pass_turn = 0
                                pass_turn += 1
                                player_turn = 2
                        elif 545 < mouse[0] < 625 and 395 < mouse[1] < 435:
                            if click[0] and player_turn == 2:
                                pass_turn += 1
                                player_turn = 1

            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()
