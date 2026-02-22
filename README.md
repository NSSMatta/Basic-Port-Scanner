# Basic Port Scanner

A simple, fast port scanner written in Python using thread pools.

## Description
This script attempts to connect to a target IP address on a range of specified ports to identify which ones are open.

## Features
- Scans a range of ports or specific ports provided in a comma-separated list
- Uses Python `concurrent.futures.ThreadPoolExecutor` for fast execution

## Usage
Run the script with Python 3:
```bash
python port_scanner.py 127.0.0.1 -p 1-1000
```
This will scan the first 1000 ports on localhost.
YOLO Badge Update
