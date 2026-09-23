#!/usr/bin/env python3
"""
syslog_listener.py
====================================================================
Darphane BİDB - Ağ İzleme (Network Monitoring) Projesi
Kaynak: Staj Günü 18 (30/07/2026) - SNMP ve Syslog protokolleri ile
        kurumsal ağ cihazlarının izlenmesi

Amaç:
    Cisco switch/router üzerinden "logging host <bu_makinenin_ip>"
    komutuyla UDP 514 portuna gönderilen Syslog mesajlarını
    gerçek zamanlı olarak dinler, ekrana basar, önem derecesine göre
    renklendirir ve logs-sample/ klasörüne tarih damgalı olarak
    kaydeder.

    Ayrıca en sık karşılaşılan olay tiplerini (link down/up,
    login failed, port-security violation vb.) tanıyıp özetler.

Kullanım:
    python3 syslog_listener.py [--port 514] [--host 0.0.0.0]

Not: UDP 514 portu ayrıcalıklı (privileged) bir porttur; Linux/macOS
    üzerinde root yetkisi veya --port 5140 gibi 1024 üzeri bir port
    gerekebilir.
====================================================================
"""

import argparse
import datetime
import os
import re
import socket
import sys

SEVERITY_NAMES = {
    0: "EMERGENCY", 1: "ALERT", 2: "CRITICAL", 3: "ERROR",
    4: "WARNING", 5: "NOTICE", 6: "INFORMATIONAL", 7: "DEBUG",
}

ANSI = {
    "red": "\033[91m", "yellow": "\033[93m", "green": "\033[92m",
    "cyan": "\033[96m", "reset": "\033[0m", "bold": "\033[1m",
}

EVENT_PATTERNS = [
    (re.compile(r"UPDOWN.*state to down", re.I), "LINK_DOWN", "red"),
    (re.compile(r"UPDOWN.*state to up", re.I), "LINK_UP", "green"),
    (re.compile(r"LOGIN_FAILED", re.I), "UNAUTHORIZED_LOGIN_ATTEMPT", "red"),
    (re.compile(r"PORT_SECURITY.*violation|err-disable", re.I), "PORT_SECURITY_VIOLATION", "red"),
    (re.compile(r"CONFIG_I", re.I), "CONFIG_CHANGED", "yellow"),
]


def parse_pri(raw: bytes):
    """RFC3164 formatındaki <PRI> alanını ayrıştırır."""
    text = raw.decode("utf-8", errors="replace").strip()
    match = re.match(r"^<(\d+)>(.*)$", text)
    if not match:
        return None, None, text
    pri = int(match.group(1))
    severity = pri % 8
    facility = pri // 8
    message = match.group(2)
    return facility, severity, message


def classify_event(message: str):
    for pattern, label, color in EVENT_PATTERNS:
        if pattern.search(message):
            return label, color
    return "GENERIC", "cyan"


def ensure_log_dir():
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs-sample")
    os.makedirs(log_dir, exist_ok=True)
    return log_dir


def main():
    parser = argparse.ArgumentParser(description="Darphane BİDB Syslog Dinleyici")
    parser.add_argument("--host", default="0.0.0.0", help="Dinlenecek arayüz (varsayılan: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=514, help="UDP port (varsayılan: 514)")
    args = parser.parse_args()

    log_dir = ensure_log_dir()
    log_file_path = os.path.join(
        log_dir, f"syslog_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind((args.host, args.port))
    except PermissionError:
        sys.exit(
            f"HATA: {args.port} portuna bağlanmak için yetki gerekiyor. "
            f"root ile çalıştırın veya --port 5140 gibi bir port deneyin."
        )
    except OSError as exc:
        sys.exit(f"HATA: Soket bağlanamadı: {exc}")

    print(f"{ANSI['bold']}Darphane BİDB Syslog Dinleyici{ANSI['reset']}")
    print(f"Dinleniyor: {args.host}:{args.port}  |  Log dosyası: {log_file_path}")
    print("Switch/Router tarafında 'logging host <bu_makinenin_ip>' komutu tanımlanmalıdır.")
    print("Çıkmak için Ctrl+C\n")

    event_counts = {}

    with open(log_file_path, "a", encoding="utf-8") as log_file:
        try:
            while True:
                raw, addr = sock.recvfrom(4096)
                facility, severity, message = parse_pri(raw)
                event_label, color = classify_event(message)
                event_counts[event_label] = event_counts.get(event_label, 0) + 1

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sev_name = SEVERITY_NAMES.get(severity, "UNKNOWN")

                line = f"[{timestamp}] {addr[0]} | {sev_name} | {event_label} | {message}"
                print(f"{ANSI[color]}{line}{ANSI['reset']}")
                log_file.write(line + "\n")
                log_file.flush()
        except KeyboardInterrupt:
            print("\n\nDinleme durduruldu.")
            print("Olay özeti:")
            for label, count in sorted(event_counts.items(), key=lambda x: -x[1]):
                print(f"  {label}: {count}")


if __name__ == "__main__":
    main()
