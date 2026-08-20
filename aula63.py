t1 = int(input('Digite quantos termos voce quer mostrar: '))
aux = 0
n1 = 0
n2 = 1
while aux < t1:
    print(n2, end=' -> ')
    n2 = n1 + n2
    n1 = n2 - n1
    aux += 1



print('FIM')