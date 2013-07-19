import sys, urwid
sys.path.insert(0,'/home/user/Documents/mgmm/modules')
from decko import *

def handle_input(key):
   #next card on j
   if key in ('j', 'J'):
	shown_str = deck.next_card().get_side()
	txt = urwid.Text(('banner', shown_str), align='center')
        mapn = urwid.AttrMap(txt, 'streak')
	urwid.MainLoop.map1 = mapn

   #exit on q 
	if key in ('q', 'Q'):
		raise urwid.ExitMainLoop()



def setup_display(): 
	palette = [
	    ('banner', 'black', 'light gray'),
	    ('streak', 'black', 'dark red'),
	    ('bg', 'black', 'dark blue'),]
	
	txt = urwid.Text(('banner', shown_str), align='center')
	map1 = urwid.AttrMap(txt, 'streak')
	fill = urwid.Filler(map1)
	map2 = urwid.AttrMap(fill, 'bg')
	loop = urwid.MainLoop(map2, palette, unhandled_input=handle_input)
	loop.run()
	

deck = Deck('/home/user/Documents/mgmm/oracle/tarot.md')
shown_str = deck.get_card().get_side()
setup_display()

































































