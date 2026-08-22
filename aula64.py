nu = int(input('Digite um numero [999 para parar]: '))
soma = 0 
cont = 0
while nu != 999:
    soma += nu
    cont += 1
    nu = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))