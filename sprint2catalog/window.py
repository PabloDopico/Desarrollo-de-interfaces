import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from cell import Cell


class MainWindow(Gtk.Window):  ## declaramos una ventana principal, cuya superclase es Gtk.Window
    flowbox = Gtk.FlowBox()  ## declaramos e inicializamos un componente FlowBox, para añadir elementos y reposicionarlos de acuerdo al tamaño disponible

    def __init__(self, data_source):
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

        for item in data_source:
            cell = Cell(item.get("name"), item.get("gtk_image"), item.get("description"))
            self.flowbox.add(cell)

        self.set_position(Gtk.WindowPosition.CENTER)