from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
import gui
import db
from variaveis import *

perfis = []
dados = []
dados = gui.tela_inicial()

url = dados[0]
nome_usuario = dados[1]
senha_usuario = dados[2]

# selecionando perfis do banco para uma lista
perfis = []
perfil_varrido = []
db.cursor.execute("SELECT perfil FROM perfis")
for perfil in db.cursor.fetchall():
    perfis.append(str(perfil))
# varrendo lista retirando caracteres indesejados
for p in perfis:
    item = p
    for i in ["(", "'", ",", ")"]:
        item = item.replace(i, "")
    perfil_varrido.append(item)

options = webdriver.FirefoxOptions()
options.add_argument('lang=pt-br')
try:
    driver = webdriver.Firefox(executable_path=GECKO_PATH)
    driver.implicitly_wait(3)

    driver.get(url)

    # login_insta = driver.find_element(By.CLASS_NAME, "sqdOP  L3NKy   y3zKF  ").click()

    usuario = driver.find_element(By.NAME, "username").send_keys(nome_usuario)
    senha = driver.find_element(By.NAME, "password").send_keys(senha_usuario)
    entrar = driver.find_element(By.CLASS_NAME, "sqdOP.L3NKy.y3zKF").click()
    sleep(2)
    driver.get(url)
    sleep(5)

    len_perfis = 0
    for perfil in perfil_varrido:
        len_perfis += 1
        comentarios = driver.find_element(By.CLASS_NAME, "_aao9").click()
        sleep(1)
        pyautogui.write(perfil, interval=0.2)
        sleep(0.3)
        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(0.5)
        if not len_perfis == len(perfil_varrido):
            sleep(60)
except Exception:
    driver.close()
else:
    driver.close()
