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

        menuBar = Gtk.MenuBar()  ## creamos un menubar

        filemenu = Gtk.Menu()  ## creamos un menu
        ayuda = Gtk.MenuItem("Ayuda")  ## creamos un item para el menu
        ayuda.set_submenu(filemenu)  ## establecemos el item como submenu

        acercaDe = Gtk.MenuItem("Acerca de")  ## creamos otro item
        acercaDe.connect("button-release-event", self.on_click)  ## lo conectamos al click del ratón
        vbox = Gtk.VBox()  ## creamos una vertical box (caja vertical)
        vbox.pack_start(menuBar, False, False, 0)  ## añadimos el menú a la caja vertical
        self.add(vbox)  ## añadimos la caja
        menuBar.append(ayuda)  ## Añadimos el item al Menubar

        ###################################################

        header = Gtk.HeaderBar(title="Animales")  ## indicamos el titulo que aparecerá en la cabecera de la ventana
        header.set_subtitle("Catálogo 2022")  ## indicamos el subtitulo de la ventana
        header.props.show_close_button = True  ## indicamos si queremos tener un botón (X) para cerrar el programa en la cabecera

        self.set_titlebar(header)  ## añadimos el header

        scrolled = Gtk.ScrolledWindow()  ## con el componente ScrolledWindow podremos scrollear verticalmente en la ventana
        scrolled.set_policy(Gtk.PolicyType.NEVER,
                            Gtk.PolicyType.AUTOMATIC)  ## indicamos políticas del scrolledwindow (solo en vertical y automatico)
        scrolled.add(self.flowbox)

        self.add(vbox)  ## añadimos la caja vertical
        vbox.add(scrolled)  ## añadimos el scrolled a la caja virtual
        for item in data_source:  ## recorremos todos los items en data_source
            cell = Cell(item.get("name"), item.get("gtk_image"),
                        item.get("description"))  ## añadimos a la celda los nombres, imagenes y descripciones acumulados
            self.flowbox.add(cell)  ## añadimos la celda

        self.set_position(Gtk.WindowPosition.CENTER)  ## indicamos que la ventana debe estar centrada en pantalla

        filemenu.append(acercaDe)  ## añadimos el item acercaDe al menu

    def on_click(self, widget, event):  ## establecemos lo que hará el programa al clickar en el menú
        win = labelWindow()  ## en este caso, mostrará una nueva ventana con la etiqueta
        win.show_all()
