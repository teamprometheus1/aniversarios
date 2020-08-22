from datetime import date

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from dbhandling import AniversariosDB, Meses
from plyer import vibrator


# Cria a classe para Gerenciador de telas
class Manager(ScreenManager):
    pass


# Cria a tela principal e checa se há aniversários no dia de hoje
class Main(Screen):
    def on_pre_enter(self, *args):
        aniversarios = AniversariosDB()
        if aniversarios.verificar_aniversarios() != False:
            self.nome = aniversarios.verificar_aniversarios()[0]
            self.dia = aniversarios.verificar_aniversarios()[1]
            self.mes = aniversarios.verificar_aniversarios()[2]
            self.mes_extenso = Meses()


        else:
            print('Nenhum Aniversariante hoje')

# Usa o label já existente no arquivo .kv

    def printar_label(self, *args):
        self.ids.aniversariododia.text = self.ids.aniversariododia.text = f'Parabéns, {self.nome}!!! \nO aniversário é hoje, dia {self.dia} de' \
                                         f' {self.mes_extenso.mes_por_extenso[self.mes-1]} de {date.today().year}'


# Cria o aplicativo e retorna o Gerenciador
class LembraimeDosAniversariosApp(MDApp):

# Função para não dar crash no android quando o aplicativo pausar
    def on_pause(self):
        return

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main())
        return sm


if __name__ == "__main__":
    lembraime = LembraimeDosAniversariosApp()
    lembraime.run()
