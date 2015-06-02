# coding: utf-8
"""
Randomly shuffles all .mp3 files in home folder, 
then enumerates them by inserting the text
from 001_ to XXX_ at the beginning of file name.

If file has some digits at the begining - they will be removed (planned,
not present yet).

Run program inside folder containing .mp3 files you want to be
shuffled and numbered.
"""

import os
import random

def create_string_num(number, lenght):
	"""
	Creates a string representation of given int() or str() 'number',
	adding '0'-s in front of it to be given lenght.
	if number = 1 and lenght = 3 returns '001'
	"""
	if len(str(number)) == lenght:
		return str(number)
	else:
		next_number = '0'+ str(number)
		return create_string_num(next_number, lenght)
#print crt_str_num(3, 5)

def get_new_name(filename, prefix):
	if filename[-4:] == '.mp3': name = filename[:-4]
	else: name = filename

	if len(name) > 0:
		if name[0].isdigit() or name[0] in [' ', '_', '-', '.']:
			name = name[1:]
			return get_new_name(name, prefix)
		else:
			return prefix +'. '+ name + '.mp3'
	else: 
		return prefix + '.mp3'


curr_path = os.path.abspath(os.curdir)
text = 'If you want me to shuffle your .mp3 files \nin your %s \
type "yes", otherwise jast hit "Enter":\n\n>>>' %str(curr_path)
to_shuffle = raw_input(text)
all_files = os.listdir(curr_path)
#print all_files
mp3_files = []
for i in xrange(len(all_files)):
	if '.mp3' in all_files[i]:
		mp3_files.append(all_files[i])
#print mp3_files
num_mp3_files = len(mp3_files)
num_digits = len(str(num_mp3_files))

numbers_for_files = []
for num in xrange(num_mp3_files):
	numbers_for_files.append(create_string_num(num + 1, num_digits))
#print numbers_for_files

if to_shuffle == 'yes': 
	random.shuffle(numbers_for_files)
#print numbers_for_files

for i in xrange(len(mp3_files)):
	old_name = mp3_files[i]
#	new_name = numbers_for_files[i]+'_'+mp3_files[i][:-4] + '.mp3'
	new_name = get_new_name(old_name, numbers_for_files[i])
	os.rename(old_name, new_name)