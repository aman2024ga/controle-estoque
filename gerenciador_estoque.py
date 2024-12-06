from produto import Produto

class GerenciadorEstoque:
    def __init__(self):
        self.__produtos = []
        self.__proximo_id = 1

    def adicionar_produto(self, nome, quantidade, preco):
        produto = Produto(self.__proximo_id, nome, quantidade, preco)
        self.__produtos.append(produto)
        self.__proximo_id += 1
        return produto

    def listar_produtos(self):
        return self.__produtos

    def buscar_produto(self, id):
        for produto in self.__produtos:
            if produto.get_id() == id:
                return produto
        return None

    def atualizar_produto(self, id, nome=None, quantidade=None, preco=None):
        produto = self.buscar_produto(id)
        if produto:
            if nome:
                produto.set_nome(nome)
            if quantidade:
                produto.set_quantidade(quantidade)
            if preco:
                produto.set_preco(preco)
            return produto
        return None

    def excluir_produto(self, id):
        produto = self.buscar_produto(id)
        if produto:
            self.__produtos.remove(produto)
            return True
        return False
