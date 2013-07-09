# coding=utf-8
import urwid
#import os, random
import sys, urwid

sys.path.insert(0,'/home/user/Documents/mgmm/modules')
from scriptfille import * 
#from modules/diary_manager import *

sys.path.insert(0,'/home/user/Documents/mgmm/conversation')
from ConversationListBox import * 
#from modules/diary_manager import *



palette = [('I say', 'default,bold', 'default'),]
urwid.MainLoop(ConversationListBox(), palette).run()

