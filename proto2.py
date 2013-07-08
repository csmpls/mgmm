# coding=utf-8
import urwid
import os, random

import sys
sys.path.insert(0,'/home/user/Documents/mgmm/modules')
from scriptfille import * 
#from modules/diary_manager import *

def question(line):
    return urwid.Pile([urwid.Edit(('I say', line + "\n"))])

class ConversationListBox(urwid.ListBox):
    
    #diary = DiaryManager(self,'/home/user/diary.txt')
 
    scriptfille = ScriptFille('/home/user/Documents/mgmm/conversation/data')

    def __init__(self):

        #setup; scriptfille and take care of the first line
	q = self.scriptfille.get_current_line()
        body = urwid.SimpleFocusListWalker([question(q)])

        super(ConversationListBox, self).__init__(body)



    def advance_or_quit_script(self):
        # quit if script is done
        if self.scriptfille.advance() == 1:
            raise urwid.ExitMainLoop()

        if self.scriptfille.get_current_line() is '.':
            self.advance_or_quit_script()



    def keypress(self, size, key):
        
        pos = self.focus_position
        
        if (self.scriptfille.current_line_is_question()): ## this is broken
            key = super(ConversationListBox, self).keypress(size, key)
            if key != 'enter':
                return key
        

        # later, this will get stored in a diary.... not right now, though
        response = self.focus[0].edit_text 

        self.advance_or_quit_script()

        # add the next line of dialogue
        line = self.scriptfille.get_current_line()
        line = "\n" + line

        #if (self.scriptfille.current_line_is_question()):
        self.body.insert(pos + 1, question(line))
        self.focus_position = pos + 1
        #else:
        #    self.focus.contents[1:] = [(dialogue(line), self.focus.options())]




palette = [('I say', 'default,bold', 'default'),]
urwid.MainLoop(ConversationListBox(), palette).run()

