import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class SpinButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Spin Button")
        self.set_border_width(10)


        #gtk.Adjustment(value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0)
        adjustment = Gtk.Adjustment(10, 0, 100, 1, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)

        check_numeric = Gtk.CheckButton("Numeric")
        check_numeric.connect("toggled", self.on_numeric_toggled)

        check_if_valid = Gtk.CheckButton("I Valid")
        check_if_valid.connect("toggled", self.on_if_valid_toggled)
       
        grid = Gtk.Grid()
        self.add(grid)
        grid.attach(self.spinbutton, 0, 0, 1, 1)
        grid.attach(check_numeric, 0, 1, 1, 1)
        grid.attach(check_if_valid, 0, 2, 1, 1)

    def on_if_valid_toggled(self, button):
        if button.get_active():
            policy = Gtk.SpinButtonUpdatePolicy.IF_VALID
        else:
            policy = Gtk.SpinButtonUpdatePolicy.ALWAYS
        self.spinbutton.set_update_policy(policy)
            
        
    
        

    def on_numeric_toggled(self, button):
        self.spinbutton.set_numeric(button.get_active())

win = SpinButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
    
