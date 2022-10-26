import gi

from labelWindow import labelWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell


class MainWindow(Gtk.Window):  ## declaramos una ventana principal, cuya superclase es Gtk.Window
    flowbox = Gtk.FlowBox()  ## declaramos e inicializamos un componente FlowBox, para añadir elementos y reposicionarlos de acuerdo al tamaño disponible

    def __init__(self, data_source):
        super().__init__(title="Catálogo")  ## titulo de la ventana

        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)  ## declaramos la anchura del borde
        self.set_default_size(400, 400)  ## declaramos el tamaño en pixeles

        ###################################################

        menuBar = Gtk.MenuBar()

        filemenu = Gtk.Menu()
        ayuda = Gtk.MenuItem("Ayuda")
        ayuda.set_submenu(filemenu)

        acercaDe = Gtk.MenuItem("Acerca de")
        acercaDe.connect("button-release-event", self.on_click)
        vbox = Gtk.VBox()
        vbox.pack_start(menuBar, False, False, 0)
        self.add(vbox)
        menuBar.append(ayuda)
        ###################################################

        header = Gtk.HeaderBar(title="Animales")  ## indicamos el titulo que aparecerá en la cabecera de la ventana
        header.set_subtitle("Catálogo 2022")  ## indicamos el subtitulo de la ventana
        header.props.show_close_button = True  ## indicamos si queremos tener un botón (X) para cerrar el programa en la cabecera

        self.set_titlebar(header)  ## añadimos el header

        scrolled = Gtk.ScrolledWindow()  ## con el componente ScrolledWindow podremos scrollear verticalmente en la ventana
        scrolled.set_policy(Gtk.PolicyType.NEVER,
                            Gtk.PolicyType.AUTOMATIC)  ## indicamos políticas del scrolledwindow (solo en vertical y automatico)
        scrolled.add(self.flowbox)

        self.add(vbox)
        vbox.add(scrolled)
        for item in data_source:
            cell = Cell(item.get("name"), item.get("gtk_image"),
                        item.get("description"))  ## añadimos a la celda los nombres, imagenes y descripciones acumulados
            self.flowbox.add(cell)  ## añadimos la celda

        self.set_position(Gtk.WindowPosition.CENTER)

        filemenu.append(acercaDe)






    def on_click(self, widget, event):
        win = labelWindow()
        win.show_all()
