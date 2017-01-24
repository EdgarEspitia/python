import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class SwitchButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Switch Button")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing = 6)
        self.add(hbox)

        switch = Gtk.Switch()
        switch.connect("notify::active", self.on_switch_activated, 1)
        switch.set_active(False)
        hbox.pack_start(switch, True, True, 0)

        switch = Gtk.Switch()
        switch.connect("notify::active", self.on_switch_activated, 2)
        switch.set_active(False)
        hbox.pack_start(switch, True, True, 0)


    def on_switch_activated(self, switch, gparm, n):
        if switch.get_active():
            state = "on"
        else:
            state = "off"
        print("Switch %d  was turned %s", (n,state))


        
    


win = SwitchButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
    
