import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Yes_Window(Gtk.Window):
    label = Gtk.Label("Has abierto la ventana SÍ")

    def __init__(self,name):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)

    def on_button_clicked(self, widget):
        pass

