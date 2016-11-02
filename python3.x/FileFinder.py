'''
.SYNOPSIS
    Fint files & their count with their extention
.DESCRIPTION
    This can be used to find files with certain extention. You will also be able to find the number of such files. 
.NOTES
    File Name      : FileFinder.py
    Author         : gajendra d ambi
    Prerequisite   : python 3.5 (tested on windows)
    Copyright      - none
.LINK
    Script posted over:
    github.com/gajuambi/python
'''
import os
#fnname stands for FileNameMatch
import fnmatch
DIRECTORY = input('path?: ')
EXTN = input('pattern, extention of the file? ')
print('examples : for mp4 files, type *.mp4; for text files, type *.mp3')
TOTAL = 0
#print('ex: to find mp4 files type *.mp4, for text files type *.txt')
for dirname, dirnames, filenames in os.walk(DIRECTORY):
# print path to all filenames.
    for filename in filenames:
        if fnmatch.fnmatch(filename, EXTN):
            TOTAL += 1
            print(TOTAL)
            print(os.path.join(dirname, filename))