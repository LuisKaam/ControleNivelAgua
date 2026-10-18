# 💧 Controle de Níveis de Água

## Objetivo

Programa em Python que simula o monitoramento de um reservatório de água, exibindo mensagens de alerta com cores diferentes conforme o nível de água informado.

O sistema utiliza cinco níveis, desde **Muito baixo (crítico)** até **Muito alto (alerta)**.

**Linguagem utilizada:** Python

![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python)

![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-black?logo=github)

![Colorama](https://img.shields.io/badge/Colorama-Cores%20no%20terminal-blue)

## Níveis de água

- **1 - Muito baixo (crítico):** Vermelho
- **2 - Baixo:** Amarelo
- **3 - Médio:** Verde
- **4 - Alto:** Ciano
- **5 - Muito alto (alerta):** Azul

## Como funciona

O programa solicita ao usuário que informe um nível de água entre 1 e 5.

Uma função determina a cor correspondente ao nível informado, enquanto uma lista armazena as mensagens de cada situação.

O sistema verifica se o nível é válido e exibe a mensagem correspondente no terminal com a cor definida pela biblioteca Colorama.

Após a exibição, o estilo do terminal é restaurado ao padrão.

## Como executar

1. Tenha o Python instalado.
2. Instale a biblioteca Colorama com `pip install colorama`.
3. Execute o arquivo Python do projeto.
4. Digite um nível de água entre 1 e 5.
5. Confira a mensagem de alerta colorida no terminal.