import gi  ## importamos librerias
from catalog.window import MainWindow

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

win = MainWindow()  ## declaramos nueva variable asignada a la ventana principal
win.show_all()  ## mostramos la ventana y su contenido
Gtk.main()