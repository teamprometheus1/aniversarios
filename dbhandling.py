import sqlite3
import json
from datetime import date

class Meses:
    mes_por_extenso = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    mes_numeral = [_ for _ in range(1,13)]


class AniversariosDB:
    def __init__(self):
        with open("aniversariosjson.json", "r") as f:
            content = f.read()
            meses = Meses()
            for key,value in json.loads(content)[0].items():
                if value[1].lower() in meses.mes_por_extenso:
                    self.criar_database()
                    self.registrar(key, int(value[0]), int(meses.mes_por_extenso.index(value[1].lower()))+1)


    def criar_database(self):
        conn = sqlite3.connect('aniversarios.db')
        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS aniversarios (_ID INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT UNIQUE, 
        dia INTEGER, mes INTEGER)''')
        conn.commit()
        conn.close()


    def registrar(self, nome, dia, mes):

        values = nome, dia, mes
        conn = sqlite3.connect('aniversarios.db')
        c = conn.cursor()
        c.execute('''INSERT OR IGNORE INTO aniversarios (nome, dia, mes) VALUES (?,?,?)''', values)
        conn.commit()
        conn.close()

    def verificar_aniversarios(self):

        conn = sqlite3.connect("aniversarios.db")
        c = conn.cursor()
        resultado = c.execute(f'''SELECT nome FROM aniversarios WHERE dia IS {date.today().day+1} AND mes IS
{date.today().month}''').fetchall()

        try:

            return resultado[0][0], date.today().day, date.today().month

        except Exception:
            return False


registrar = AniversariosDB()
registrar.verificar_aniversarios()
