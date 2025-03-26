#!/usr/bin/env python
"""page_reducer.py"""

from operator import itemgetter
import sys

current_path = None
current_count = 0
path = None

# Dictionary to store all paths and their counts
path_counts = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    path, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because we sort the map output
    # by key (here: path) before it is passed to the reducer
    if current_path == path:
        current_count += count
    else:
        if current_path:
            # Store the count in our dictionary
            path_counts[current_path] = current_count
        current_count = count
        current_path = path

# do not forget to output the last word if needed!
if current_path == path:
    path_counts[current_path] = current_count

# Sort paths by count and get top 5
sorted_paths = sorted(path_counts.items(), key=itemgetter(1), reverse=True)[:5]

# Print the top 5 most popular pages
print("\nTop 5 Most Popular Pages:")
print("------------------------")
for path, count in sorted_paths:
    print(f"{path}\t{count}")

# Save results to file
with open('page_analysis.txt', 'w') as f:
    f.write("Most Popular Pages Analysis Results\n")
    f.write("=================================\n\n")
    f.write("Top 5 Most Popular Pages:\n")
    f.write("------------------------\n")
    f.write("Page Path\tCount\n")
    f.write("---------\t-----\n")
    for path, count in sorted_paths:
        f.write(f"{path}\t{count}\n") 