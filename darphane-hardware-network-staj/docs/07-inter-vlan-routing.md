# 7. Inter-VLAN Routing (Router-on-a-Stick) ve PDU/OSI Analizi

**Tarih:** 17/07/2026, 20/07/2026, 23/07/2026 (Staj Günü 9, 10, 13)

## Cisco Packet Tracer Dijital İkiz

Fiziksel ortamda kurulan 2 PC + 1 Switch topolojisinin Cisco Packet Tracer üzerinde birebir dijital ikizi (Digital Twin) tasarlanmıştır. Ayrıntılar: [`packet-tracer/topology-description.md`](../packet-tracer/topology-description.md)

## PDU (Protocol Data Unit) Analizi — Simulation Mode

PC-0 (192.168.1.10) → PC-1 (192.168.1.20) arasına ICMP Echo Request paketi gönderilerek adım adım izlenmiştir:

1. **Katman 3 (Network):** Kaynak IP 192.168.1.10, Hedef IP 192.168.1.20
2. **Katman 2 (Data Link):** Ethernet II çerçeve yapısı — Kaynak/Hedef MAC adresleri
3. **ARP/Broadcast Süreci:** Hedef MAC bilinmediğinde ARP Broadcast (FF:FF:FF:FF:FF:FF) yayımlanır; Switch, gelen port hariç tüm portlara iletir (Flooding); PC-1'den dönen Unicast ARP yanıtı ile ARP tablosu güncellenir
4. **Switch CAM Tablosu:** Switch, gelen çerçevenin Kaynak MAC adresini okuyarak CAM (Content Addressable Memory) tablosuna port eşleşmesiyle kaydeder

Doğrulama: `show mac address-table`

## Router-on-a-Stick ile Inter-VLAN Routing

VLAN 10 (PERSONEL) ve VLAN 20 (MISAFIR) arasında kontrollü haberleşme için:

- **IEEE 802.1Q Trunking:** Switch–Router hattı tek fiziksel bağlantı üzerinden birden fazla VLAN trafiği taşır
- **Sub-interface (Alt-arayüz) mimarisi:**
  - `Gi0/0/0.10` → `encapsulation dot1Q 10` → Gateway 192.168.10.1/24
  - `Gi0/0/0.20` → `encapsulation dot1Q 20` → Gateway 192.168.20.1/24

Konfigürasyon: [`configs/router/router-on-a-stick.txt`](../configs/router/router-on-a-stick.txt)

### Doğrulama

PC-1 (VLAN 10) → PC-2 (VLAN 20) ping testi: ilk paket ARP çözümlemesi nedeniyle düşer, sonraki ICMP Echo Reply'ler eksiksiz alınır — Katman 2'de izole edilmiş VLAN'ların Katman 3 router üzerinden başarıyla haberleştiği doğrulanmıştır.
