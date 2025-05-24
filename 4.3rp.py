import subprocess
import sqlite3
from datetime import datetime
import time

conn = sqlite3.connect('sys_monitor_mac.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT,
    cpu REAL,
    memory REAL,
    disk REAL
)
""")
conn.commit()

def get_cpu_usage():
    try:
        output = subprocess.check_output(["top", "-l", "1", "-n", "0"]).decode()
        for line in output.splitlines():
            if "CPU usage" in line:
                parts = line.split(':')[1].split(',')
                idle_part = [p for p in parts if 'idle' in p]
                if idle_part:
                    idle_str = idle_part[0]
                    idle_value_str = idle_str.strip().split()[0].replace('%','')
                    idle_value = float(idle_value_str)
                    return 100 - idle_value
        return None
    except:
        return None

def get_memory_usage():
    try:
        output = subprocess.check_output(["vm_stat"]).decode()
        page_size_bytes = None
        pages_free=pages_active=pages_inactive=pages_speculative=pages_wired_down=0
        for line in output.splitlines():
            if "page size of" in line:
                page_size_bytes=int(line.split('of')[1].split()[0])
            elif "Pages free:" in line:
                pages_free=int(line.split(':')[1].strip().replace('.',''))
            elif "Pages active:" in line:
                pages_active=int(line.split(':')[1].strip().replace('.',''))
            elif "Pages inactive:" in line:
                pages_inactive=int(line.split(':')[1].strip().replace('.',''))
            elif "Pages speculative:" in line:
                pages_speculative=int(line.split(':')[1].strip().replace('.',''))
            elif "Pages wired down:" in line:
                pages_wired_down=int(line.split(':')[1].strip().replace('.',''))
        if page_size_bytes is None or (pages_free+pages_active+pages_inactive+pages_speculative+pages_wired_down)==0:
            return None
        total_pages=pages_free+pages_active+pages_inactive+pages_speculative+pages_wired_down
        total_memory_bytes=total_pages*page_size_bytes
        free_memory_bytes=pages_free*page_size_bytes
        used_percent=(total_memory_bytes - free_memory_bytes)/total_memory_bytes*100
        return used_percent
    except:
        return None

def get_disk_usage():
    try:
        output=subprocess.check_output(["df","/"]).decode()
        lines=output.splitlines()
        if len(lines)>=2:
            parts=lines[1].split()
            capacity=float(parts[4].strip('%'))
            return capacity
        return None
    except:
        return None

def save():
    now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu_usage=get_cpu_usage()
    memory_usage=get_memory_usage()
    disk_usage=get_disk_usage()
    cur.execute(
        "INSERT INTO stats (time, cpu, memory, disk) VALUES (?, ?, ?, ?)",
        (now, cpu_usage, memory_usage, disk_usage)
     )
    conn.commit()

def show():
    cur.execute("SELECT * FROM stats ORDER BY id")
    rows=cur.fetchall()
    print(f"{'ID':<4} {'Время':<19} {'CPU (%)':<8} {'Память (%)':<10} {'Диск (%)':<8}")
    print("-"*55)
    for row in rows:
        id_, time_str, cpu, memory, disk = row
        cpu_str=f"{cpu:.1f}" if cpu is not None else "N/A"
        memory_str=f"{memory:.1f}" if memory is not None else "N/A"
        disk_str=f"{disk:.1f}" if disk is not None else "N/A"
        print(f"{id_:<4} {time_str:<19} {cpu_str:<8} {memory_str:<10} {disk_str:<8}")

if __name__=="__main__":
    while True:
        print("\n1 - Сохранить\n2 - Показать\n3 - Выход")
        cmd=input("Выберите: ").strip()
        if cmd=='1':
            save()
            time.sleep(1)
        elif cmd=='2':
            show()
        elif cmd=='3':
            break
conn.close()