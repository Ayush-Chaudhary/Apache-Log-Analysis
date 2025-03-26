#!/usr/bin/env python
"""ip_mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    
    # Extract IP address (first column)
    if len(words) > 0:
        ip = words[0]
        # Output IP address with count 1
        print('%s\t%s' % (ip, 1)) 