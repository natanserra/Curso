
import random


numero_aleatorio = random.randint(1, 10)

vidas = 0

while vidas < 5:
    usuario = int(input('Escolha um numero de 1 a 10: '))

if usuario == numero_aleatorio:
    print('Parabéns, voce acertou!!!')


vidas += 1

if vidas < 5:
    if usuario < numero_aleatorio:
        print('Seu numero é menor, tente novamente! ')
    else:
        print('Seu numero é maior, tente novamente! ')

if vidas == 5:
    print('Game over, o numero aleatorio é', numero_aleatorio)
