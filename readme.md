# My practical excercises for learning python with GTK

This is the way to learn python and github

## Day one

The file [eje1_myWin.py](https://github.com/fbespitia/python/blob/master/eje1_myWin.py)  contains the source codes that makes a window. All worked aparently well, but I got the next warning message: 
>eje1_myWin.py:1: PyGIWarning: Gtk was imported without specifying a version first. Use gi.require_version('Gtk', '3.0') before import to ensure that the right version gets loaded.
  from gi.repository import Gtk
True

## Day two 
The file [eje2_myWin.py](https://github.com/fbespitia/python/blob/master/eje2_myWin.py)  contains the source codes that makes a window, this example is create a personalized window with some aditional elements, as default size and position.

The insights todays were that warning messasge was fixed by adding:
```
	import gi
	gi.require_version("Gtk", "3.0")
```

By other hand, from this code the line  `self.set_position(Gtk.WindowPosition.MOUSE)` doesn't do anything.

## Day three
The file [eje3_myWin.py](https://github.com/fbespitia/python/blob/master/eje3_myWin.py) contains the source codes that makes a window with an image of Tux.

## Day four
The file [eje4_HelloGnome.py](https://github.com/fbespitia/python/blob/master/eje4_HelloGnome.py) contains the source codes that makes a windowns with a label, meanwhile in the terminar is shown the properties of label objet.

## Day five
The file [eje5_1_ContainerBox.py](https://github.com/fbespitia/python/blob/master/eje5_1_ContainersBox.py) contains the source codes that makes a windowns with two buttons in a container, these buttons are conected with a function that print on command line a messages.







