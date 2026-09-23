# 5. Fiziksel Ağ Kurulumu, IPv4 Adresleme ve Switch Temel Konfigürasyonu

**Tarih:** 10/07/2026, 13/07/2026, 16/07/2026 (Staj Günü 5, 6, 8)

## Fiziksel Bağlantılar

2 adet istemci PC ve 1 adet Cisco Kat-2 Yönetilebilir Switch laboratuvar ortamında konumlandırılmış; Cat6 Ethernet kabloları ile bilgisayarlar Switch'in FastEthernet/GigabitEthernet portlarına bağlanmıştır. Auto-Negotiation protokolü ile cihazların **1000 Mbps (1 Gbps) / Full-Duplex** modda senkronize olduğu doğrulanmıştır.

## IPv4 Adresleme Planı

- **Ağ Adresi:** 192.168.1.0/24 (C Sınıfı, RFC 1918 özel IP bloğu)
- **Alt Ağ Maskesi:** 255.255.255.0
- **Kullanılabilir Host:** 254 adet

| Cihaz | IP Adresi | Alt Ağ Maskesi |
|---|---|---|
| PC-1 | 192.168.1.10 | 255.255.255.0 |
| PC-2 | 192.168.1.20 | 255.255.255.0 |
| Switch (SVI) | 192.168.1.2 | 255.255.255.0 |

IP tanımlamaları `ncpa.cpl` → TCP/IPv4 Özellikleri üzerinden DHCP'den Statik IP'ye geçilerek yapılmış; `ipconfig /all` ile doğrulanmıştır.

## Switch CLI Erişimi

Fabrika ayarlarındaki bir Switch'e ağ üzerinden IP ile erişilemediği için ilk erişim **RS-232 / USB-to-RJ45 Console kablosu** ile sağlanır.

**COM Port Parametreleri:** Baud Rate 9600, Data Bits 8, Parity None, Stop Bits 1, Flow Control None (PuTTY / TeraTerm)

### CLI Mod Hiyerarşisi

```
Switch>                    User EXEC Mode
Switch# (enable)           Privileged EXEC Mode
Switch(config)#            Global Configuration Mode (configure terminal)
```

Uygulanan temel konfigürasyon: bkz. [`configs/switch/01-baseline.txt`](../configs/switch/01-baseline.txt)

Yapılan konfigürasyonlar `write memory` (`copy running-config startup-config`) ile NVRAM'e kalıcı olarak kaydedilmiştir.
