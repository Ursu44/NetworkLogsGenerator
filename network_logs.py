import random
from utils import (
    syslog_timestamp, hostname,
    random_port, internal_ip, external_ip,
    is_attack_wave
)

def firewall_log(malicious=False):
    protocols = ["TCP", "UDP"]

    if malicious:
        action = "BLOCK"
        src    = external_ip()
        dst    = internal_ip()
    else:
        action = "ACCEPT"
        src    = internal_ip()
        dst    = external_ip()

    return (
        f"{syslog_timestamp()} {hostname()} firewall "
        f"{action} "
        f"{random.choice(protocols)} "
        f"{src}:{random_port()} "
        f"{dst}:{random_port()}"
    )


def dns_log(malicious=False):
    domains_good = [
        "google.com",
        "github.com",
        "microsoft.com"
    ]
    domains_bad = [
        "suspicious-domain.xyz",
        "c2-server.bad",
        "malware-callback.ru"
    ]

    domain = random.choice(domains_bad if malicious else domains_good)

    return (
        f"{syslog_timestamp()} {hostname()} "
        f"named[{random.randint(1000,5000)}]: "
        f"client {internal_ip()}#{random.randint(1024,65535)} "
        f"query: {domain} IN A"
    )

def ids_log(malicious=False):
    alerts = [
        ("ET SCAN Possible Nmap Scan",              3),
        ("ET TROJAN Possible C2 Communication",     3),
        ("ET DATA Data Exfiltration Attempt",        3),
        ("ET POLICY Suspicious outbound traffic",    2),
    ]

    if malicious:
        alert, severity = random.choice(alerts)
        return (
            f"{syslog_timestamp()} {hostname()} "
            f"suricata[{random.randint(2000,6000)}]: "
            f"[1:{random.randint(2000000,3000000)}:{severity}] "
            f"{alert} "
            f"{{TCP}} {internal_ip()}:{random.randint(1024,65535)} -> "
            f"{external_ip()}:{random.choice([80,443,22,8080])}"
        )

    return (
        f"{syslog_timestamp()} {hostname()} "
        f"suricata[{random.randint(2000,6000)}]: "
        f"flow tcp {internal_ip()}:{random.randint(1024,65535)} -> "
        f"{external_ip()}:443 established"
    )

def routing_log(malicious=False):
    messages_good = [
        "Route update successful",
        "BGP session established",
        "Routing table recalculated"
    ]
    messages_bad = [
        "BGP session reset"
    ]

    return (
        f"{syslog_timestamp()} {hostname()} routerd: "
        f"{random.choice(messages_bad if malicious else messages_good)}"
    )

def generate():
    # ── is_attack_wave() în loc de GOOD_RATIO ────────────────────
    malicious = is_attack_wave()

    generators = [
        lambda: firewall_log(malicious),
        lambda: dns_log(malicious),
        lambda: ids_log(malicious),
        lambda: routing_log(malicious)
    ]

    return random.choice(generators)()