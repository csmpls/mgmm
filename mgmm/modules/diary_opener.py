from datetime import datetime, timedelta 
import os, subprocess

class DiaryOpener:

	def get_yesterday_date(self, today):
		return today-timedelta(days=3)	

	def get_diary_filename(self, date):
		datestr = str(date).split(' ')[0]
		return datestr + '.md'

	def open_diary(self, fname):
		fname = '../diary/' + fname
		cmd = os.environ.get('EDITOR', 'vi') + ' ' + fname
		subprocess.call(cmd, shell=True)
		
		with open(fname, 'w') as f:
			strings = f.read()
			f.write(strings)

		os.unlink(fname)

	def open_yesterdays_diary(self):
		yesterday = self.get_yesterday_date(datetime.now())
		self.open_diary(self.get_diary_filename(yesterday))

	def open_todays_diary(self):
		today = datetime.now()
		self.open_diary(self.get_diary_filename(today))