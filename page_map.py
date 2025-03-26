#!/usr/bin/env python
"""page_mapper.py"""

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # Use regex to find the GET request and extract the path
    match = re.search(r'GET\s+([^\s]+)', line)
    if match:
        path = match.group(1)
        # Output path with count 1
        print('%s\t%s' % (path, 1)) 