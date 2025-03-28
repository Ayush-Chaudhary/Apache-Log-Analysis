#!/usr/bin/env python
"""page_mapper.py"""

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    words = line.split()
    
    link = words[6]
    print('%s\t%s' % (link, 1)) 