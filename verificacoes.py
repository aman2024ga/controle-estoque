def obter_inteiro_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def obter_string_nao_vazia(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        print("A entrada não pode estar vazia. Tente novamente.")
