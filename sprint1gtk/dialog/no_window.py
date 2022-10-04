import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class No_Window(Gtk.Window):
    label = Gtk.Label("Has abierto la ventana NO")
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

    def __init__(self):
        super().__init__(title="NO WINDOW")
        self.add(self.box)
        self.box.pack_start(self.label, True, True, 0)
