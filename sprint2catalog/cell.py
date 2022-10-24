import gi

from detail_window import DetailWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Cell(Gtk.EventBox):
    name = None

    def __init__(self, name, imagen, description):
        super().__init__()
        self.name = name  ## asignamos los valores enviados desde window.py
        self.image = imagen
        self.description=description

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)  ## creamos nueva box que tendrá el contenido de las celdas
        box.pack_start(Gtk.Label(label=name), False, False, 0)  ## añadimos el titulo del animal
        box.pack_start(imagen, True, True, 0)  ## añadimos la imagen del animal, indicada en window.py mediante el pixbuf
        self.add(box)
        self.connect("button-release-event", self.on_click, self.image)

    def on_click(self, widget, event, imagen):  ## indicamos lo que hará el programa al pulsar el botón

        label = Gtk.Label()  ## creamos nuevas label para el titulo y descripcion
        label2 = Gtk.Label()

        image = Gtk.Image()
        image.set_from_pixbuf(self.image.get_pixbuf())  ## establecemos en la variable image la imagen obtenida mediante pixbuf


        label.set_text(self.name)  ## establecemos el nombre y descripcion del json en las etiquetas de detailwindow
        label2.set_text(self.description)

        print("Se ha clicado la celda de " + self.name)  ## indicamos que celda ha clicado el usuario

        detwin = DetailWindow(label, image, label2)  ## mostramos la DetailWindow con los parámetros indicados previamente
        detwin.show_all()
