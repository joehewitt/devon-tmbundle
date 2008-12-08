#!/usr/bin/env python

from os import environ as ENV
import sys

prefix = sys.argv[1]
pattern = sys.argv[2]
wrapWidth = int(ENV["TM_COLUMNS"])
offset = int(ENV['TM_LINE_INDEX'])
patternLen = (wrapWidth - offset)/len(pattern) - len(prefix)
line = '%s%s\n%s' % (prefix, pattern * patternLen, ' ' * offset)
sys.stdout.write(line.replace("\\", "\\\\"))

