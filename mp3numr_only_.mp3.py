# -*- coding: utf-8 -*-

"""
Shuffles all .mp3 files in home folder,
then enumerates them by inserting the text
from 001_ to XXX_ at the beginning of file name.
If filename has some digits, '.', '-', '_' or ' '
at the begining - that digits and symbols will be removed.
Run program inside folder containing .mp3 files you want to be
shuffled and numbered.
"""

import os
import random


SYMBOLS_TO_CLEAN = [' ', '_', '-', '.']
file_extension = '.mp3'


len_file_extension = len(file_extension)


def create_string_num(number, lenght):
    """
    Creates a string representation of given int() or str() 'number',
    adding '0'-s in front of it to be given lenght.
    if number = 1 and lenght = 3 returns '001'
    """
    if len(str(number)) == lenght:
        return str(number)
    else:
        next_number = '0' + str(number)
        return create_string_num(next_number, lenght)


def get_new_name_wo_ext(filename):
    """
    Returns name of file without extension, cleans it from numbers and
    simbols from SYMBOLS_TO_CLEAN at the beginning.
    """
    if filename[- len_file_extension:] == file_extension:
        name = filename[:-len_file_extension]
    else:
        name = filename
    if len(name) > 0:
        if name[0].isdigit() or name[0] in SYMBOLS_TO_CLEAN:
            name = name[1:]
            return get_new_name_wo_ext(name)
        else:
            return name
    else:
        return ' '


curr_path = os.path.abspath(os.curdir)
text1 = 'I am going to clean filenames of your .mp3 files \n\
from starting symbols in collection %s in your %s.\n\
If you want me to number files after cleaning \
type "yes", otherwise jast hit "Enter":\n\n>>>\
' % (str(SYMBOLS_TO_CLEAN), str(curr_path))

text2 = 'If you want me to shuffle your .mp3 files \nin your %s \
type "yes", otherwise jast hit "Enter":\n\n>>>' % str(curr_path)
to_number = raw_input(text1)
to_shuffle = None

if to_number == 'yes':
    to_shuffle = raw_input(text2)

all_files = os.listdir(curr_path)
working_files = []

for i in xrange(len(all_files)):
    if (
            all_files[i].endswith('.mp3') or
            all_files[i].endswith('.Mp3') or
            all_files[i].endswith('.MP3')
            ):
        working_files.append(all_files[i])
# print working_files
num_working_files = len(working_files)
num_digits = len(str(num_working_files))

numbers_for_files = []

for num in xrange(num_working_files):
    numbers_for_files.append(create_string_num(num + 1, num_digits))

if to_shuffle == 'yes':
    random.shuffle(numbers_for_files)

new_names_wo_ext = []
for i in xrange(num_working_files):
    old_name = working_files[i]
    new_name = get_new_name_wo_ext(old_name)
    if new_name == '':
        new_names_wo_ext.append(str(i))
    else:
        new_names_wo_ext.append(new_name)

if to_number == 'yes':
    for i in xrange(num_working_files):
        old_name = working_files[i]
        new_names_wo_ext[i] = (numbers_for_files[i] +
                               '. ' + new_names_wo_ext[i])

for i in xrange(num_working_files):
    old_name = working_files[i]
    new_name = new_names_wo_ext[i] + file_extension
    try:
        os.rename(old_name, new_name)
    except WindowsError:
        new_name = new_names_wo_ext[i] + '(2)' + file_extension
        os.rename(old_name, new_name)
