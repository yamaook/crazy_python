#!/usr/bin/env python
import sys

data = sys.stdin.read()
print('Content-type: text/plain\n\nGot Data: "%s"' % data)
