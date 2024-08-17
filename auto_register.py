import pyautogui as auto
import time as t
import pandas as pd
import webbrowser
import os

tabela = pd.read_csv('produtos.csv')
auto.PAUSE = 0.5

caminho_arquivo = 'first_page.html'
webbrowser.open('file://' + os.path.realpath(caminho_arquivo))

t.sleep(1)
textbox = auto.locateCenterOnScreen('pag1img.png', confidence=0.9)
auto.click(textbox)
auto.write('nomeemail@gmail.com')
auto.press('enter')
auto.write('senhasegura')
auto.press('enter')

textbox2 = auto.locateCenterOnScreen('pag2img.png', confidence=0.9)
auto.click(textbox2)
auto.hotkey('ctrl','a')

for linha in tabela.index:
    auto.write(str(tabela.loc[linha,'codigo']))
    auto.press('enter')
    auto.write(str(tabela.loc[linha,'marca']))
    auto.press('enter')
    auto.write(str(tabela.loc[linha,'tipo']))
    auto.press('enter')
    auto.write(str(tabela.loc[linha,'categoria']))
    auto.press('enter')
    auto.write(str(tabela.loc[linha,'preco_unitario']))
    auto.press('enter')
    auto.write(str(tabela.loc[linha,'custo']))
    auto.press('enter')
    obs = str(tabela.loc[linha,'obs'])
    if (obs != 'nan'):
        auto.write(obs)
    auto.press('enter')
    auto.click(textbox2)