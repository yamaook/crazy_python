"""
    12.5.5 管道输入
"""
import sys
import re

mainPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+' \
              + '[\.][a-z]{2,3}([\.][a-z]{2})?'

text = sys.stdin.read()
it = re.finditer(mainPattern, text, re.I)
for e in it:
    print(str(e.span()) + '--->' + e.group())
