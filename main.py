import plyer
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from dbhandling import AniversariosDB
from plyer import vibrator


class Manager(ScreenManager):
    pass


class Main(Screen):
    def on_pre_enter(self, *args):
        aniversarios = AniversariosDB()
        if aniversarios.verificar_aniversarios() != False:
            print(aniversarios.verificar_aniversarios())
            vibrator.vibrate(10)


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
