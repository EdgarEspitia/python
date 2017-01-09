import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):
    # constructor for a Gtk.ApplicationWindow
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME from Python", application=app)
        self.set_default_size(200, 500)

        label = Gtk.Label(label="Hello World",
                          angle=25,
                          halign=Gtk.Align.CENTER)
        widget = Gtk.Label()
        print(dir(widget.props))
        self.add(label)

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)
        

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()
        win.set_position(Gtk.WindowPosition.CENTER)
        
    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()

exit_status = app.run(sys.argv)
sys.exit(exit_status)
