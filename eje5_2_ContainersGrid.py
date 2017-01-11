import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My window with grid")
        grid=Gtk.Grid(border_width=5)
        self.add(grid)
        widget = Gtk.Button()
        #print(dir(widget.props))
        button_1  = Gtk.Button(label="Button_1", margin=5 )
        button_1.connect("clicked", self.on_button_clicked, 1 )
        button_2  = Gtk.Button(label="Button 2", margin=5 )
        button_2.connect("clicked", self.on_button_clicked, 2 )
        button_3  = Gtk.Button(label="Button 3", margin=5 )
        button_3.connect("clicked", self.on_button_clicked, 3 )
        button_4  = Gtk.Button(label="Button 4", margin=5 )
        button_4.connect("clicked", self.on_button_clicked, 4 )
        button_5  = Gtk.Button(label="Button 5", margin=5 )
        button_5.connect("clicked", self.on_button_clicked, 5 )
        button_quit  = Gtk.Button(label="Quit", margin=5 )
        button_quit.connect("clicked", self.on_button_quit )

        grid.add(button_1)
        grid.attach(button_2, 1, 0, 2, 1)
        grid.attach_next_to(button_3, button_1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button_4, button_3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button_5, 1, 2, 1, 1)
        grid.attach_next_to(button_quit, button_5, Gtk.PositionType.RIGHT,1 ,1)
        
    def on_button_clicked(self, widget, n):
        print("Button {0:2.3f} clicked".format(n) )
        
    def on_button_quit(self, widget):
        print("Bye")
        Gtk.main_quit()
        self.destroy()
        
        
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

        
