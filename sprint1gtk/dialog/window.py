import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from dialog.no_window import No_Window
from dialog.yes_window import Yes_Window

class MainWindow(Gtk.Window):
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    buttonSI = Gtk.Button(label="Sí")
    buttonNO = Gtk.Button(label="No")
    label = Gtk.Label("¿Naciste en unos de los primeros 6 meses del año?")

    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.buttonSI.connect("clicked", self.on_button_clicked)
        self.buttonNO.connect("clicked", self.on_button_clicked2)

        # ----BOX LABEL----
        self.add(self.box)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.box2, True, True, 0)

        # ----BOX BUTTONS----
        self.add(self.box2)
        self.box2.pack_start(self.buttonSI, True, True, 0)
        self.box2.pack_start(self.buttonNO, True, True, 0)

    def on_button_clicked(self,widget):
        yeswin = Yes_Window()
        yeswin.show_all()
    def on_button_clicked2(self, widget):
        nowin = No_Window()
        nowin.show_all()



