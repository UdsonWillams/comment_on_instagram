import PySimpleGUI as sg
import db


def tela_inicial():

    dados = list()
    sg.theme("Reddit")
    layout = [
        [sg.Text("COMENTARIOS PARA INSTAGRAM")],
        [sg.Text("COLOQUE OS PERFIS ABAIXO E CLIQUE PARA SALVAR [NÃO ESQUEÇA DO @]")],
        [sg.InputText(key="perfisDoInsta",do_not_clear=False)], [sg.Button("registrar")],
        [sg.Text("LINK DA FOTO DO INSTA")], [sg.InputText(key="link_da_foto")],
        [sg.Text("SEU USUARIO")], [sg.InputText(key="usuario")],
        [sg.Text("SUA SENHA")], [sg.InputText(key="senha",  password_char="*")],
        [sg.Button("INICIAR")],
        [sg.Text("PARA EVITAR QUE O INSTA TRAVE O ENVIO O PADRÃO TEM 1 MINUTO DE ESPERA")],
        ]

    janela = sg.Window("Comente Instagram", layout)
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        if evento == "registrar":
            perfis = valores["perfisDoInsta"]
            if perfis != "":
                if len(perfis) >= 5 and perfis[0] == "@":
                    db.cursor.execute(
                        "INSERT INTO perfis VALUES('"+perfis+"')")
                    db.banco.commit()
                    sg.popup("PERFIL CADASTRADO")
                else:
                    sg.popup("POR FAVOR INSIRA O @ E UM PERFIL COM MAIS DE 4 LETRAS")

        if evento == "INICIAR":
            dados.append(valores["link_da_foto"])
            dados.append(valores["usuario"])
            dados.append(valores["senha"])
            break
    janela.close()
    return dados
