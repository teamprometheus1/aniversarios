import sqlite3
import json
from datetime import date

#arquivo para lidar com a base de dados


#Correlaciona o nome do mês do aniversário com o número do mês
class Meses:
    mes_por_extenso = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    mes_numeral = [_ for _ in range(1,13)]


#abre e cria a base de dados e usa a classe de Meses para correlacionar
class AniversariosDB:
    def __init__(self):
        with open("aniversariosjson.json", "r") as f:
            content = f.read()
            meses = Meses()
            for key,value in json.loads(content)[0].items():
                if value[1].lower() in meses.mes_por_extenso:
                    self.criar_database()
                    self.registrar(key, int(value[0]), int(meses.mes_por_extenso.index(value[1].lower()))+1)

    #efetivamente cria e salva a base de dados e tabela.
    def criar_database(self):
        conn = sqlite3.connect('aniversarios.db')
        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS aniversarios (_ID INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT UNIQUE, 
        dia INTEGER, mes INTEGER)''')
        conn.commit()
        conn.close()

    #registra aniversários na base de dados (vindo do arquivo JSON)
    #Permite criar um formulário para registrar novos aniversários
    def registrar(self, nome, dia, mes):

        values = nome, dia, mes
        conn = sqlite3.connect('aniversarios.db')
        c = conn.cursor()
        c.execute('''INSERT OR IGNORE INTO aniversarios (nome, dia, mes) VALUES (?,?,?)''', values)
        conn.commit()
        conn.close()

    # Verifica aniversários do dia e, caso exista, retorna os dados pertinentes

    def verificar_aniversarios(self):

        conn = sqlite3.connect("aniversarios.db")
        c = conn.cursor()
        resultado = c.execute(f'''SELECT nome FROM aniversarios WHERE dia IS {date.today().day} AND mes IS
{date.today().month}''').fetchall()

        try:

            return resultado[0][0], date.today().day, date.today().month

        except Exception:
            return False

#cria instância da classe aniversário e inicia em cascata.


# registrar = AniversariosDB()
# registrar.verificar_aniversarios()
