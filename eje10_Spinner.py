import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class SpinnerWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Spinner")
        self.set_border_width(10)
        self.connect("delete-event", Gtk.main_quit)
        
        self.button = Gtk.ToggleButton("Start Spinning")
        self.button.connect("toggled", self.on_button_toggled)
        self.button.set_active(False)

        self.spinner = Gtk.Spinner()

        self.button_quit = Gtk.Button("Quit")
        self.button_quit.connect("clicked", self.on_button_quit)
        
        self.table = Gtk.Table(5, 2, True)
        self.table.attach(self.button, 0, 2, 0, 1)
        self.table.attach(self.spinner, 0, 2, 2, 3)
        self.table.attach(self.button_quit, 0, 2, 4, 5)
        
        

        self.add(self.table)
        self.show_all()

    def on_button_toggled(self, button):
        if button.get_active():
            self.spinner.start()
            self.button.set_label("Stop Spinning")
        else:
            self.spinner.stop()
            self.button.set_label("Start Spinning")
                
        
        

        
    def on_button_quit(self, button):
        Gtk.main_quit()
        


win = SpinnerWindow()
Gtk.main()
