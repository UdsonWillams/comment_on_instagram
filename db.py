import sqlite3

banco = sqlite3.connect("perfis.db")

cursor = banco.cursor()

# Cria o Banco de dados
try:
    cursor.execute(
        "CREATE TABLE perfis (perfil text)")
    banco.commit()
except sqlite3.OperationalError:
    pass
