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

# selecionando perfis do banco para uma lista
perfis = []
perfilVarrido = []
db.cursor.execute("SELECT perfisInsta FROM perfis")
for perfil in db.cursor.fetchall():
    perfis.append(str(perfil))
# varrendo lista retirando caracteres indesejados
for p in perfis:
    item = p
    for i in ["(", "'", ",", ")"]:
        item = item.replace(i, "")
    perfilVarrido.append(item)

options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome()

driver.get(url)
driver.fullscreen_window()
login_insta = driver.find_element_by_class_name('tdiEy').click()
sleep(1)
usuario = driver.find_element_by_name('username').send_keys(nome_usuario)
sleep(2)

senha = driver.find_element_by_name('password').send_keys(senha_usuario)
sleep(1)

entrar = driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
sleep(5)
driver.get(url)
sleep(2)
driver.fullscreen_window()
sleep(1)

for i in perfilVarrido:

    comentarios = driver.find_element_by_class_name("X7cDz").click()
    sleep(1)
    pyautogui.write(i, interval=0.1)
    sleep(2)
    publicar = driver.find_element_by_xpath("//*[@type='submit']").click()
    sleep(60)

driver.close()
