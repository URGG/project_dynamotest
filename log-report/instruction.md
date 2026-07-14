# Access Log Analysis

You need to parse an Apache-style access log and generate a JSON summary report.

## Success Criteria

1. Calculate `total_requests`: The total number of request lines in the log.
2. Calculate `unique_ips`: The total number of unique client IP addresses.
3. Calculate `top_path`: The single most frequently requested path.
4. Save your output to a file exactly named `/app/report.json` with the calculated metrics as keys.