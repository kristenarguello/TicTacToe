#escolher qual simbolo
def simb1():
    simbolo = 'null'
    valido = False
    while not valido:
        simbolo = input('Please, player 1, insert which symbol do you wanna play with (X or O)')
        simbolo = simbolo.upper()
        if simbolo == 'X' or simbolo == 'O':
            valido = True
    return simbolo

#exibir grade
def grade(jogo):
    print('   |   |   ')
    print(f' {jogo[6]} | {jogo[7]} | {jogo[8]} ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {jogo[3]} | {jogo[4]} | {jogo[5]} ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {jogo[0]} | {jogo[1]} | {jogo[2]} ')
    print('   |   |   ')

#ver se a posicao é possível
def posicao():
    posicao = 'null'
    while not posicao.isnumeric():
        posicao = input('Insert the desired position to make your move (1-9)')
    posicao = int(posicao)
    return posicao
def alcance(posicao):
    if posicao not in range(1,10):
        print('Please insert a possible position')
        return False
    return True
def vazio(posicao,ja_foi):
    if posicao in ja_foi:
        print('Please insert an unused position')
        return False
    return True

#se alguem ja ganhou
def ganhou(jogo):
    for i in [0,3,6]:
        if jogo[i]==jogo[i+1]:
            if jogo[i+1]==jogo[i+2]:
                if not jogo[i]==' ':
                    return True
    for k in [6,7,8]:
        if jogo[k]==jogo[k-3]:
            if jogo[k]==jogo[k-6]:
                if not jogo[k]==' ':
                    return True
    if jogo[0]==jogo[4]:
        if jogo[4]==jogo[8]:
            if not jogo[4]==' ':
                return True
    if jogo[6]==jogo[4]:
        if jogo[4]==jogo[2]:
            if not jogo[4]==' ':
                return True
    return False

#empate?
def velha(jogo):
    if ' ' not in jogo:
        return True
    else:
        return False

#reiniciar?
def jogar():
    valor = True
    while valor:
        resposta = input('Wanna play again? (Y or N)')
        resposta = resposta.upper()
        if resposta=='Y':
            valor = False
        elif resposta=='N':
            valor = False
    if resposta=='Y':
        return True
    else: 
        return False

global pos
global usados
global jogo
reinicia = True    
while reinicia:
    print("Let's start TicTacToe!")
    p1 = simb1()
    p2 = 'null'
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'

    jogo = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    grade([1,2,3,4,5,6,7,8,9])

    sem_ganhadores = False
    empate = False
    vez = 0
    usados = []
    while not sem_ganhadores and not empate:
        if vez%2==0:
            print("\n**Player 1's turn**\n")
        else:
            print("\n**Player 2's turn**\n")
        pos = -1
        foi = False
        while not foi:
            pos = posicao()
            foi = alcance(pos)
        while not vazio(pos,usados):
            pos = posicao()
        usados.append(pos)

        if vez%2==0:
            jogo[pos-1] = p1
        else: 
            jogo[pos-1] = p2
        grade(jogo)
        sem_ganhadores = ganhou(jogo)
        empate = velha(jogo)
        vez += 1

    if sem_ganhadores:
        if vez%2==1:
            print("Congrats Player 1! You won the game!")
        else:
            print("Congrats Player 2! You won the game!")
    elif empate:
        print("Sorry, it seems that we have a tie!")
    reinicia = jogar()
print('Thanks for playing!')
