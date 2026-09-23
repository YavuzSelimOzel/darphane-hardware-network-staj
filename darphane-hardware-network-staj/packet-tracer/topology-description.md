# Cisco Packet Tracer — Dijital İkiz Topolojisi Yeniden Kurulum Talimatı

Bu depo bir `.pkt` binary dosyası içermez (ikili format, versiyon uyumluluğu ve metin tabanlı diff/versiyon kontrolüne uygun olmadığı için). Bunun yerine, staj defteri Günü 9 ve 13'te tarif edilen topoloji burada adım adım yeniden üretilebilir şekilde tarif edilmiştir; Packet Tracer'da bu adımlar birebir uygulanarak `.pkt` dosyası yeniden oluşturulabilir.

## 1. Cihazların Yerleştirilmesi

| Cihaz | Kütüphane | Model |
|---|---|---|
| PC-0 | End Devices | Generic PC |
| PC-1 | End Devices | Generic PC |
| SW-DARPHANE-TEST | Switches | Cisco Catalyst 2960 (24 port, Layer-2) |
| RT-DARPHANE-TEST | Routers | Cisco 2911 Series |

## 2. Kablolama (Connections)

| Kablo Tipi | Bağlantı |
|---|---|
| Copper Straight-Through | PC-0 FastEthernet0 ↔ Switch FastEthernet0/1 |
| Copper Straight-Through | PC-1 FastEthernet0 ↔ Switch FastEthernet0/2 |
| Copper Straight-Through (Trunk) | Switch GigabitEthernet0/1 ↔ Router GigabitEthernet0/0/0 |

## 3. IP Yapılandırması (Desktop → IP Configuration)

| Cihaz | IP Adresi | Alt Ağ Maskesi | Varsayılan Ağ Geçidi |
|---|---|---|---|
| PC-0 | 192.168.1.10 | 255.255.255.0 | 192.168.10.1 |
| PC-1 | 192.168.1.20 | 255.255.255.0 | 192.168.20.1 |

## 4. CLI Konfigürasyonu

Switch ve Router için aşağıdaki dosyaları sırasıyla CLI sekmesine yapıştırın:

1. [`../configs/switch/01-baseline.txt`](../configs/switch/01-baseline.txt)
2. [`../configs/switch/02-vlan.txt`](../configs/switch/02-vlan.txt)
3. [`../configs/switch/03-trunk-portsecurity.txt`](../configs/switch/03-trunk-portsecurity.txt)
4. [`../configs/router/router-on-a-stick.txt`](../configs/router/router-on-a-stick.txt)

## 5. Doğrulama

- Port ışıklarının turuncudan yeşile dönmesi (STP dinleme/öğrenme tamamlanması) beklenir.
- **Realtime Mode:** PC-0'dan PC-1'e `ping 192.168.1.20` çalıştırılır.
- **Simulation Mode:** Event List filtresine yalnızca `ICMP` ve `ARP` seçilerek paketin adım adım (ARP Broadcast → Unicast yanıt → ICMP Echo Request/Reply) izlenmesi sağlanır; her cihazdaki PDU penceresinden OSI katman başlıkları incelenir.
- Switch CLI üzerinde `show mac address-table` ile CAM tablosunun dinamik öğrenmesi doğrulanır.
