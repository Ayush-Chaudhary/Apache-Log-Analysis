#!/usr/bin/env python
"""ip_reducer.py"""

from operator import itemgetter
import sys

current_ip = None
current_count = 0
ip = None
total_unique_ips = 0

# List to store output lines
output_lines = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    ip, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because we sort the map output
    # by key (here: ip) before it is passed to the reducer
    if current_ip == ip:
        current_count += count
    else:
        if current_ip:
            # store result in our output list
            output_lines.append(f"{current_ip}\t{current_count}")
            total_unique_ips += 1
        current_count = count
        current_ip = ip

# do not forget to output the last word if needed!
if current_ip == ip:
    output_lines.append(f"{current_ip}\t{current_count}")
    total_unique_ips += 1

# Print results to stdout
for line in output_lines:
    print(line)

# Save results to file
with open('ip_analysis.txt', 'w') as f:
    f.write("IP Address Analysis Results\n")
    f.write("=========================\n\n")
    f.write(f"Total Unique IPs: {total_unique_ips}\n\n")
    f.write("IP Address\tCount\n")
    f.write("----------\t-----\n")
    for line in output_lines:
        f.write(line + '\n') 