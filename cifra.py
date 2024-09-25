# Função para criptografar ou descriptografar um texto usando a Cifra de César
def cifra_de_cesar(texto, deslocamento):
    alfabeto = "abcdefghijklmnopqrstuvwxyzàáãâéêẽèóòôõìîĩíúùûũç!?*#$%&*+=-_/@" # Alfabeto que inclui letras e alguns caracteres especiais
    resultado = ""
    
    # Para cada caractere no texto
    for caractere in texto: 
        if caractere in alfabeto: # Se o caractere estiver no alfabeto, aplica o deslocamento
            indice = alfabeto.find(caractere)
            indice = (indice - deslocamento) % len(alfabeto) # Calcula o novo índice após o deslocamento e adiciona o caractere ao resultado
            resultado += alfabeto[indice]
        else:
            resultado += caractere  # Se não estiver no alfabeto, mantém o caractere original
    return resultado

# Programa principal: exibe um menu para o usuário escolher
while True:
    print("Escolha uma opção:")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("0 - Sair")
    escolha = input("Opção: ")

    if escolha == "1":
        mensagem = input("Digite a mensagem para criptografar: ").lower()  # Criptografar: pede a mensagem e o deslocamento
        chave = int(input("Digite o deslocamento (um número entre 1 e 60): "))

        if 1 <= chave <= 60:
            mensagem_criptografada = cifra_de_cesar(mensagem, chave)  # Chama a função e mostra a mensagem criptografada
            print(f"Mensagem criptografada: {mensagem_criptografada}")
        else:
            print("Por favor, insira um valor entre 1 e 60.")

    elif escolha == "2":
        mensagem = input("Digite a mensagem para descriptografar: ").lower() # Descriptografar: pede a mensagem criptografada e o deslocamento
        chave = int(input("Digite o deslocamento (um número entre 1 e 60): "))

        if 1 <= chave <= 60:
            mensagem_descriptografada = cifra_de_cesar(mensagem, -chave) # Chama a função e mostra a mensagem descriptografada
            print(f"Mensagem descriptografada: {mensagem_descriptografada}")
        else:
            print("Por favor, insira um valor entre 1 e 60.")
    
    # Opção para sair do programa
    elif escolha == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")  # Caso o usuário escolha uma opção inválida
