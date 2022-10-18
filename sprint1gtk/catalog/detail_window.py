import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

class DetailWindow(Gtk.Window):

    def __init__(self, label, image, label2):
        super().__init__(title="Detalles")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)  ## creamos nueva bo que contendrá los datos

        self.add(box)
        box.pack_start(label, True, True, 0)  ## añadimos el titulo,imagen y descripcion enviadas desde cell.py
        box.pack_start(image, True, True, 0)
        box.pack_start(label2, True, True, 0)


