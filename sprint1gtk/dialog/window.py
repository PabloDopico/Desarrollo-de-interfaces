#Crea una carpeta llamada dialog dentro de sprint1gtk. En esa carpeta, añade el
#código del apartado 2 para mostrar una ventana con un label y un botón. Igual que
#en el ejemplo, deberá haber 2 ficheros main.py y window.py. Comprueba que
#funciona como se espera. Haz commit y push.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    button = Gtk.Button(label="Realizar acción")


    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)



    def on_button_clicked(self, widget):
        pass
