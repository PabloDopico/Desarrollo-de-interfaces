import gi  ## importamos librerias

from load_window import LoadWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = LoadWindow()
win.show_all()
Gtk.main()
