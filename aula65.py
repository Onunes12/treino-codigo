p1 = int(input('Digite um numero : '))
p2 = int(input('Digite outro numero : '))
if p1 > p2:
    print('O maior numero e {}'.format(p1))
elif p2 > p1:
    print('O maior numero e {}'.format(p2))
else:
    print(' os numers {} e {} sao iguais'.format(p1,p2))
p3 = str(input('Voce quer continuar [S/N] : ')).upper().strip()
while p3 == 'S':
    p1 = int(input('Digite um numero : '))
    p2 = int(input('Digite outro numero : '))
    if p1 > p2:
        print('O maior numero e {}'.format(p1))
    elif p2 > p1:
        print('O maior numero e {}'.format(p2))
    else:
        print(' os numeros {} e {} sao iguais'.format(p1,p2))
    p3 = str(input('Voce quer continuar [S/N] : ')).upper().strip()
