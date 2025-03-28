#!/usr/bin/env python
"""browser_reducer.py"""

from operator import itemgetter
import sys

current_browser = None
current_count = 0
browser = None

# List to store output lines
output_lines = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    browser, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because we sort the map output
    # by key (here: browser) before it is passed to the reducer
    if current_browser == browser:
        current_count += count
    else:
        if current_browser:
            # store result in our output list
            output_lines.append(f"{current_browser}\t{current_count}")
        current_count = count
        current_browser = browser

# do not forget to output the last word if needed!
if current_browser == browser:
    output_lines.append(f"{current_browser}\t{current_count}")

# Sort the output lines by count in descending order
sorted_output = sorted(output_lines, key=lambda x: int(x.split('\t')[1]), reverse=True)

# Print results to stdout
for line in sorted_output:
    print(line)

# Save results to file
with open('browser_analysis.txt', 'w') as f:
    f.write("Browser Usage Analysis Results\n")
    f.write("============================\n\n")
    f.write("Browser\tCount\n")
    f.write("-------\t-----\n")
    for line in sorted_output:
        f.write(line + '\n') 