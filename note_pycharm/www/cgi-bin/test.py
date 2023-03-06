#!/usr/bin/env python
import sys

data = sys.stdin.read()
print('Content-type: text/plain\n\nGot Data: "%s"' % data)
# print("Content-Type: text/html \n")
# print('Hello World')
