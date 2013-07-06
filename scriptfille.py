class ScriptFille():

	def __init__(self):
		# read file to lines
		with open('data/good morning script.mgmm') as f:  # TODO - either a given nae or rando fra file -- overloaded constrctor
   			self.script = f.readlines()

   		# we start on the first line of the script
   		self.step = 0


	def get_current_line(self):

		return self.script[self.step].split('\n')[0]


	def current_line_is_question(self):

		if self.is_last_line():
			return False

		next = self.script[self.step+1]
		next = next.split('\n')[0]

		if '.' is next:
			return True
	
		return False


	def is_last_line(self):
		if self.step+1 == len(self.script):
			return True
		return False


	def advance(self):

		if self.is_last_line():
			return 1

		self.step+=1
		return 0