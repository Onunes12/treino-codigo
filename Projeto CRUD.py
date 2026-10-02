produtos = []
while True:
    print(''' 
 1 - CADASTRAR PROODUTO
 2 - CONSULTAR PRODUTO
 3 - ATUALIZAR PRODUTO
 4 - DELETAR PRODUTO
 5 - SAIR ''')
    escolha = int(input('Digite a opcao desejada: '))
    if escolha == 1:
        nome = str(input('Digite o nome do produto: '))
        preco = float(input('Digite o preco do produto: '))
        quantidade = int(input('Digite a quantidade de produtos: '))
        produto = {'nome': nome,
                   'preco': preco,
                   'quantidade': quantidade}
        produtos.append(produto)
        print('Produto cadastrado com sucesso!')
        
     









