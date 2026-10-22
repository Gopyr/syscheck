# SysCheck
Cek kesehatan sistem lokal dari terminal.

## Tujuan
- Cek uptime, load, RAM, disk, dan jumlah proses
- Output text atau JSON
- Ringkasan cepat untuk troubleshooting

## Cara pakai
```bash
python3 syscheck.py          # text output
python3 syscheck.py --json   # JSON output
```

## Preview output (text)
```
=== SysCheck 2026-09-01 12:06:18 WIB ===
Uptime: up 1 day, 19 hours, 14 minutes
Load: 0.11 0.22 1.38
RAM: 4.5Gi 23Gi 19Gi
Disk: 27G 48G 57%
Processes: 21
```

## Preview output (JSON)
```json
{
  "timestamp": "2026-09-01 12:06:18 WIB",
  "uptime": "up 1 day, 19 hours, 14 minutes",
  "load": "0.11 0.22 1.38",
  "memory_used_total_avail": "4.5Gi 23Gi 19Gi",
  "disk_used_total_pct": "27G 48G 57%",
  "process_count": "21"
}
```
