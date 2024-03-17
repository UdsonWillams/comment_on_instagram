import PySimpleGUI as simple_gui
from app.db import AppDB

class InitialScreen:

    def __init__(self) -> None:
        self.db = AppDB()
        self.window = simple_gui

    def make_initial_window(self):
        dados = list()
        self.window.theme("Reddit")
        layout = self.make_layout()
        window = self.window.Window("Comentando no Instagram", layout)

        while True:
            event, event_values = window.read()
            if event == self.window.WIN_CLOSED:
                break
            if event == "register":
                profile = event_values["instagram_profile"]
                if profile != "":
                    if self.validate_profile_name(profile):
                        if self.db.create_instagram_profile():
                            self.window.popup("PERFIL CADASTRADO")
                        else:
                            self.window.popup("ERRO AO CADASTRAR PERFIL, TENTE NOVAMENTE!")
                    else:
                        self.window.popup("POR FAVOR INSIRA O @ E UM PERFIL COM MAIS DE 4 LETRAS")

            if event == "INICIAR":
                dados.append(event_values["picture_link"])
                dados.append(event_values["user"])
                dados.append(event_values["senha"])
                break        
        window.close()
        return dados

    def validate_profile_name(self, profile: str) -> bool:
        try:
            assert len(profile) >= 5 
            assert profile[0] == "@"
            return True
        except AssertionError:
            return False

    def make_layout(self):
        return [
            [self.window.Text("COMENTARIOS PARA INSTAGRAM")],
            [self.window.Text("COLOQUE OS profile ABAIXO E CLIQUE PARA SALVAR [NÃO ESQUEÇA DO @]")],
            [self.window.InputText(key="instagram_profile",do_not_clear=False)], [self.window.Button("register")],
            [self.window.Text("LINK DA FOTO DO INSTAGRAM")], [self.window.InputText(key="picture_link")],
            [self.window.Text("SEU USUARIO")], [self.window.InputText(key="user")],
            [self.window.Text("SUA SENHA")], [self.window.InputText(key="password",  password_char="*")],
            [self.window.Button("INICIAR")],
            [self.window.Text("PARA EVITAR QUE O INSTAGRAM TRAVE O ENVIO O PADRÃO TEM 1 MINUTO DE ESPERA")],
        ]
