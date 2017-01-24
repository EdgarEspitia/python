import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class LinkButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Link Button")
        self.set_border_width(10)

        button = Gtk.LinkButton("https://github.com/fbespitia/python", "Link")
        self.add(button)

`win = LinkButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
