# 11. Wireshark Paket Analizi, ICMP/ARP Testleri ve Sorun Giderme

**Tarih:** 14/07/2026, 29/07/2026 (Staj Günü 7, 17)

## Komut Satırı ile Katman 3 Doğrulaması (Gün 7)

PC-1'den PC-2'ye yönelik testler:

```
ping 192.168.1.20      → ICMP Echo Request/Reply, %0 paket kaybı, düşük RTT
arp -a                 → IP-MAC çözümleme tablosu (ARP Table)
tracert 192.168.1.20   → tek atlamalı (single-hop) yol doğrulaması
```

## Wireshark ile Paket Yakalama (Gün 17)

Ağ Arayüz Kartı **Promiscuous Mode**'a alınarak canlı trafik dinlenmiştir. Yakalanan ve analiz edilen paket tipleri:

- Ethernet II çerçeveleri
- ARP istek/yanıt paketleri
- ICMP (Ping) kontrol paketleri
- **TCP 3-Way Handshake:** SYN → SYN-ACK → ACK

## Sistematik Sorun Giderme Metodolojisi

OSI Katman 1'den (Fiziksel) başlayarak yukarı doğru adım adım kontrol edilen, kurgulanmış 3 arıza senaryosu:

| # | Senaryo | Kök Neden Tespiti | Çözüm |
|---|---|---|---|
| 1 | Kablo temassızlığı / sinyal kaybı | Fiziksel katman (Katman 1) LED durumu | Kablo değişimi |
| 2 | Yanlış VLAN port ataması (Katman 2 erişim engeli) | `show vlan brief` ile port-VLAN eşleşmesi | Switch CLI üzerinden port VLAN düzeltmesi |
| 3 | IP Çakışması (IP Conflict / Gratuitous ARP) | `ping`, `arp -a`, `ipconfig /renew` | IP bloğunun yeniden düzenlenmesi |

Kullanılan Wireshark görüntüleme filtreleri: `arp`, `icmp`, `ip.addr`

Bu çalışma ile kurumsal bir ağda kriz anında yapılması gereken teknik müdahale ve paket düzeyinde arıza tespit tecrübesi kazanılmıştır.
