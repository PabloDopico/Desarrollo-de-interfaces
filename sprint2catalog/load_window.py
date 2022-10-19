import gi
import requests,threading,shutil
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib

from window import MainWindow

class LoadWindow(Gtk.Window):
    label = Gtk.Label("Cargando elementos...")  ## declaramos una etiqueta
    spinner = Gtk.Spinner() ## declaramos un componente spinner (círculo de carga)
    box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20) ## declaramos una caja

    def __init__(self):
        super().__init__(title="")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(60) ## indicamos el borde
        self.set_resizable(False) ## indicamos si la ventana sera reajustable
        self.spinner.props.active = True ## activamos el spinner

        self.box.pack_start(self.label, False, False, 0) ## añadimos label y spinner a la caja
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)
        self.launch_load() ## iniciamos el metodo launch_load

    def start_main_window(self,loaded_itemos_list):
        win=MainWindow(loaded_itemos_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main.quit)
        self.close()
    def launch_load(self): ## método para realizar hilos secundarios
        thread = threading.Thread(target=self.load_json, args=())
        thread.start()

    def load_json(self):
        response = requests.get('https://raw.githubusercontent.com/PabloDopico/Desarrollo-de-interfaces/main/catalog.json')
        json_list = response.json()

        result = [] ## inicializamos una lista para guardar los resultados

        for json_item in json_list:  ## recorremos los elementos de la lista
            name = json_item.get("name")  ## almacenamos en las 3 variables los valores del json
            description = json_item.get("description")
            image_url = json_item.get("image_url")
            r = requests.get(image_url,stream=True)  ## descargamos la imagen
            with open("temp.png",'wb') as f:
                shutil.copyfileobj(r.raw, f)  ## convertimos la imagen en un archivo temporal
            image = Gtk.Image.new_from_file("temp.png")  ## creamos un Gtk.Image para almacenar la imagen
            result.append({"name": name, "description":description,"gtk_image":image})  ## añadimos los valores almacenados a un diccionario en la lista shutil
        GLib.idle_add(self.start_main_window,result)