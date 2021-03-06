import sys, urwid
from mgmm.modules import scriptfille, diary_manager  

def question(line):
    return urwid.Pile([urwid.Edit(('machine line', line + "\n"))])


class ConversationListBox(urwid.ListBox):

    def __init__(self, script_path, diary_path):

        # set up the diary
        self.diary = diary_manager.DiaryManager(diary_path)
	
	#find the script
	self.scriptfille = scriptfille.ScriptFille(script_path)

        #set up scriptfille and take care of the first line
        q = self.scriptfille.get_current_line()
        body = urwid.SimpleFocusListWalker([question(q)])

        super(ConversationListBox, self).__init__(body)



    def advance_or_quit_script(self):
        # quit if script is done
        if self.scriptfille.advance() == 1:
            raise urwid.ExitMainLoop()
	
	#skip line if it's .
        if self.scriptfille.get_current_line() is '.':
            self.advance_or_quit_script()
	
	#detect "clear" command
	if '/clear' in self.scriptfille.get_current_line():
		self.advance_or_quit_script()
		
		line = self.scriptfille.get_current_line()	
	       
		body = urwid.SimpleFocusListWalker([question(line)])
                                                                 
                super(ConversationListBox, self).__init__(body)


    def keypress(self, size, key):
        
        pos = self.focus_position
        
        if (self.scriptfille.current_line_is_question()): ## this is broken
            key = super(ConversationListBox, self).keypress(size, key)
            if key != 'enter':
                return key
       
	if key == 'enter': 

        	# store user's response in the diary
        	response = self.focus[0].edit_text 
        	self.diary.add_human_line(response)

        	self.advance_or_quit_script()

        	# add the next line of dialogue
        	line = self.scriptfille.get_current_line()

        	# add this line of dialogue to our diary
        	self.diary.add_machine_line(line)

		# add the next question and move cursor focus
        	self.body.insert(pos + 1, question('\n' + line))
        	self.focus_position = pos + 1
