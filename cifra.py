# Define a função cifra_de_cesar para criptografar ou descriptografar um texto.
def cifra_de_cesar(texto, deslocamento):
    alfabeto = "abcdefghijklmnopqrstuvwxyzàáãâéêẽèóòôõìîĩíúùûũç!?*#$%&*+=-_/@" # Define o alfabeto, que inclui letras minúsculas, letras com acentos e caracteres especiais.
    resultado = ""
    
    # Loop para processar cada caractere na mensagem de entrada.
    for caractere in texto: 
        if caractere in alfabeto:# Verifica se o caractere está no alfabeto.
            indice = (alfabeto.find(caractere) + deslocamento)# Calcula o novo índice após o deslocamento e concatena o caractere correspondente.
            resultado += alfabeto[indice]
        else:
            resultado += caractere # Se o caractere não estiver no alfabeto, mantém inalterado.
    return resultado

# Loop principal que exibe um menu de opções para o usuário.
while True:
    print("Escolha uma opção:")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("0 - Sair")
    escolha = input("Opção: ")

    if escolha == "1":
        # Opção de criptografar: pede a mensagem e o deslocamento.
        mensagem = input("Digite a mensagem para criptografar: ").lower()
        chave = int(input(f"Digite o deslocamento (um número entre 1 e 60): "))

        if 1 <= chave <= 60:
            # Chama a função cifra_de_cesar para criptografar a mensagem e exibe o resultado.
            mensagem_criptografada = cifra_de_cesar(mensagem, chave)
            print(f"Mensagem criptografada: {mensagem_criptografada}")
        else:
            print(f"Por favor, insira um valor entre 1 e 60.")

    elif escolha == "2":
        # Opção de descriptografar: pede a mensagem criptografada e o deslocamento.
        mensagem = input("Digite a mensagem para descriptografar: ").lower()
        chave = int(input(f"Digite o deslocamento (um número entre 1 e 60): "))

        if 1 <= chave <= 60:
            # Chama a função cifra_de_cesar para descriptografar a mensagem e exibe o resultado.
            mensagem_descriptografada = cifra_de_cesar(mensagem, -chave)
            print(f"Mensagem descriptografada: {mensagem_descriptografada}")
        else:
            print(f"Por favor, insira um valor entre 1 e 60.")
    
    # Opção de sair do programa.
    elif escolha == "0":
        print("Encerrando o programa.")
        break
    else: # Opção inválida: exibe uma mensagem de erro.
        print("Opção inválida. Tente novamente.")
