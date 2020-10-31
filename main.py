from selenium import webdriver
from time import sleep
import pyautogui
import gui
import db


perfis = []
dados = []
dados = gui.tela_inicial()

url = dados[0]
nome_usuario = dados[1]
senha_usuario = dados[2]


options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome()
driver.get(url)
driver.fullscreen_window()
login_insta = driver.find_element_by_class_name('tdiEy')
login_insta.click()
sleep(1)
usuario = driver.find_element_by_name('username')
usuario.send_keys(nome_usuario)
sleep(2)
senha = driver.find_element_by_name('password')
senha.send_keys(senha_usuario)
sleep(1)
pyautogui.press('enter')
sleep(5)
driver.get(url)
sleep(2)
driver.fullscreen_window()
comentarios = driver.find_element_by_class_name('Ypffh')
comentarios.click()
sleep(2)

""" REFAZER
for i in perfis:
    db.cursor.execute("SELECT perfisInsta FROM perfis")
    pyautogui.write(i)
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('enter')
    sleep(5)
    comentarios = driver.find_element_by_class_name('Ypffh')
    comentarios.click()
    sleep(60)
"""
driver.close()
