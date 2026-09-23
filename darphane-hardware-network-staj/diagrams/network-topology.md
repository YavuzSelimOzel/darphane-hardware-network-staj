# Ağ Topolojisi ve VLAN Şeması

## Fiziksel / Mantıksal Topoloji

```mermaid
graph TB
    subgraph "VLAN 10 - PERSONEL (192.168.10.0/24)"
        PC1[PC-1<br/>192.168.1.10<br/>Fa0/1]
    end

    subgraph "VLAN 20 - MISAFIR (192.168.20.0/24)"
        PC2[PC-2<br/>192.168.1.20<br/>Fa0/2]
    end

    PC1 -->|Cat6 UTP T568B| SW
    PC2 -->|Cat6 UTP T568B| SW

    subgraph SW["Cisco 2960 Yönetilebilir Switch (SW-DARPHANE-TEST)"]
        direction TB
        FA01[Fa0/1 - Access VLAN10]
        FA02[Fa0/2 - Access VLAN20]
        GI01[Gi0/1 - Trunk 802.1Q]
    end

    SW -->|Trunk - GigabitEthernet| RT

    subgraph RT["Router (Router-on-a-Stick)"]
        SUB10["Gi0/0/0.10<br/>dot1Q 10<br/>GW: 192.168.10.1/24"]
        SUB20["Gi0/0/0.20<br/>dot1Q 20<br/>GW: 192.168.20.1/24"]
    end

    VM["VMware VM<br/>192.168.1.30<br/>Bridged vNIC -> vSwitch0"] -.->|Host: PC-1 üzerinden| SW

    SW -.->|Syslog UDP/514, SNMP| MON[Syslog / Network Monitoring<br/>syslog_listener.py]
```

## VLAN Tablosu

| VLAN ID | İsim | Amaç | Örnek Host IP | Gateway (Sub-interface) |
|---|---|---|---|---|
| 1 | default | Yönetim SVI | 192.168.1.2/24 | — |
| 10 | PERSONEL | Kurum içi personel cihazları | 192.168.1.10 → 192.168.10.x | 192.168.10.1/24 |
| 20 | MISAFIR | Ziyaretçi/misafir cihazları (izole) | 192.168.1.20 → 192.168.20.x | 192.168.20.1/24 |

## Katman Bazlı Akış (OSI)

1. **Katman 1 (Fiziksel):** Cat6 UTP T568B kablolama, LED link/activity durumları, Auto-Negotiation ile 1 Gbps / Full-Duplex senkronizasyon.
2. **Katman 2 (Veri Bağı):** Switch CAM (MAC Address) tablosu, VLAN'lar arası izolasyon, 802.1Q trunk etiketleme, Port Security (sticky MAC).
3. **Katman 3 (Ağ):** IPv4 statik adresleme, Router-on-a-Stick ile Inter-VLAN Routing, ICMP (ping/tracert) doğrulaması.
4. **Katman 7 (Uygulama):** SMB (TCP/445) dosya paylaşımı testleri, RDP (TCP/3389) ve SSH (TCP/22) yönetim erişimi.
