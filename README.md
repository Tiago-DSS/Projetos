# Automação de Cadastro de Produtos com Python

Este projeto foi desenvolvido como prática de automação utilizando Python.
A ideia é automatizar um processo repetitivo: acessar um site, realizar login
e cadastrar produtos a partir de uma planilha CSV.

## O que o script faz
- Abre o navegador automaticamente
- Acessa a página de login do sistema
- Preenche e-mail e senha
- Lê os dados de produtos de um arquivo CSV
- Preenche o formulário de cadastro de produtos
- Repete o processo até acabar a lista de produtos

## Tecnologias utilizadas
- Python
- Pandas (leitura e manipulação do CSV)
- PyAutoGUI (automação das ações no navegador)

## Sobre os dados
Os dados utilizados no cadastro vêm de um arquivo CSV, contendo informações
como código do produto, marca, tipo, categoria, preço, custo e observações.

## Como executar
1. Instale as dependências:
```bash
pip install pandas pyautogui
