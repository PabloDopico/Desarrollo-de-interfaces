import gi ## importamos librerias GTK
gi.require_version("Gtk", "3.0") ## nos aseguramos de que importamos la versión deseada
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")  ## instanciamos un objeto de cla clase Gtk.Window
window.show() ## muestra la ventana (window) en pantalla
window.connect("destroy", Gtk.main_quit) ## detenemos el bucle principal y termina el programa
Gtk.main() ## ejecuta el bucle principal o main