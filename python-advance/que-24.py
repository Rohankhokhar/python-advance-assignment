import re

str = "apple,23,sgxyqw,dwdw 23," 
pattern = r'\bapple\b'

mathch = re.match(pattern,str)

print(mathch)