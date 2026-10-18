## Importação da biblioteca colorama
from colorama import Fore, Style, init
# Inicializa a colorama
init()

# Pede ao usuário que insira o nível de água
nivelAlerta = int(input("Digite o nível de água (1 a 5): "))

## Definindo as mensagens para cada nível de água
mensagens = [
    "CRÍTICO: Nível de água muito baixo!",
    "ATENÇÃO: Nível de água abaixo do ideal.",
    "NORMAL: Nível de água adequado.",
    "ATENÇÃO: Nível de água elevado.",
    "ALERTA: Nível de água muito alto! Risco de transbordamento."
]


def definirCor(nivelAgua):
    if nivelAgua == 1:
        return Fore.RED
    elif nivelAgua == 2:
        return Fore.YELLOW
    elif nivelAgua == 3:
        return Fore.GREEN
    elif nivelAgua == 4:
        return Fore.CYAN
    elif nivelAgua == 5:
        return Fore.BLUE

## Checa se o nível de água está no valor certo e depois imprime a mensagem com a cor correspondente
if 1 <= nivelAlerta <= 5:
    cor = definirCor(nivelAlerta)
    mensagem = mensagens[nivelAlerta - 1]
    print(cor + mensagem + Style.RESET_ALL)
else:
    print("Nível de água inválido. Por favor, insira um valor entre 1 e 5.")
