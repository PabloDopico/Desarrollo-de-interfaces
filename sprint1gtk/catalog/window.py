import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="Catálogo")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Elementos")
        header.set_subtitle("Catálogo 2022")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)
    
        cell_one = Cell("Camaleón", Gtk.Image.new_from_file("C:\\msys64\\home\\Trabajo\\Desarrollo-de-interfaces\\sprint1gtk\\catalog\\data\\edited\\camaleonEdit.png"))
        cell_two = Cell("Conejo", Gtk.Image.new_from_file("C:\\msys64\\home\\Trabajo\\Desarrollo-de-interfaces\\sprint1gtk\\catalog\\data\\edited\\conejoEdit.png"))
        cell_three = Cell("Perro", Gtk.Image.new_from_file("C:\\msys64\\home\\Trabajo\\Desarrollo-de-interfaces\\sprint1gtk\\catalog\\data\\edited\\perroEdit.png"))
        cell_four = Cell("Pingüino", Gtk.Image.new_from_file("C:\\msys64\\home\\Trabajo\\Desarrollo-de-interfaces\\sprint1gtk\\catalog\\data\\edited\\pinguinoEdit.png"))
        cell_five = Cell("Tiburón", Gtk.Image.new_from_file("C:\\msys64\\home\\Trabajo\\Desarrollo-de-interfaces\\sprint1gtk\\catalog\\data\\edited\\tiburonEdit.png"))
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
