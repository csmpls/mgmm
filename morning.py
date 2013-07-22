# coding=utf-8
import urwid
import subprocess

from mgmm.conversation import ConversationListBox 
from mgmm.modules import diary_manager

script_path = 'morning.mgmm'
diary_path = 'diary/'


dm = diary_manager.DiaryManager(diary_path)
dm.add_header('morning')

palette = [('machine line', 'yellow,bold', 'default'),]
urwid.MainLoop(ConversationListBox.ConversationListBox(script_path, diary_path), palette).run()

#clear terminal screen after quit
subprocess.Popen('clear')
