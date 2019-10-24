# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:39:16 2019

@author: FangGuo
"""



import glob, os
import re

directory = r'\\Schcasql8\ssis\Invoice_Files\CanadaPost'
os.chdir(directory)
for filename in glob.glob("*.txt"):
    process_file = directory + '\\' + filename
    with open(process_file) as f:
        Text = f.read().splitlines(True)
    with open(process_file, "w") as f:
        f.writelines(Text[1:])
    with open(process_file) as f:
        Text = f.read()
        newText = Text.replace('" ', 'quotation ')
        newText= re.sub('-%', '', newText)
    with open(process_file, "w") as f:
        f.write(newText)
