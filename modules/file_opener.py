from datetime import datetime, timedelta 
import os, subprocess, tempfile

class FileOpener:

	def get_yesterday_date(self, today):
		return today-timedelta(days=1)	

	def get_diary_filename(self, date):
		datestr = str(date).split(' ')[0]
		return datestr + '.md'

	def open_diary(self, fname):
		#read lines from the diary
		fname = '/home/user/Documents/mgmm/diary/' + fname
		
		with open(fname, 'r') as f:
			strings = f.read()
		
		#make a temp file
		(fd, path) = tempfile.mkstemp('.md')
		fp = os.fdopen(fd, 'w')
		
		#write diary's strings into it
		fp.write(strings)
		fp.close()

		#open tempfile in vi
		editor = os.getenv('EDITOR', 'vi')
		print(editor, path)
		subprocess.call('%s %s' % (editor, path), shell=True)

		with open(path, 'r') as f:
		  print(f.read())

		os.unlink(path)


	def open_yesterdays_diary(self):
		yesterday = self.get_yesterday_date(datetime.now())
		self.open_diary(self.get_diary_filename(yesterday))

	def open_todays_diary(self):
		today = datetime.now()
		self.open_diary(self.get_diary_filename(today))
