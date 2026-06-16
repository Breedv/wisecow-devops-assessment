import psutil
from datetime import datetime

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

LOG_FILE = "system_health.log"

alerts = []

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
processes = len(psutil.pids())

print("=" * 50)
print("SYSTEM HEALTH REPORT")
print("=" * 50)
print(f"Timestamp: {datetime.now()}")
print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")
print(f"Running Processes: {processes}")

if cpu > CPU_THRESHOLD:
    alerts.append(f"CPU usage exceeded threshold: {cpu}%")

if memory > MEM_THRESHOLD:
    alerts.append(f"Memory usage exceeded threshold: {memory}%")

if disk > DISK_THRESHOLD:
    alerts.append(f"Disk usage exceeded threshold: {disk}%")

if alerts:
    print("\nALERTS:")
    for alert in alerts:
        print(f"[WARNING] {alert}")

    with open(LOG_FILE, "a") as log:
        log.write(f"\n[{datetime.now()}]\n")
        for alert in alerts:
            log.write(alert + "\n")
else:
    print("\nSystem is healthy.")