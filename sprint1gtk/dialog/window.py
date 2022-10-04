import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from dialog.no_window import No_Window
from dialog.yes_window import Yes_Window


class MainWindow(Gtk.Window):
    #box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    #box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    #buttonNO = Gtk.Button(label="No")
    #buttonSI = Gtk.Button(label="Sí")
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    button = Gtk.Button(label="OK")
    label = Gtk.Label("blablablabla")

    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.button.connect("clicked",self.on_button_clicked)
        self.add(self.box)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.button, True, True, 0)

        #self.buttonNO.connect("clicked", Yes_Window)
        #self.buttonSI.connect("clicked", No_Window)
        #self.add(self.box2)
        #self.add(self.box)
        #self.box2.pack_start(self.label, True, True, 0)
        #self.box.pack_start(self.buttonNO, True, True, 0)
        #self.box.pack_start(self.buttonSI, True, True, 0)

    def on_button_clicked(self, widget):
        pass
