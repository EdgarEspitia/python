import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WindowRadioButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Radio Button")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing = 6)
        self.add(hbox)

        button_1 = Gtk.RadioButton.new_with_label_from_widget(None, "A")
        button_1.connect("toggled", self.on_button_toggled, "A")
        hbox.pack_start(button_1, False, False, 0)

        button_2 = Gtk.RadioButton.new_with_label_from_widget(button_1, "B")
        button_2.connect("toggled", self.on_button_toggled, "B")
        hbox.pack_start(button_2, False, False, 0)

        button_3 = Gtk.RadioButton.new_with_label_from_widget(button_1, "C")
        button_3.connect("toggled", self.on_button_toggled, "C")
        hbox.pack_start(button_3, False, False, 0)

        button_4 = Gtk.RadioButton.new_with_label_from_widget(button_1, "D")
        button_4.connect("toggled", self.on_button_toggled, "D")
        hbox.pack_start(button_4, False, False, 0)


    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was tunned", state)
            
    
        
        


win = WindowRadioButton()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
