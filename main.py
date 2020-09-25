from selenium import webdriver
from time import sleep
import pyautogui

lista_nomes = []

print("BEM VINDO AO GERADOR DE COMENTARIOS AUTOMATICOS")
print("VOCÊ PRECISA COLOCAR OS PERFILS NA LISTA DE NOMES\n")

url = str(input("DIGITE A URL: "))

nome_usuario = str(input("Digite seru usuario: "))
senha_usuario = str(input("Digite sua senha: "))

options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(executable_path=r'E:\Programação\Python\Bot de Mensagens para '
                                          r'grupo\chromedriver.exe')

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
for i in lista_nomes:
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
    sleep(5)
driver.close()
print("CRIATED BY GENERALX")
