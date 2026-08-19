n1 = int(input('Digite um Numero:'))
n2 = int(input('Digite outro Numero:'))
print ('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')
while True:
     escolha = 0
     while escolha < 1 or escolha > 5:
          escolha = int(input('Digite qual sera a sua escolha: '))
          if escolha < 1 or escolha > 5:
               print('Escolha invalida! escolha novamente com base na numeracao acima.')
     if escolha == 1:
          resultado = n1 + n2
          print('Voce escolheu SOMAR, e sua soma dos numeros {} e {} ficou {}!'.format(n1,n2,resultado))
     elif escolha == 2:
          resultado = n1 * n2
          print('Voce escolheu MULTIPLICAR, e sua multiplicacao dos numeros {} e {} ficou {}!'.format(n1,n2,resultado))
     elif escolha == 3:
        if n1 > n2:
            print('Voce escolheu MAIOR NUMERO, e o maior numero entre {} e {} e {}'.format(n1,n2,n1))
        elif n2 > n1:
            print('Voce escolheu o MAIOR NUMERO, e o maior numero entre {} e {} e {}'.format(n1,n2,n2))
        elif n1 == n2:
            print('Eita! parece que os dois numeros sao iguais.')
     elif escolha == 4:
        print('Voce escolheu NOVOS NUMEROS, e sera solicitado que digite novos numeros!')
        n1 = int(input('Digite um novo numero: '))
        n2 = int(input('Digite outro novo numero: '))
     elif escolha == 5:
         print('Voce escolheu SAIR DO PROGRAMA, ate a proxima!')
         break
          