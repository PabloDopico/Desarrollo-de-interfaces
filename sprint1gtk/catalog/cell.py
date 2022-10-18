import gi

from catalog.detail_window import DetailWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Cell(Gtk.EventBox):
    name = None

    def __init__(self, name, imagen):
        super().__init__()
        self.name = name  ## asignamos los valores enviados desde window.py
        self.image = imagen

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

        if self.name == "Camaleón":
            label.set_text(self.name)  ## añadimos el nombre y descripción del animal a las etiquetas
            label2.set_text(
                "Pequeños saurópsidos escamosos. Famosos por su habilidad de cambiar de color según las circunstancias, por su lengua rápida y alargada, y por sus ojos, que pueden ser movidos independientemente el uno del otro.")

        elif self.name == "Conejo":
            label.set_text(self.name)
            label2.set_text(
                "Especie de mamífero lagomorfo de la familia Leporidae. Se caracteriza por tener un cuerpo cubierto de un pelaje espeso y lanudo, de color pardo pálido a gris, cabeza ovalada y ojos grandes.")

        elif self.name == "Perro":
            label.set_text(self.name)
            label2.set_text(
                "Mamífero carnívoro doméstico de la familia de los cánidos que se caracteriza por tener los sentidos del olfato y el oído muy finos, y por su fidelidad al ser humano, que lo ha domesticado desde tiempos prehistóricos; existen muchas razas y de características muy diversas.")

        elif self.name == "Pingüino":
            label.set_text(self.name)
            label2.set_text(
                "Los pingüinos son las únicas aves vivientes no voladoras adaptadas al buceo propulsado por las alas. Por ello, sus alas se han convertido en aletas con huesos fuertemente comprimidos y articulaciones rígidas que impiden el movimiento independiente de los huesos del ala")

        elif self.name == "Tiburón":
            label.set_text(self.name)
            label2.set_text(
                "Los tiburones son una superorden de condrictios (peces cartilaginosos), que se caracterizan por ser grandes depredadores, tener esqueleto cartilaginoso y boca ventral. Su piel está formada por una especie de escamas conocidas como dentículos dérmicos ")

        print("Se ha clicado la celda de " + self.name)  ## indicamos que celda ha clicado el usuario

        detwin = DetailWindow(label, image, label2)  ## mostramos la DetailWindow con los parámetros indicados previamente
        detwin.show_all()
