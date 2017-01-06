from gi.repository import Gtk
import sys


class MyApplication(Gtk.Application):
    def do_activate(self):
        # create a Gtk Window belonging to the application itself
        window = Gtk.Window(application=self)
        # set the title
        window.set_title("Welcome to GNOME from python")
        #The command set_position doesn't work, I don't undestand whats happened!
        window.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)
        print(window.get_resizable())
        # show the window
        window.show_all()
        
# create and run the application, exit with the value returned by
# running the program

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
