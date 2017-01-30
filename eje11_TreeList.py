import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from gi.repository import Pango

class MyTable(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Table")
        self.box = Gtk.Box(margin = 6, spacing = 6, orientation = Gtk.Orientation.VERTICAL)
        self.add(self.box)

        
        self.store = Gtk.ListStore(str, str, str, float)

        for i in range(10):
            
            self.treeiter = self.store.append([ str(i) , "Donald", "Knuth", 25.46])
        

        self.table = Gtk.TreeView(model=self.store)

        self.cod = Gtk.CellRendererText()
        self.cod.props.weight_set = True
        self.cod.props.weight = Pango.Weight.NORMAL

        self.col = Gtk.TreeViewColumn("Cod", self.cod, text=0)
        #self.col.set_title("efes")
        self.table.append_column(self.col)
        
        self.col = Gtk.TreeViewColumn("Name", self.cod, text=1)
        self.table.append_column(self.col)

        self.col = Gtk.TreeViewColumn("Family", self.cod, text=2)
        self.table.append_column(self.col)

        self.col = Gtk.TreeViewColumn("Size", self.cod, text=3)
        self.table.append_column(self.col)
                
  
        
        
        
        
        self.button_quit = Gtk.Button("Quit")
        self.button_quit.connect("clicked", self.on_button_quit)


        self.table.get_selection().connect("changed", self.on_changed)

        
        
        self.label = Gtk.Label()
        self.box.pack_start(self.table, True, True, 0)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.button_quit, True, True, 0)
        
        
    def on_changed(self, selection):
        (model, iter) = selection.get_selected()
        self.label.set_text("\n %s %s %s %s" %
                            (model[iter][0],  model[iter][1], model[iter][2] , model[iter][0] ))
        return True
        

        
    def on_button_quit(self, button):
        Gtk.main_quit()

    
win = MyTable()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
        

