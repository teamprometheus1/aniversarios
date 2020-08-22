from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from dbhandling import AniversariosDB
from plyer import vibrator


# Cria a classe para Gerenciador de telas
class Manager(ScreenManager):
    pass


# Cria a tela principal e checa se há aniversários no dia de hoje
class Main(Screen):
    def on_pre_enter(self, *args):
        aniversarios = AniversariosDB()
        if aniversarios.verificar_aniversarios() != False:
            nome = aniversarios.verificar_aniversarios()[0]
            dia = aniversarios.verificar_aniversarios()[1]
            mes = aniversarios.verificar_aniversarios()[2]
            # print(f'Parabéns, {nome}!!! \nO aniversário é hoje, dia {dia}/{mes}')
            # vibrator.vibrate(10)
            # self.ids.aniversariododia.text = f'Parabéns, {nome}!!! \nO aniversário é hoje, dia {dia}/{mes}'
            self.add_widget(MDLabel(text=f'Parabéns, {nome}!!! \nO aniversário é hoje, dia {dia}/{mes}',
                                    size_hint_x=0.5))


        else:
            print('Nenhum Aniversariante hoje')



# Cria o aplicativo e retorna o Gerenciador
class LembraimeDosAniversariosApp(MDApp):

    def on_pause(self):
        return

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main())
        return sm


if __name__ == "__main__":
    lembraime = LembraimeDosAniversariosApp()
    lembraime.run()
