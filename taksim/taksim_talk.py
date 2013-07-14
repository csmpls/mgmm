# coding=utf-8
import urwid
import subprocess
import sys, urwid

sys.path.insert(0,'/home/user/Documents/mgmm/modules')
from scriptfille import * 
sys.path.insert(0,'/home/user/Documents/mgmm/conversation')
from ConversationListBox import * 

script_path = '/home/user/Documents/mgmm/taksim.mgmm'
diary_path = '/home/user/Documents/mgmm/taksim/'

palette = [('machine line', 'yellow,bold', 'default'),]
urwid.MainLoop(ConversationListBox(script_path, diary_path), palette).run()

#clear terminal screen after quit
subprocess.Popen('clear')
