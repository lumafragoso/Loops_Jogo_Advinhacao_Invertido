import random
nusuario = int(input('Escolha um número entre 0 e 10, que o computador tentará adivinhar: '))
computador = random.randint(0, 10)
tentativas = 0
condicao = True
minimo = 0
maximo = 10
while condicao:
    if nusuario != computador:
        if nusuario < computador:
            print('Palpite do computador: {}'. format(computador))
            print('Menor... Tente novamente.')
            tentativas = tentativas + 1
            maximo = computador - 1
            computador = random.randint(minimo, maximo)
        elif nusuario > computador:
            print('Palpite do computador: {}'.format(computador))
            print('Maior... Tente novamente.')
            tentativas = tentativas + 1
            minimo = computador + 1
            computador = random.randint(minimo, maximo)
    elif nusuario == computador:
        tentativas = tentativas + 1
        print('Palpite do computador: {}'.format(computador))
        print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
        condicao = False
