# coding: utf-8
"""
Randomly shuffles all .mp3 files in home folder, 
then enumerates them by inserting the text
from 001_ to XXX_ at the beginning of file name.
If file has some digits at the begining - they will be removed.

Run program inside folder that contains .mp3 files you want to
shuffle and enumerate.
"""
import os
import random

def crt_str_num(number, lenght):
	"""
	Creates a string representation of given int() or str() 'number',
	adding '0'-s in front of it to be given lenght.
	if number = 1 and lenght = 3 returns '001'
	"""
	if len(str(number)) == lenght:
		return str(number)
	else:
		next_number = '0'+ str(number)
		return crt_str_num(next_number, lenght)

print crt_str_num(3, 5)

curr_path = os.path.abspath(os.curdir)
text = 'If you want me to shuffle your .mp3 files \n in your %s \
type "yes":\n\n\n' %str(curr_path)
to_shaffle = raw_input(text)
curr_path = os.path.abspath(os.curdir)
all_files = os.listdir(curr_path)
print all_files
mp3_files = []
for i in xrange(len(all_files)):
	if '.mp3' in all_files[i]:
		mp3_files.append(all_files[i])
print mp3_files
num_mp3_files = len(mp3_files)

num_digits = len(str(num_mp3_files))

numbers_for_files = []

if to_shaffle == 'yes': 
	pass