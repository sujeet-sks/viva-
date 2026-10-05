import psutil
import time

#process name as input
target_process = input("Enter the process name to check : ").strip().lower()

process_found = False

#loop through all currently running system processes
for proc in psutil.process_iter(['pid', 'name']):
    try:
        #check if the process name matches what the user typed
        if target_process in proc.info['name'].lower():
            process_found = True
            pid = proc.info['pid']
            p = psutil.Process(pid)
            cpu_usage = p.cpu_percent(interval=0.1)
            memory_bytes = p.memory_info().rss
            memory_mb = memory_bytes / (1024 * 1024)
            print(f"\nProcess Found: {proc.info['name']}")
            print(f"Process ID (PID): {pid}")
            print(f"CPU Usage      : {cpu_usage}%")
            print(f"Memory Usage   : {memory_mb:.2f} MB")
            
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        #skip processes that close unexpectedly or have restricted system permissions
        continue

#if the process isn't running at all
if not process_found:
    print(f"\nProcess Not Found! '{target_process}' is not currently running.")
