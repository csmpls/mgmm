# coding=utf-8
import urwid
import subprocess
import sys, urwid

sys.path.insert(0,'/home/user/Documents/mgmm/conversation')
from ConversationListBox import * 
#from modules/diary_manager import *

script_path = '/home/user/Documents/mgmm/script.mgmm'
diary_path = '/home/user/Documents/mgmm/diary/'

palette = [('machine line', 'yellow,bold', 'default'),]
urwid.MainLoop(ConversationListBox(script_path, diary_path), palette).run()

#clear terminal screen after quit
subprocess.Popen('clear')
