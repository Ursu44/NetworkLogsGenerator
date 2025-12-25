from datetime import datetime, timezone
import random

HOSTNAMES = ["server", "web01", "db01", "fw01", "ids01"]

def hostname():
    return random.choice(HOSTNAMES)

def syslog_timestamp():
    return datetime.now(timezone.utc).strftime("%b %d %H:%M:%S")

def random_port():
    common_ports = [22, 80, 443, 3389, 3306, 5432]
    if random.random() < 0.7:
        return random.choice(common_ports)
    return random.randint(1024, 6553)

def internal_ip():
    return f"192.168.{random.randint(0,25)}.{random.randint(10,25)}"

def external_ip():
    return f"{random.randint(20,120)}.{random.randint(0,25)}.{random.randint(0,25)}.{random.randint(1,24)}"