# -*- coding: utf-8 -*-
"""
Randomly shuffles user defined files in home folder,
then enumerates them by inserting the text
from '001. ' to 'XXX. ' at the beginning of file name.

If filename has some digits, '.', '-', '_' or ' '
at the begining - that digits and symbols will be removed.

Run program inside folder containing files you want to be
shuffled and numbered.
"""

import os
import random
import string
# import unidecode


SYMBOLS_TO_CLEAN = [' ', '_', '-', '.']


transliter = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
            'е': 'ye', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
            'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
            'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
            'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'А': 'A',
            'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
            'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L',
            'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
            'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'TS', 'Ч': 'CH',
            'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
            'Ю': 'yu', 'Я': 'YA'
            }


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


def transliterate(list_names):  # !!! not working yet
    res_names_list = []
    for name in list_names:
        res_name = ''
        for ch in name:
            s = r'%s' % ch
            print ch, s
            if ch in string.printable:
                res_name += ch
            elif ch in transliter.keys():
                print '1', transliter[ch]
                res_name += transliter[ch]
            else:
                res_name += '_'
        res_names_list.append(res_name)
    return res_names_list

curr_path = os.path.abspath(os.curdir)
text_1 = '\n\nI am going to work with filenames in your\n %s \n \
Please input extension of files you would like me to work with\n \
(Type .mp3 , for an instance.) :\n\n>>>' % str(curr_path)
file_extension = raw_input(text_1)
len_file_extension = len(file_extension)

# temporary, while transliteration doesn't work
to_trliter = None
# text_2 = '\n\nTo transliterate filenames of your %s files in your\n %s \n \
# type "yes", otherwise just hit "Enter":\n\n>>>\
# ' % (file_extension, str(curr_path))
# to_trliter = raw_input(text_2)


text_3 = '\n\nTo number your %s files in your\n %s \n \
type "yes", otherwise just hit "Enter":\n\n>>>\
' % (file_extension, str(curr_path))
to_number = raw_input(text_3)

to_shuffle = None



all_files = os.listdir(curr_path)
# print all_files
working_files = []
for i in xrange(len(all_files)):
    if all_files[i].endswith(file_extension):
        working_files.append(all_files[i])
# print working_files
num_working_files = len(working_files)
num_digits = len(str(num_working_files))

if to_number == 'yes':

    text_4 = '\n\nTo shuffle your %s files in your\n %s \n \
    type "yes", otherwise just hit "Enter":\n\n>>>\
    ' % (file_extension, str(curr_path))
    to_shuffle = raw_input(text_4)

    numbers_for_files = []
    for num in xrange(num_working_files):
        numbers_for_files.append(create_string_num(num + 1, num_digits))
# print numbers_for_files

if to_shuffle == 'yes':
    random.shuffle(numbers_for_files)
# print numbers_for_files

new_names_wo_ext = []
for i in xrange(num_working_files):
    old_name = working_files[i]
#   new_name = numbers_for_files[i]+'_'+mp3_files[i][:-4] + '.mp3'
#   new_name = get_new_name(old_name, numbers_for_files[i])
    new_name = get_new_name_wo_ext(old_name)
    if new_name == ' ':
        new_names_wo_ext.append(str(i))
    else:
        new_names_wo_ext.append(new_name)

if to_trliter == 'yes':
    new_names_wo_ext = transliterate(new_names_wo_ext)

if to_number == 'yes':
    for i in xrange(num_working_files):
        old_name = working_files[i]
        new_names_wo_ext[i] = numbers_for_files[i] + '. ' + new_names_wo_ext[i]

for i in xrange(num_working_files):
    old_name = working_files[i]
    # print old_name
    new_name = new_names_wo_ext[i] + file_extension
    try:
        os.rename(old_name, new_name)
    except WindowsError:
        new_name = new_names_wo_ext[i] + '(2)' + file_extension
        os.rename(old_name, new_name)
