# 2. Proje Mimarisi ve İş Planı

## Kapsam Belirleme

Oryantasyon sonrası, sistem odası erişim yetkilendirme prosedürleri ve teknik dokümantasyon incelenerek staj süresince gerçekleştirilecek projenin kapsamı belirlenmiştir: **2 istemci PC + 1 Yönetilebilir Switch + 1 Router** üzerinde kurulacak, sanallaştırma, VLAN segmentasyonu, güvenlik ve izleme katmanlarını içeren uçtan uca bir kurumsal ağ altyapısı simülasyonu.

## Mimari Katmanlar

| # | Katman | Kapsam | İlgili Belge |
|---|---|---|---|
| 1 | Fiziksel Donanım | İstemci montajı, POST/BIOS doğrulama | `docs/03-donanim-montaj-post.md` |
| 2 | Sanallaştırma | VMware Type-2 Hypervisor, VM kaynak yönetimi | `docs/04-sanallastirma-vmware.md` |
| 3 | Fiziksel Ağ | Kablolama, Switch/Router temel kurulumu, IP adresleme | `docs/05-switch-temel-konfigurasyon.md` |
| 4 | Mantıksal Ağ | VLAN segmentasyonu, Inter-VLAN Routing | `docs/06-vlan-segmentasyon.md`, `docs/07-inter-vlan-routing.md` |
| 5 | Güvenlik | Port Security, Host Firewall | `docs/08-guvenlik-port-security.md`, `docs/09-firewall-windows.md` |
| 6 | İzleme ve Sorun Giderme | SNMP/Syslog, Wireshark | `docs/10-network-monitoring-snmp-syslog.md`, `docs/11-wireshark-analiz-troubleshooting.md` |

Ayrıntılı topoloji diyagramı için bkz. [`diagrams/network-topology.md`](../diagrams/network-topology.md)
