import os

produtos = []
produto_id = 0

# Funcção para exibir mensagem
def exibirMensagem(texto):
    print('*' * 40)
    print(texto.upper())
    print('*' * 40)

# Função para cadastra roupa
def novoCadastro():
    global produtos, produto_id
    
    nome_fabricante = input('Digite o nome do fabricate: ')
    ano_fabricacao = input('Digite o ano de fabricação: ')
    qtds = input('Quantidade: ')
    
    # Incrementando o ID de identificação do registro
    produto_id += 1
    
    produtos.insert(len(produtos), {
        'id': produto_id,
        'fabricante': nome_fabricante,
        'ano_fabricacao': ano_fabricacao,
        'quantidade': qtds
    })
    
# *****

# Função para lista os produtos cadastrados
def listarProdutos():
    global produtos
    
    exibirMensagem('Produtos Cadastrados')
    
    for produto in produtos:
        for key in produto:
            print(f'{key}: {produto[key]}')
        
        print('-' * 10)
        
# *****

# Função para apagar produto
def apagarProduto():
    global produtos
    
    produto_id = int(input('Insira a ID de identificação do produto: '))
    
    for produto in produtos:
        if produto['id'] == produto_id:
            produtos.remove(produto)
            print(f'Produto com ID {produto_id} removido com sucesso!')
            break
    else:
        print('Produto não encontrado.')
        
# *****

while True:
    exibirMensagem('Sistema de Cadastro de Roupas')
    
    print('1 - Cadastrar Roupa')
    print('2 - Listar Roupa Cadastrada')
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
        os.system('cls' if os.name == 'nt' else 'clear')
        apagarProduto()
    elif opcao == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Opção inválida!')
        continue
    
# Limpar o terminal no em multiplataforma (Windows, Linux e macOs)
os.system('cls' if os.name == 'nt' else 'clear')
