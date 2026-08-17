import random
cont = 0
random.randint(0, 10)
rd = random.randint(0, 10)
num = -1
while num != rd:
    num = int(input('Digite um numero de 0 a 10: '))
    if num == rd:
        print('Parabens, voce acertou o numero!!')
        print('voce tentou {} vezes ate acertar o numero'.format(cont))
    else:
        print('Voce errou, o numero correto era {}, tente novamente!'.format(rd))
        cont += 1
        print('Voce ja tentou {} vezes'.format(cont))
