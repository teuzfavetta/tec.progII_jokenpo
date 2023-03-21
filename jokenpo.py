from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Opções:[0]PEDRA [1]PAPEL [2]TESOURA')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-='*11)

print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
        













