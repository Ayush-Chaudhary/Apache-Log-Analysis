#!/usr/bin/env python
"""browser_mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split('" "')
    
    # # Extract browser information (second to last column)
    # if len(words) >= 2:
    #     browser = words[-1]
    #     # Clean up browser string to get major browser engine
    #     if 'Mozilla' in browser:
    #         if 'Firefox' in browser:
    #             browser = 'Firefox'
    #         elif 'Chrome' in browser:
    #             browser = 'Chrome'
    #         elif 'Safari' in browser:
    #             browser = 'Safari'
    #         elif 'Edge' in browser:
    #             browser = 'Edge'
    #         else:
    #             browser = 'Other browser in Mozilla browser engine'
    #     elif 'MSIE' in browser or 'Trident' in browser:
    #         browser = 'Internet Explorer'
    #     elif 'Opera' in browser:
    #         browser = 'Opera'
    #     else:
    #         browser = 'Unknown Browser engine'
    
        # output the browser and count of 1
    print('%s\t%s' % (words[-1], 1)) 