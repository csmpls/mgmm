# coding=utf-8
import urwid
#import os, random
import sys, urwid

sys.path.insert(0,'/home/user/Documents/mgmm/modules')
from scriptfille import * 
#from modules/diary_manager import *

sys.path.insert(0,'/home/user/Documents/mgmm/conversation')
from ConversationListBox import * 

script_path = '/home/user/Documents/mgmm/script.mgmm'
diary_path = '/home/user/Documents/mgmm/diary/'

palette = [('I say', 'default,bold', 'default'),]
urwid.MainLoop(ConversationListBox(script_path, diary_path), palette).run()

