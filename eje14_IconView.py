import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf

icons = ["edit-cut", "edit-paste", "edit-copy"]

class IconViewWindow(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self)
    self.set_default_size(200, 200)
    
    liststore = Gtk.ListStore(Pixbuf, str)
    iconview = Gtk.IconView.new()
    iconview.set_model(liststore)
    iconview.set_pixbuf_column(0)
    iconview.set_text_column(1)
    
    
    
    for icon in icons:
        pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
        liststore.append([pixbuf, "Label"])
        
      
    #my_icon = liststore
    #print(dir(iconview))
    
    iconview.connect("item-activated", self.on_iconview_double_clicked_edit_cut)
    
    iconview.connect("button-press-event", self.on_iconview_clicked_edit_cut)
        
    self.add(iconview)

  def on_iconview_clicked_edit_cut(self, widget, item):
    print("Icon clicked")
    
    
  def on_iconview_double_clicked_edit_cut(self, widget, path):
    print(path)
    
win = IconViewWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
