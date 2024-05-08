# Importar bibliotecas
import pyautogui
import time
import pandas as pd
# Abrir sistema (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# Fazer login
    # Esperar carregar
time.sleep(3)
pyautogui.click(x=-1275, y=780)
pyautogui.write("lelemozaos2@gmail.com")
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=-1083, y=1028)
# Abrir base de dados dos produtos
tabela = pd.read_csv("produtos.csv")
# Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=-1132, y=603)
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #pega o código da tabela e escreve no campo
    pyautogui.press("tab")
    # Repetir tudo até o final da lista de produtos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)