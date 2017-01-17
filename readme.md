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

## Day six

It was made a window with five buttons, each one are connected with a funtion that print one formate number. And for ending the app it's used a button connected with the function quit. [eje5_2_ContainersGrid.py](https://github.com/fbespitia/python/blob/master/eje5_2_ContainersGrid.py)


## Day seven

The example was the use of list box container, and how to use a class to generate objects, as Gtk.Label and adding in the main window. [eje5_3_ListBox.py](https://github.com/fbespitia/python/blob/master/eje5_3_ListBox.py) 

## Day seven

The container StackSwitcher is an intersting and fancy container with animation.
[eje5_4_Stack.py](https://github.com/fbespitia/python/blob/master/eje5_4_Stack.py) 

## Day eight
The container Header Bar was used in order to get a window with a text entry field. Using this container appeared one problem with the title, it was solved, but the are some interrogants, such as why the title of windows is missing when the propertie "names" isn't used?, and why get error if the line ''' Gtk.Window.__init__(self, title = "Stack Demo") ''' if the line is missing? why the title doesn't have any effect?

[eje5_5_HeaderBar.py](https://github.com/fbespitia/python/blob/master/eje5_5_HeaderBar.py) 

## Day nine
The container flow box allows to put elements that it follows the size window but increasing une row.

In this example is used a button object where is changed the popertie color, but i don't understan why it doesn't work.

[eje5_6_FlowBox.py](https://github.com/fbespitia/python/blob/master/eje5_6_FlowBox.py) 


## Day ten
Using labels with formats in two columns.
[eje6_Label.py](https://github.com/fbespitia/python/blob/master/eje6_Label.py) 

