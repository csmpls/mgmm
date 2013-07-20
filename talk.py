# coding=utf-8
import urwid
import subprocess

from mgmm.conversation import ConversationListBox 

script_path = 'script.mgmm'
diary_path = 'diary/'

palette = [('machine line', 'yellow,bold', 'default'),]
urwid.MainLoop(ConversationListBox.ConversationListBox(script_path, diary_path), palette).run()

#clear terminal screen after quit
subprocess.Popen('clear')
