from datetime import datetime, timezone
import random
import time

_attack_state = {
    "in_attack":   False,
    "attack_end":  0.0,
    "next_attack": time.time() + random.randint(120, 300),
}

def is_attack_wave() -> bool:
    now   = time.time()
    state = _attack_state

    if state["in_attack"]:
        if now < state["attack_end"]:
            return random.random() < 0.90
        else:
            state["in_attack"]   = False
            state["next_attack"] = now + random.randint(180, 480)
            print(
                f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] "
                f"⚔️  Attack wave terminat. "
                f"Următor în {int(state['next_attack'] - now)}s"
            )
            return random.random() < 0.08
    else:
        if now >= state["next_attack"]:
            duration            = random.randint(30, 90)
            state["in_attack"]  = True
            state["attack_end"] = now + duration
            print(
                f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] "
                f"🚨 Attack wave START — durată {duration}s"
            )
            return random.random() < 0.90
        else:
            return random.random() < 0.08


def hostname():
    return random.choice(["server", "web01", "db01", "fw01", "ids01"])


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
    return (
        f"{random.randint(20,120)}.{random.randint(0,25)}"
        f".{random.randint(0,25)}.{random.randint(1,24)}"
    )