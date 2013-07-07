class DiaryManager:
	def __init__(self, diary_path):
		self.diary = open(diary_path, 'rw+')
		self.diary.close()

	def add_line(self, line):
		with open (self.diary, 'w') as f:
			lines = f.read()
			lines.append(line)
			f.write(lines)
