import pyautogui
import pandas as pd
import time

#Importacao da base de dados produtos
table = pd.read_csv('produtos.csv')
print(table)