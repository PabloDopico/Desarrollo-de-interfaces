import gi
import self

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class labelWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="acerca del desarrollador")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label("acerca del desarrollador")
        self.add(box)
        box.pack_start(label, True, True, 0)

        self.set_position(Gtk.WindowPosition.CENTER)
