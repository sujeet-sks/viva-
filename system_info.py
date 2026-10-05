import os
import socket
import shutil
import time
from datetime import datetime

print(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


print(f"User: {os.environ.get('USERNAME') or os.environ.get('USER')}")
print(f"Hostname: {socket.gethostname()}")

print(f"Directory: {os.getcwd()}")

#available disk space (in GB)
total, used, free = shutil.disk_usage(".")
print(f"Available Disk: {free / (1024**3):.2f} GB")

#system uptime
try:
    uptime_seconds = time.clock_gettime(1)
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    print(f"System Uptime: {hours} hours, {minutes} minutes")
except AttributeError:
    import ctypes
    uptime_ms = ctypes.windll.kernel32.GetTickCount64()
    hours = int(uptime_ms // (1000 * 3600))
    print(f"System Uptime: ~{hours} hours")
