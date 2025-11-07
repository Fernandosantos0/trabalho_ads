import os

produtos = []

# Função para cadastra roupa
def novoCadastro():
    nome_fabricante = input('Digite o nome do fabricate: ')
    ano_fabricacao = input('Digite o ano de fabricação: ')
    qtds = input('Quantidade: ')
    
    id_produto = len(produtos) + 1
    if produtos[len(produtos) - 1] < 1:
        id_produto = 1
    
    produtos.append({
        'id': id_produto,
        'frabricante': nome_fabricante,
        'ano_frabricacao': ano_fabricacao,
        'quantidade': qtds
    })
    
# *****

# Função para lista os produtos cadastrados
def listarProdutos():
    print(produtos)
    
# *****

while True:
    print('*' * 40)
    print('Sistema de Cadastro de Roupas'.upper())
    print('*' * 40)
    print('1 - Cadastrar Roupa')
    print('2 - Listar Roupas Cadastradas')
    print('3 - Apagar Cadastro')
    print('4 - Sair')
    
    opcao = input('Digite a opção: ')
    
    # Executar as funcionalidades
    if opcao == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        novoCadastro()
    elif opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        listarProdutos()
    elif opcao == '3':
        pass
    elif opcao == '4':
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Opção inválida!')
        continue
    
# Limpar o terminal no em multiplataforma (Windows, Linux e macOs)
os.system('cls' if os.name == 'nt' else 'clear')
