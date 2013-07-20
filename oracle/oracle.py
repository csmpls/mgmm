import sys, urwid
from mgmm.modules import decko 





deck = decko.Deck('tarot.md')
shown_str = deck.get_card().get_side()


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

    if key in ('j', 'J'):
    	shown_str = deck.next_card().get_side()
    	txt.set_text(shown_str)

    if key in ('k', 'K'):
    	shown_str = deck.prev_card().get_side()
    	txt.set_text(shown_str)
    
    if key in ('h','H'):
    	shown_str = deck.get_card().flip_left()
    	txt.set_text(shown_str)
    
    if key in ('l','L'):
    	shown_str = deck.get_card().flip_right()
    	txt.set_text(shown_str)

palette = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06'),]

#setup
placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(placeholder, 'bg')
loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

# setup the attributes
div = urwid.Divider()
outside = urwid.AttrMap(div, 'outside')
inside = urwid.AttrMap(div, 'inside')
txt = urwid.Text(('banner', shown_str), align='center')
streak = urwid.AttrMap(txt, 'streak')

# add the attributes to a pile
pile = loop.widget.base_widget # .base_widget skips the decorations
for item in [outside, inside, streak, inside, outside]:
    pile.contents.append((item, pile.options()))

loop.run()































































