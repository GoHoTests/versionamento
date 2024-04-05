import os

goho = "A verdade está lá fora..."

def limpar_tela():
    # Verifica se o sistema operacional é Windows ou Linux/Mac
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')
# Chamada da função para limpar a tela
limpar_tela()

print("Branch Develop")
print("Branch goho")
print(f"{goho}\n\n")