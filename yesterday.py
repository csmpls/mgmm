from datetime import datetime, timedelta 
import os, subprocess

def get_yesterday_date(today):
	return today-timedelta(days=1)	

def get_diary_filename(date):
	datestr = str(date).split(' ')[0]
	return datestr + '.md'



yesterday = get_yesterday_date(datetime.now())
print yesterday

print get_diary_filename(yesterday)


fname = '/home/user/Documents/mgmm/diary/' + get_diary_filename(yesterday)


cmd = os.environ.get('EDITOR', 'vi') + ' ' + fname
subprocess.call(cmd, shell=True)
with open(fname, 'r') as f:
	print('file open')
os.unlink(fname)
