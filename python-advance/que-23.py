# : 23) Write a Python program to search for a word in a string using re.search()

import re

str = "apple,23,sgxyqw,dwdw 23," 
pattern = r'\bapple\b'

mathch = re.search(pattern,str)

print(mathch)