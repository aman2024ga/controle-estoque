from gerenciador_estoque import GerenciadorEstoque
from verificacoes import obter_inteiro_valido, obter_string_nao_vazia

def main():
    estoque = GerenciadorEstoque()

    while True:
        print("\n--- Sistema de Controle de Estoque ---")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Consultar Produto")
        print("6. Sair")

        opcao = obter_inteiro_valido("Escolha uma opção: ")

        if opcao == 1:
            nome = obter_string_nao_vazia("Nome do produto: ")
            quantidade = obter_inteiro_valido("Quantidade: ")
            preco = float(obter_inteiro_valido("Preço: "))
            produto = estoque.adicionar_produto(nome, quantidade, preco)
            print(f"Produto adicionado: {produto}")
        elif opcao == 2:
            produtos = estoque.listar_produtos()
            if produtos:
                print("\nProdutos no Estoque:")
                for produto in produtos:
                    print(produto)
            else:
                print("Nenhum produto no estoque.")
        elif opcao == 3:
            id = obter_inteiro_valido("ID do produto a ser atualizado: ")
            nome = obter_string_nao_vazia("Novo nome (deixe vazio para manter o atual): ")
            quantidade = input("Nova quantidade (deixe vazio para manter o atual): ")
            preco = input("Novo preço (deixe vazio para manter o atual): ")

            quantidade = int(quantidade) if quantidade else None
            preco = float(preco) if preco else None

            produto = estoque.atualizar_produto(id, nome, quantidade, preco)
            if produto:
                print(f"Produto atualizado: {produto}")
            else:
                print("Produto não encontrado.")
        elif opcao == 4:
            id = obter_inteiro_valido("ID do produto a ser excluído: ")
            if estoque.excluir_produto(id):
                print("Produto excluído com sucesso.")
            else:
                print("Produto não encontrado.")
        elif opcao == 5:
            id = obter_inteiro_valido("ID do produto: ")
            produto = estoque.buscar_produto(id)
            if produto:
                print(f"Detalhes do produto: {produto}")
            else:
                print("Produto não encontrado.")
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
