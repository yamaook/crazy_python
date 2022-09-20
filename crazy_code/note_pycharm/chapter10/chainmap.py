"""
10.8.1 chainmap对象
"""

from collections import ChainMap

a = {'Kotlin': 90, 'Python': 86}
b = {'Go': 93, 'Python': 92}
c = {'Swift': 89, 'Go': 87}
cm = ChainMap(a, b, c)
print(cm)
print(cm['Kotlin'])
print(cm['Python'])
print(cm['Go'])

import builtins

my_name = '孙悟空'


def test():
    my_name = 'yeeku'
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    print(pylookup['my_name'])
    print(pylookup['len'])


test()

import os, argparse

defaults = {'color': '蓝色', 'user': 'yeeku'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])
print(combined['PYTHONPATH'])
