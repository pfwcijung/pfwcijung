import pygame
import Othello_Board
import Othello_UI
from pygame.locals import *
from Othello_config import EMPTY_stone, WHITE_stone, BLACK_stone, player_turn, BLACK, WHITE, GREEN
pass_turn = 0
'''
BLACK = [0,0,0]
WHITE = [255,255,255]
GREEN = [192,255,192]
WHITEB = 1
BLACKB = 2
EMPTYB = 0
'''

class othello():
    def __init__(self):
        self.gui = Othello_UI.GUI()
        self.board = Othello_Board.Board()
        self.gui.show_menu(self.start)

    def start(self, *args):
        player1, player2, level = args

        self.gui.show_game()
        self.gui.update(self.board.board, 2, 2, player_turn)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()

    def re_start(self):
        for i in range(8):
            for j in range(8):
                self.boardi[i][j] = EMPTY_stone

def main():
    game = othello()
    game.run()

main()


'''
player1 = 0 #whiteplayer
player2 = 0 #blackplayer
player_turn = 1
pass_turn = 0



def init():
    global  player1, player2, player_turn, pass_turn
    player1 = 0
    player2 = 0
    player_turn = 1
    pass_turn = 0

board = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

board[3][4] = BLACKB
board[4][3] = BLACKB
board[3][3] = WHITEB
board[4][4] = WHITEB

def ready():
    while True:
        screen.fill(GREEN)

        titlemsg = font.render("How to play",True,BLACK)
        howmsg1 = font.render("판에 돌을 놓았을 때",True,BLACK)
        howmsg2 = font.render("그 돌과 기존 자신의 돌 사이에",True,BLACK)
        howmsg3 = font.render("상대의 돌이 있다면",True,BLACK)
        howmsg4 = font.render("모두 자신의 돌로 만들어",True,BLACK)
        howmsg5 = font.render("결과적으로 돌이 많은 사람이",True,BLACK)
        howmsg6 = font.render("승리하는 게임입니다.",True,BLACK)

        screen.blit(titlemsg,(230,20))
        screen.blit(howmsg1,(170,100))
        screen.blit(howmsg2,(110,140))
        screen.blit(howmsg3,(170,180))
        screen.blit(howmsg4,(140,220))
        screen.blit(howmsg5,(110,260))
        screen.blit(howmsg6,(160,300))
    
        pygame.draw.rect(screen,BLACK,[230,400,180,45],0)
        msg = font.render("Game Start",True,WHITE)
        screen.blit(msg,(240,405))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if 230 < mouse[0] < 410 and 400 < mouse[1] < 445 and click[0]:
                    start()
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

def start():
    global player1, player2, player_turn

    while True:
        screen.fill(BLACK)
        player1 = 0
        player2 = 0

        check_turn()
        check_board()
        show_score()
        push_dol()
        pass_check()
        win_check()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

        # 돌을 둘 곳 없을 때 턴 넘기게 하기
        # 8방향 검사 간결하게 만들기
        # 보드그림 새로 찾기
#턴 알려주기
def check_turn():
    global player_turn
    if player_turn == 1:
        msg1 = font.render("Turn",True,WHITE)
        msg2 = font.render("White",True,WHITE)
        screen.blit(msg1,(20,100))
        screen.blit(msg2,(10,60))
        pygame.draw.rect(screen,WHITE,[20,395,80,40],0)
        msg = font.render("PASS",True,BLACK)
        screen.blit(msg,(22,395))
        return
    else:
        msg1 = font.render("Turn",True,WHITE)
        msg2 = font.render("Black",True,WHITE)
        screen.blit(msg1,(550,100))
        screen.blit(msg2,(545,60))
        pygame.draw.rect(screen,WHITE,[545,395,80,40],0)
        msg = font.render("PASS",True,BLACK)
        screen.blit(msg,(547,395))
        return
#board에 돌 넣을 곳 확인하기
def check_board():
    for i in range(8):
        for j in range(8):
            if board[i][j] == WHITEB:
                block(blockW,i,j)
                score(WHITEB)
            elif board[i][j] == BLACKB:
                block(blockB,i,j)
                score(BLACKB)
            elif board[i][j] == EMPTYB:
                block(blockE,i,j)
#board에 돌 그림 넣기
def block(self, x, y):
    boardX = 120
    boardY = 40
    x *= 50
    y *= 50

    screen.blit(self,(boardX+x,boardY+y))
#score 계산
def score(b):
    global player1, player2
    if b == WHITEB:
        player1+=1
    elif b == BLACKB:
        player2+=1
#점수 표시
def show_score():
    TextScoreWhite = font.render(str(player1), True, WHITE)
    TextScoreBlack = font.render(str(player2), True, WHITE)
    screen.blit(TextScoreWhite,(40,200))
    screen.blit(TextScoreBlack,(580,200))
#돌 놓기
def push_dol():
    global player_turn, pass_turn
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            for i in range(8):
                for j in range(8):
                    if (120 + (i *50)) < mouse[0] < (170 + (i *50)) and (40 + (j *50)) < mouse[1] < (90 + (j *50)) and ( board[i][j] == 0 ):
                        if click[0] and player_turn == 1:
                            if check_possible(i,j,1,2):
                                pass_turn = 0
                                board[i][j] = 1
                                player_turn = 2
                        elif click[0] and player_turn == 2:
                            if check_possible(i,j,2,1):
                                board[i][j] = 2
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
#8방향 검사
def check_possible(x,y,player,opponent):
    check = False  # 놓을 수 없다고 가정
    if x > 0 and y > 0 and board[x - 1][y - 1] == opponent:  # 좌상단
        temp_x = x - 1
        temp_y = y - 1
        while temp_x >= 0 and temp_y >= 0:
            if board[temp_x][temp_y] == opponent:
                temp_x -= 1
                temp_y -= 1
            elif board[temp_x][temp_y] == player:
                check = True
                temp_x += 1
                temp_y += 1
                while board[temp_x][temp_y] == opponent:
                    board[temp_x][temp_y] = player
                    temp_x += 1
                    temp_y += 1
                break
            else:
                break
    if y > 0 and board[x][y - 1] == opponent:  # 상단
        temp_x = x
        temp_y = y - 1
        while temp_y >= 0:
            if board[temp_x][temp_y] == opponent:
                temp_y -= 1
            elif board[temp_x][temp_y] == player:
                check = True
                temp_y += 1
                while board[temp_x][temp_y] == opponent:
                    board[temp_x][temp_y] = player
                    temp_y += 1
                break
            else:
                break
    if x < 7 and y > 0 and board[x + 1][y - 1] == opponent:  # 우상단
        temp_x = x + 1
        temp_y = y - 1
        while temp_x <= 7 and temp_y >= 0:
            if board[temp_x][temp_y] == opponent:
                temp_x += 1
                temp_y -= 1
            elif board[temp_x][temp_y] == player:
                check = True
                temp_x -= 1
                temp_y += 1
                while board[temp_x][temp_y] == opponent:
                    board[temp_x][temp_y] = player
                    temp_x -= 1
                    temp_y += 1
                break
            else:
                break
    if x < 7 and board[x + 1][y] == opponent:  # 우측
        temp_x = x + 1
        temp_y = y
        while temp_x <= 7:
            if board[temp_x][temp_y] == opponent:
                temp_x += 1
            elif board[temp_x][temp_y] == player:
                check = True
                temp_x -= 1
                while board[temp_x][temp_y] == opponent:
                    board[temp_x][temp_y] = player
                    temp_x -= 1
                break
            else:
                break
    if x < 7 and y < 7 and board[x + 1][y + 1] == opponent:  # 우하단
        temp_x = x + 1
        temp_y = y + 1
        while temp_x <= 7 and temp_y <= 7:
            if board[temp_x][temp_y] == opponent:
                temp_x += 1
                temp_y += 1
            elif board[temp_x][temp_y] == player:
                check = True
                temp_x -= 1
                temp_y -= 1
                while board[temp_x][temp_y] == opponent:
                    board[temp_x][temp_y] = player
                    temp_x -= 1
                    temp_y -= 1
                break
            else:
                break
    if y < 7 and board[x][y + 1] == opponent:  # 하단
        temp_x = x
        temp_y = y + 1
        while temp_y <= 7:
            if board[temp_x][temp_y] == opponent:
                temp_y += 1
            elif board[temp_x][temp_y] == player:
                check = True
                temp_y -= 1
                while board[temp_x][temp_y] == opponent:
                    board[temp_x][temp_y] = player
                    temp_y -= 1
                break
            else:
                break
    if x > 0 and y < 7 and board[x - 1][y + 1] == opponent:  # 좌하단
        temp_x = x - 1
        temp_y = y + 1
        while temp_x >= 0 and temp_y <= 7:
            if board[temp_x][temp_y] == opponent:
                temp_x -= 1
                temp_y += 1
            elif board[temp_x][temp_y] == player:
                check = True
                temp_x += 1
                temp_y -= 1
                while board[temp_x][temp_y] == opponent:
                    board[temp_x][temp_y] = player
                    temp_x += 1
                    temp_y -= 1
                break
            else:
                break
    if x > 0 and board[x - 1][y] == opponent:  # 좌측
        temp_x = x - 1
        temp_y = y
        while temp_x >= 0:
            if board[temp_x][temp_y] == opponent:
                temp_x -= 1
            elif board[temp_x][temp_y] == player:
                check = True
                temp_x += 1
                while board[temp_x][temp_y] == opponent:
                    board[temp_x][temp_y] = player
                    temp_x += 1
                break
            else:
                break
    return check
#돌 색 바꾸기
def color_change(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE
#돌을 둘 곳이 없다면(우선 패스 4회로 설정함)
def pass_check():
    global pass_turn
    if pass_turn == 2:
        unable()
#승패 판독기1
def win_check():
    if player1 + player2 == 64:
        if player1 > player2:
            screen.fill(WHITE)
            msg = font.render("Game Over",True,BLACK)
            screen.blit(msg,(250,180))
            msg = font.render("White win",True,BLACK)
            screen.blit(msg,(255,230))
        elif player1 < player2:
            screen.fill(BLACK)
            msg = font.render("Game Over",True,WHITE)
            screen.blit(msg,(250,180))
            msg = font.render("Black win",True,WHITE)
            screen.blit(msg,(255,230))
        elif player1 == player2:
            screen.fill(BLACK)
            msg = font.render("Game Over",True,WHITE)
            screen.blit(msg,(250,180))
            msg = font.render("Draw",True,WHITE)
            screen.blit(msg,(290,230))

    show_score()
#승패 판독기2
def unable():
        if player1 > player2:
            screen.fill(WHITE)
            msg = font.render("Game Over",True,BLACK)
            screen.blit(msg,(250,180))
            msg = font.render("White win",True,BLACK)
            screen.blit(msg,(255,230))
        elif player1 < player2:
            screen.fill(BLACK)
            msg = font.render("Game Over",True,WHITE)
            screen.blit(msg,(250,180))
            msg = font.render("Black win",True,WHITE)
            screen.blit(msg,(255,230))
        elif player1 == player2:
            screen.fill(BLACK)
            msg = font.render("Game Over",True,WHITE)
            screen.blit(msg,(250,180))
            msg = font.render("Draw",True,WHITE)
            screen.blit(msg,(290,230))

        show_score()

pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
blockW = pygame.image.load("white.bmp")
blockB = pygame.image.load("black.bmp")
blockE = pygame.image.load("smallboard.bmp")
font = pygame.font.SysFont("malgungothic",30,bold=True)
pygame.display.set_caption("Othello")
pygame.display.set_icon(blockW)

ready()
'''