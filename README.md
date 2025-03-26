# Apache Access Log Analysis using MapReduce

This project contains MapReduce scripts to analyze Apache Access Logs. The scripts are designed to answer three specific questions:

1. Number of unique users by their IP addresses
2. Count of each browser in the log
3. Most popular 5 webpages

## Files

- `ip_map.py` and `ip_reduce.py`: Count unique IP addresses
- `browser_map.py` and `browser_reduce.py`: Count browser occurrences
- `page_map.py` and `page_reduce.py`: Find most popular webpages
- `run_analysis.py`: Script to run all analyses and save results to a text file

## Usage

### Individual Analysis

For each analysis, use the following command pattern:

```bash
cat oreillyaccess10.log | python <map_script>.py | sort | python <reduce_script>.py
```

### Examples:

1. To count unique IP addresses:
```bash
cat oreillyaccess10.log | python ip_map.py | sort | python ip_reduce.py
```

2. To count browser occurrences:
```bash
cat oreillyaccess10.log | python browser_map.py | sort | python browser_reduce.py
```

3. To find most popular webpages:
```bash
cat oreillyaccess10.log | python page_map.py | sort | python page_reduce.py
```

### Running All Analyses

To run all analyses and save the results to a text file:

```bash
python run_analysis.py
```

This will create a file named `analysis_results_YYYYMMDD_HHMMSS.txt` containing all three analyses.

## Output Format

- IP Analysis: Shows each IP address and its count, followed by total unique IPs
- Browser Analysis: Shows each browser type and its count
- Page Analysis: Shows the top 5 most accessed webpages with their counts

## Notes

- The scripts assume the Apache log format follows the standard pattern
- Browser detection is based on major browser engines (Mozilla, Chrome, Safari, Edge, IE)
- Webpage paths are extracted from GET requests 