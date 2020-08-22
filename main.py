import plyer
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel

from dbhandling import AniversariosDB
from plyer import vibrator


class Manager(ScreenManager):
    pass


class Main(Screen):
    def on_pre_enter(self, *args):
        aniversarios = AniversariosDB()
        if aniversarios.verificar_aniversarios() != False:
            nome = aniversarios.verificar_aniversarios()[0]
            dia = aniversarios.verificar_aniversarios()[1]
            mes = aniversarios.verificar_aniversarios()[2]
            print(f'Parabéns, {nome}!!! \nO aniversário é hoje, dia {dia}/{mes}')
            # vibrator.vibrate(10)
            self.add_widget(MDLabel(text=f'Parabéns, {nome}!!! \nO aniversário é hoje, dia {dia}/{mes}'))


        else:
            print('Nenhum Aniversariante hoje')


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
