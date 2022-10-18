import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from cell import Cell


class MainWindow(Gtk.Window):  ## declaramos una ventana principal, cuya superclase es Gtk.Window
    flowbox = Gtk.FlowBox()  ## declaramos e inicializamos un componente FlowBox, para añadir elementos y reposicionarlos de acuerdo al tamaño disponible

    def __init__(self):
        super().__init__(title="Catálogo")  ## titulo de la ventana
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)  ## declaramos la anchura del borde
        self.set_default_size(400, 400)  ## declaramos el tamaño en pixeles

        header = Gtk.HeaderBar(title="Animales")  ## indicamos el titulo que aparecerá en la cabecera de la ventana
        header.set_subtitle("Catálogo 2022")  ## indicamos el subtitulo de la ventana
        header.props.show_close_button = True  ## indicamos si queremos tener un botón (X) para cerrar el programa en la cabecera

        self.set_titlebar(header)  ## añadimos el header

        scrolled = Gtk.ScrolledWindow()  ## con el componente Scrolledwindow podremos scrollear verticalmente en la ventana
        scrolled.set_policy(Gtk.PolicyType.NEVER,
                            Gtk.PolicyType.AUTOMATIC)  ## indicamos políticas del scrolledwindow (solo en vertical y automatico)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        image = Gtk.Image()
        ## con pixbuf asignamos la ruta y los pixeles a los que queremos reajustar la imagen
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/camaleon.png", 200, 200, False)
        image.set_from_pixbuf(pixbuf)  ## asignamos los valores del pixbuf a la variable image

        image2 = Gtk.Image()
        pixbuf2 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/conejo.png", 200, 200, False)
        image2.set_from_pixbuf(pixbuf2)

        image3 = Gtk.Image()
        pixbuf3 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/perro.png", 200, 200, False)
        image3.set_from_pixbuf(pixbuf3)

        image4 = Gtk.Image()
        pixbuf4 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/pinguino.png", 200, 200, False)
        image4.set_from_pixbuf(pixbuf4)

        image5 = Gtk.Image()
        pixbuf5 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/tiburon.png", 200, 200, False)
        image5.set_from_pixbuf(pixbuf5)

        cell_one = Cell("Camaleón", image)  ## indicamos los valores de la celda (el titulo y la imagen indicada mediante el pixbuf)
        cell_two = Cell("Conejo", image2)
        cell_three = Cell("Perro", image3)
        cell_four = Cell("Pingüino", image4)
        cell_five = Cell("Tiburón", image5)

        self.flowbox.add(cell_one)  ## añadimos las celdas a la ventana
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
