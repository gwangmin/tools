import os
import sys

# Change before to after in file named fname.
def change_word(fname,before,after):
	con = None

	with open(fname,'r') as f:
		con = f.read()
	
	con = con.replace(before,after)

	with open(fname,'w') as f:
		f.write(con)

# Print this program's help message
def help_msg():
	print 'python '+sys.argv[0]+' [before] [after]'

if sys.argv[1] == '-h':
	help_msg()
	exit(0)

for path,dirs,files in os.walk('.'):
	for fname in files:
		if fname != sys.argv[0]:
			change_word(fname,sys.argv[1],sys.argv[2])

