from tkinter import *
from random import randint
from comandos import modif

janela = Tk()

telalt = 200
telarg = 445
telax = int(janela.winfo_screenwidth()/2-telarg/2)
telay = int(janela.winfo_screenheight()/2-telalt)

janela.geometry(f'{telarg}x{telalt}+{telax}+{telay}')
janela.resizable(False, False)
janela.title('Jogo da velha simples - Feito por André')
janela.iconbitmap("image/velha.ico")
turn = randint(1, 2)
dificult = 0
players = 1
decision = 0
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
pval = ('X', 'O')
tambutton = 20


def newgame():
    global board, turn
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = randint(1, 2)
    update()


def victory():
    global board, turn, pval
    if turn != 0:
        for cont in range(0, 2):
            if board[0] == cont+1 and board[1] == cont+1 and board[2] == cont+1:
                turn = 0
                vict['text'] = f'Jogador {pval[cont]} venceu'
            elif board[3] == cont+1 and board[4] == cont+1 and board[5] == cont+1:
                turn = 0
                vict['text'] = f'Jogador {pval[cont]} venceu'
            elif board[6] == cont+1 and board[7] == cont+1 and board[8] == cont+1:
                turn = 0
                vict['text'] = f'Jogador {pval[cont]} venceu'
            elif board[0] == cont+1 and board[3] == cont+1 and board[6] == cont+1:
                turn = 0
                vict['text'] = f'Jogador {pval[cont]} venceu'
            elif board[1] == cont+1 and board[4] == cont+1 and board[7] == cont+1:
                turn = 0
                vict['text'] = f'Jogador {pval[cont]} venceu'
            elif board[2] == cont+1 and board[5] == cont+1 and board[8] == cont+1:
                turn = 0
                vict['text'] = f'Jogador {pval[cont]} venceu'
            elif board[0] == cont+1 and board[4] == cont+1 and board[8] == cont+1:
                turn = 0
                vict['text'] = f'Jogador {pval[cont]} venceu'
            elif board[2] == cont+1 and board[4] == cont+1 and board[6] == cont+1:
                turn = 0
                vict['text'] = f'Jogador {pval[cont]} venceu'


def update():
    global board, turn
    if turn != 0:
        bta['text'] = f'{modif(board[0])}'
        btb['text'] = f'{modif(board[1])}'
        btc['text'] = f'{modif(board[2])}'
        btd['text'] = f'{modif(board[3])}'
        bte['text'] = f'{modif(board[4])}'
        btf['text'] = f'{modif(board[5])}'
        btg['text'] = f'{modif(board[6])}'
        bth['text'] = f'{modif(board[7])}'
        bti['text'] = f'{modif(board[8])}'
        victory()
        if turn == 1:
            turn = 2
            vez['text'] = f'Vez de jogador O'
        elif turn == 2:
            turn = 1
            vez['text'] = f'Vez de jogador X'


def oponent():
    update()


def a():
    global turn, board
    this = 0
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


def b():
    global turn, board
    this = 1
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


def c():
    global turn, board
    this = 2
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


def d():
    global turn, board
    this = 3
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


def e():
    global turn, board
    this = 4
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


def f():
    global turn, board
    this = 5
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


def g():
    global turn, board
    this = 6
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


def h():
    global turn, board
    this = 7
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


def i():
    global turn, board
    this = 8
    if board[this] == 0 and turn != 0:
        if players == 1:
            board[this] = turn
            update()
        elif turn == 1 and players == 0:
            board[this] = turn
            update()


# linhas brancas abaixo das funções

vez = Label(janela, text=f'Vez de jogador X' if turn == 1 else 'Vez de jogador O', font='Arial 20 bold')
vict = Label(janela, text=f'Jogo em andamento', font='Arial 15', fg='#FF052B')
bta = Button(janela, text='    ', command=a, font=f'Arial {tambutton}')
btb = Button(janela, text='    ', command=b, font=f'Arial {tambutton}')
btc = Button(janela, text='    ', command=c, font=f'Arial {tambutton}')
btd = Button(janela, text='    ', command=d, font=f'Arial {tambutton}')
bte = Button(janela, text='    ', command=e, font=f'Arial {tambutton}')
btf = Button(janela, text='    ', command=f, font=f'Arial {tambutton}')
btg = Button(janela, text='    ', command=g, font=f'Arial {tambutton}')
bth = Button(janela, text='    ', command=h, font=f'Arial {tambutton}')
bti = Button(janela, text='    ', command=i, font=f'Arial {tambutton}')
resbt = Button(janela, text='New Game', command=newgame, font='Arial 20', fg='#0066ff')

bta.grid(row=0, column=0)
btb.grid(row=0, column=1)
btc.grid(row=0, column=2)
btd.grid(row=1, column=0)
bte.grid(row=1, column=1)
btf.grid(row=1, column=2)
btg.grid(row=2, column=0)
bth.grid(row=2, column=1)
bti.grid(row=2, column=2)
vez.grid(row=0, column=3)
vict.grid(row=1, column=3)
resbt.grid(row=2, column=3)

janela.mainloop()
