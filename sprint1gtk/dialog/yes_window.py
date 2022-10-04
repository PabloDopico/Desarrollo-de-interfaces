import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Yes_Window(Gtk.Window):
    label = Gtk.Label("Has abierto la ventana SÍ")
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

    def __init__(self):
        super().__init__(title="YES WINDOW")
        self.add(self.box)
        self.box.pack_start(self.label, True, True, 0)
