class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.__id = id
        self.__nome = nome
        self.__quantidade = quantidade
        self.__preco = preco

    # Getters e Setters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def __str__(self):
        return f"Produto {self.__id}: {self.__nome} | Quantidade: {self.__quantidade} | Preço: R${self.__preco:.2f}"
