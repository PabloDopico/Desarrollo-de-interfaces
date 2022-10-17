import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="Catálogo")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15) ## declaramos la anchura
        self.set_default_size(400, 400) ## declaramos el tamaño en pixeles

        header = Gtk.HeaderBar(title="Elementos") ## indicamos el titulo que aparecerá en la cabecera de la ventana
        header.set_subtitle("Catálogo 2022") ## indicamos el subtitulo de la ventana
        header.props.show_close_button = True ## indicamos si queremos tener un botón (X) para cerrar el programa en la cabecera

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow() ## con el componente Scrolledwindow podremos scrollear verticalmente en la ventana
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC) ## indicamos políticas automáticas del scrolledwindow
        scrolled.add(self.flowbox)
        self.add(scrolled)

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/camaleon.png", 200, 200, False) ## con pixbuf asignamos la ruta y los pixeles a los que queremos reajustar la imagen
        image.set_from_pixbuf(pixbuf) ##asignamos los valores del pixbuf a la variable image
        desc1="descripcion prueba 1"

        image2 = Gtk.Image()
        pixbuf2 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/conejo.png", 200, 200, False)
        image2.set_from_pixbuf(pixbuf2)
        desc2 = "descripcion prueba 2"

        image3 = Gtk.Image()
        pixbuf3 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/perro.png", 200, 200, False)
        image3.set_from_pixbuf(pixbuf3)
        desc3 = "descripcion prueba 3"

        image4 = Gtk.Image()
        pixbuf4 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/pinguino.png", 200, 200, False)
        image4.set_from_pixbuf(pixbuf4)
        desc4 = "descripcion prueba 4"

        image5 = Gtk.Image()
        pixbuf5 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/tiburon.png", 200, 200, False)
        image5.set_from_pixbuf(pixbuf5)
        desc5 = "descripcion prueba 5"

        cell_one = Cell("Camaleón", image,desc1) ##indicamos los valores de la celda
        cell_two = Cell("Conejo", image2,desc2)
        cell_three = Cell("Perro", image3,desc3)
        cell_four = Cell("Pingüino", image4,desc4)
        cell_five = Cell("Tiburón", image5,desc5)
        self.flowbox.add(cell_one)  ## añadimos la celda a la ventana
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
