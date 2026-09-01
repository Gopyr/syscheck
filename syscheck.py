#!/usr/bin/env python3
"""
SysCheck — Local system health checker.
Usage:
    python3 syscheck.py [--json]

Output:
    - Text summary to stdout
    - JSON if --json is set
"""
import argparse, json, os, socket, subprocess
from datetime import datetime, timezone, timedelta

def now_wib():
    return datetime.now(timezone(timedelta(hours=7))).strftime('%Y-%m-%d %H:%M:%S WIB')

def run(cmd):
    try:
        out = subprocess.check_output(cmd, shell=True, text=True, timeout=10)
        return out.strip()
    except Exception as e:
        return f"error: {e}"

def check():
    uptime = run("uptime -p")
    load = run("cat /proc/loadavg | awk '{print $1, $2, $3}'")
    mem = run("free -h | awk '/Mem:/{print $3, $2, $7}'")
    disk = run("df -h / | awk 'NR==2{print $3, $2, $5}'")
    procs = run("ps -eo user,pid,%cpu,%mem,cmd --no-headers | wc -l")
    return {
        'timestamp': now_wib(),
        'uptime': uptime,
        'load': load,
        'memory_used_total_avail': mem,
        'disk_used_total_pct': disk,
        'process_count': procs,
    }

def main():
    parser = argparse.ArgumentParser(description='Local system health checker')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()

    data = check()
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(f"=== SysCheck {data['timestamp']} ===")
        print(f"Uptime: {data['uptime']}")
        print(f"Load: {data['load']}")
        print(f"RAM: {data['memory_used_total_avail']}")
        print(f"Disk: {data['disk_used_total_pct']}")
        print(f"Processes: {data['process_count']}")

if __name__ == '__main__':
    main()
