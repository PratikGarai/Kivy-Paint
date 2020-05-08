from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config 

Config.set('graphics','height',400)
Config.set('graphics','width',500)

Builder.load_file('comicwidgets.kv')
Builder.load_file('comiccreator.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('toolbox.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('generaloptions.kv')

class ComicCreator(AnchorLayout):
    pass

class ComicCreatorApp(App):
    def build(self):
        return ComicCreator()


ComicCreatorApp().run()
