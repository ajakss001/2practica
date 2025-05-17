import psutil
import sqlite3
from datetime import datetime
import time
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

class SystemMonitor:
    def __init__(self, db_name='monitor.db'):
        self.db_name = db_name
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS cpu(timestamp DATETIME, percent REAL)')
            conn.execute('CREATE TABLE IF NOT EXISTS mem(timestamp DATETIME, used REAL, total REAL, percent REAL)')
            conn.execute('CREATE TABLE IF NOT EXISTS disk(timestamp DATETIME, used REAL, total REAL, percent REAL)')

    def collect(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('INSERT INTO cpu VALUES (?, ?)', (now, psutil.cpu_percent(interval=1)))
            mem = psutil.virtual_memory()
            conn.execute('INSERT INTO mem VALUES (?, ?, ?, ?)', (now, mem.used, mem.total, mem.percent))
            disk = psutil.disk_usage('/')
            conn.execute('INSERT INTO disk VALUES (?, ?, ?, ?)', (now, disk.used, disk.total, disk.percent))

    def get_data(self, table, limit=None):
        with sqlite3.connect(self.db_name) as conn:
            query = f'SELECT * FROM {table} ORDER BY timestamp DESC'
            if limit: query += f' LIMIT {limit}'
            return conn.execute(query).fetchall()

    def plot(self, table, title):
        data = self.get_data(table)
        timestamps = [datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S') for row in data]
        plt.figure(figsize=(10, 5))
        plt.plot(timestamps, [row[-1] for row in data])
        plt.title(title)
        plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))
        plt.grid()
        plt.show()

    def print_status(self):
        cpu, mem, disk = self.get_data('cpu', 1)[0], self.get_data('mem', 1)[0], self.get_data('disk', 1)[0]
        print(f"\nTime: {cpu[0]}\nCPU: {cpu[1]:.1f}%\nMemory: {mem[3]:.1f}% ({mem[1]/1e9:.1f}GB/{mem[2]/1e9:.1f}GB)\nDisk: {disk[3]:.1f}% ({disk[1]/1e9:.1f}GB/{disk[2]/1e9:.1f}GB)")

monitor = SystemMonitor()
try:
    while True:
        monitor.collect()
        monitor.print_status()
        time.sleep(5)
except KeyboardInterrupt:
    monitor.plot('cpu', 'CPU Usage')
    monitor.plot('mem', 'Memory Usage')
    monitor.plot('disk', 'Disk Usage')