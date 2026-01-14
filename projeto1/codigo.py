#objetivo: 
#abrir o site da empresa, preencher o email e a senha
#colocar as informações corretas dos produtos no site
#e continuar preenchendo até acabar os dados

import pandas #API para manipulação de dados
import pyautogui #API para automações
import time #API para trabalhar com tempo

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "emailinventado@gmail.com"

pyautogui.PAUSE = 1 # para dar um tempo de uma ação para outra

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=780, y=372)# clicar no campo do email
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write("senha linda")
pyautogui.press("enter")
time.sleep(1)

#pandas vai ler o arquivo csv
#tambem daria no excel: pandas.read_excel("produtos.xlsx") ou colocando o caminho completo até a planilha
tabela = pandas.read_csv("C:/projetos_programacao/vscode/teste_python/automacao-cadastro-produtos/produtos.csv") # o caminho do arquivo CSV deve ser ajustado conforme o ambiente local

#vai passar por cada linha da tabela
#a variavel linha foi criada devido o .index, se fosse coluna seria .columns
#o passo de agora é fazer com que o pyautogui cadastre os produtos no site
for linha in tabela.index:
    pyautogui.click(x=754, y=262) #clica no botão de novo produto
    codigo = tabela.loc[linha, "codigo"]
    time.sleep(0.3)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca)) 
    pyautogui.press("tab") 
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl, home") #volta para o topo da página se necessario
    time.sleep(0.5)



#resumindo o que esse código acima faz:
#lê o arquivo csv
#para cada linha do arquivo csv ele pega as informações de cada coluna
#e preenche no site da empresa

#pyautogui.hotkey("ctrl, home") É desnecessario, mas coloquei por garantia que o click sempre irá acertar no exato ponto que coloquei





