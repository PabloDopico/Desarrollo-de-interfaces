import gi   ## importamos librerias
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from dialog.no_window import No_Window
from dialog.yes_window import Yes_Window

class MainWindow(Gtk.Window): ## declaramos una ventana principal, cuya superclase es Gtk.Window
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL) ## declaramos e inicializamos un componente contenedor/caja
    buttonSI = Gtk.Button(label="Sí") ## declaramos e inicializamos un atributo botón con una etiqueta en su interior
    buttonNO = Gtk.Button(label="No")
    label = Gtk.Label("¿Naciste en unos de los primeros 6 meses del año?")

    def __init__(self):
        super().__init__(title="Main") ## llamamos el constructor de la superclase
        self.connect("destroy", Gtk.main_quit) ## conectamos la señal destroy, para detener el bucle principal
        self.buttonSI.connect("clicked", self.on_button_clicked) ## conectamos la señal clicked sobre el botón
        self.buttonNO.connect("clicked", self.on_button_clicked2)

        # ----BOX LABEL----
        self.add(self.box) ## añadimos la caja a la ventana
        self.box.pack_start(self.label, True, True, 0) ## empaquetamos los componentes necesarios en la caja
        self.box.pack_start(self.box2, True, True, 0)

        # ----BOX BUTTONS----
        self.add(self.box2) ## añadimos otra  caja a la ventana
        self.box2.pack_start(self.buttonSI, True, True, 0) ## el primer atributo booleano indica si debe adaptar su posicion
        self.box2.pack_start(self.buttonNO, True, True, 0) ## y el segundo indica si debe crecer

    def on_button_clicked(self,widget): ## indicamos lo que deben hacer los botones
        yeswin = Yes_Window() ## en este caso este botón mostrará la ventana Yes_Window
        yeswin.show_all()
    def on_button_clicked2(self, widget):
        nowin = No_Window()
        nowin.show_all()



