import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
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

        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/camaleon.png", 200, 200, False)
        image.set_from_pixbuf(pixbuf)

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


        cell_one = Cell("Camaleón", image)
        cell_two = Cell("Conejo", image2)
        cell_three = Cell("Perro", image3)
        cell_four = Cell("Pingüino", image4)
        cell_five = Cell("Tiburón", image5)
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
