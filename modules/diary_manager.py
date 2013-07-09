class DiaryManager:

	def __init__(self, _diary_path):
		
		self.diary_path = self.get_complete_diary_path(_diary_path)

		try:
			f = open(self.diary_path, 'a')
			f.write(self.get_entry_opener())
			f.close()

		except:
			f = open(self.diary_path, 'w+')
			f.write(self.get_entry_opener())
			f.close()

	def add_machine_line(self, line):
		with open (self.diary_path, 'a') as f:
			f.write('> ' + line + '\n\n')	

	def add_human_line(self, line):
		with open (self.diary_path, 'a') as f:
			f.write(line + '\n\n\n')	

	def get_entry_opener(self):
		return '\n\n#New entry\n\n'

	def get_complete_diary_path(self, _diary_path):
		return _diary_path #+ get_timestamp()