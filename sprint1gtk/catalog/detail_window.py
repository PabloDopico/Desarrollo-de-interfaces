import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

class DetailWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self, titulo, image, description):
        super().__init__(title="Main")

        self.add(self.flowbox)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(image, 200, 200, False)
        image = Gtk.Image()
        image.set_from_pixbuf(pixbuf)

        labeltitulo = Gtk.Label(titulo)
        labeldescripcion = Gtk.Label(description)
        labeldescripcion = Gtk.Label(description)

        self.flowbox.add(labeltitulo)
        self.flowbox.add(image)
        self.flowbox.add(labeldescripcion)
