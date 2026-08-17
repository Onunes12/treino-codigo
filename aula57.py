sexo = input('Digite o seu sexo (M/F):').strip().upper()
while sexo not in 'MF':
    sexo = input('Nao compreendi, Digite novamente o seu sexo (M/F):').strip().upper()
if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')
