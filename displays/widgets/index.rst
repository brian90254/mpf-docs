Display widgets
===============

Display widgets are where the real action takes place in MPF-MC's display system.
They're what you (as a game programmer) interact with most often. They're the
"stuff" that shows up on a display. (Well, technically, they're the stuff that
is added to a slide, and then that slide in turn is shown on a display.) MPF
includes the following types of display widgets:

+ Text
+ Image
+ Video
+ DMD
+ Character picker
+ Entered chars
+ Bezier
+ Ellipse
+ Line
+ Point
+ Quad
+ Rectangle
+ Triangle

These widgets plug-in to MPF-MC's display system in a standard way, so it's easy
for us (or for you) to write your own widgets if you need to be able to display
something that we don't include out-of-the-box. (We also have plans for more
types of display elements, including ones to render segmented displays to the on
screen window and ones that show the current status of lights, switches, and
coils.)
