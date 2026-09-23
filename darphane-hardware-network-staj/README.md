# Darphane ve Damga Matbaası Genel Müdürlüğü — Bilgi İşlem Daire Başkanlığı Donanım Stajı Projesi

**Öğrenci:** Yavuz Selim Özel — Bilgisayar Mühendisliği, 4. Sınıf (No: 16008123167)  
**GitHub:** [YavuzSelimOzel](https://github.com/YavuzSelimOzel)
**Kurum:** T.C. Hazine ve Maliye Bakanlığı — Darphane ve Damga Matbaası Genel Müdürlüğü
**Birim:** Bilgi İşlem Daire Başkanlığı — Ağ ve Sistem Yönetimi (Donanım, Sanallaştırma ve Siber Güvenlik)
**Staj Süresi:** 20 iş günü (06.07.2026 – 03.08.2026)
**Kılavuz Uyumu:** Bilgisayar Mühendisliği Bölümü Uygulamalı Eğitimler Komisyonu Donanım Stajı Esasları Kılavuzu — **D-3** (Bilgisayar Ağ Donanımlarının Tasarımı, Konfigürasyonu, Yönetilmesi ve Test Edilmesi) ve **D-4** (Sistem Kurulumu, Sanallaştırma ve Donanım Kaynakları Analizi) maddeleri

---

## 1. Projenin Amacı

Bu depo, Darphane ve Damga Matbaası Genel Müdürlüğü Bilgi İşlem Daire Başkanlığı bünyesinde gerçekleştirilen 20 günlük donanım stajı süresince yapılan tüm teknik çalışmaların (donanım montajı, sanallaştırma, switch/router konfigürasyonu, VLAN segmentasyonu, güvenlik politikaları, ağ izleme ve sorun giderme) **yeniden üretilebilir, dokümante edilmiş ve test edilebilir** bir mühendislik projesi haline getirilmiş hâlidir. Depo hem GitHub'da barındırılmak hem de staj sonunda Uygulamalı Eğitimler Komisyonu'na sunulmak üzere hazırlanmıştır.

## 2. Kurum Tanıtımı

T.C. Hazine ve Maliye Bakanlığı'na bağlı bir kamu kuruluşu olan Darphane ve Damga Matbaası Genel Müdürlüğü; Türkiye Cumhuriyeti'nin tedavül ve hatıra madeni paralarının basımı, cumhuriyet altınlarının üretimi, resmi mühürlerin imalatı, pasaport/sürücü belgesi/kimlik kartı gibi değerli belgelerin basımı ile Nitelikli Elektronik Sertifika ve Bilişim Sistemleri entegrasyon süreçlerini yürütmektedir. Üretim süreçlerinin yüksek güvenlik gerektirmesi nedeniyle bilişim altyapısının kesintisiz, güvenli ve sürdürülebilir olması esastır.

Bilgi İşlem Daire Başkanlığı üç alt birimden oluşur:
- **Sistem ve Sanallaştırma Şube Müdürlüğü** — veri merkezi sunucuları, depolama (SAN/NAS), yedekleme, Hypervisor mimarileri
- **Ağ ve Siber Güvenlik Şube Müdürlüğü** — core/kenar switch, firewall, VPN, VLAN segmentasyonu, ACL ve güvenlik politikaları
- **Donanım ve Teknik Destek Birimi** — istemci donanımı, kurulum, bakım ve arıza tespiti

## 3. Proje Mimarisi (Özet)

```
2x İstemci PC ──(Cat6 UTP)── Cisco Kat-2 Yönetilebilir Switch ──(Trunk, 802.1Q)── Router (Router-on-a-Stick)
        │                              │
   VMware Workstation Pro         VLAN 10 (PERSONEL) / VLAN 20 (MISAFIR)
   (Bridged vNIC → vSwitch0)      Port Security + SNMP/Syslog + Port Filtering
```

Ayrıntılı diyagram: [`diagrams/network-topology.md`](diagrams/network-topology.md)

## 4. Klasör Yapısı

| Klasör/Dosya | İçerik |
|---|---|
| `docs/` | Her çalışma başlığı için ayrıntılı teknik dokümantasyon (12 bölüm) |
| `configs/switch/` | Cisco IOS switch konfigürasyon dosyaları (baseline, VLAN, trunk/port-security, SNMP/Syslog) |
| `configs/router/` | Router-on-a-Stick alt-arayüz (sub-interface) konfigürasyonu |
| `scripts/windows-firewall-rules.ps1` | Windows Defender Firewall (WFAS) Inbound/Outbound kural script'i |
| `scripts/syslog_listener.py` | UDP 514 üzerinden çalışan, gerçek zamanlı Syslog dinleyici ve log analiz aracı (Python) |
| `diagrams/network-topology.md` | Mermaid ile çizilmiş ağ topolojisi ve VLAN şeması |
| `packet-tracer/topology-description.md` | Cisco Packet Tracer dijital ikiz topolojisinin adım adım yeniden kurulum talimatı |
| `logs-sample/` | Örnek Syslog çıktısı (test/demo amaçlı) |

## 5. Gün Gün Çalışma Özeti

| Gün | Tarih | Konu | İlgili Dosya |
|---|---|---|---|
| 1 | 06/07/2026 | Kurum oryantasyonu, bilgi güvenliği, BİDB altyapı incelemesi | `docs/01-kurum-tanitimi.md` |
| 2 | 07/07/2026 | İSG/ESD eğitimi, donanım bileşen analizi | `docs/03-donanim-montaj-post.md` |
| 3 | 08/07/2026 | Test PC montajı, termal bakım, POST/BIOS doğrulama | `docs/03-donanim-montaj-post.md` |
| 4 | 09/07/2026 | Hypervisor mimarileri, VMware Workstation kurulumu, VM konfigürasyonu | `docs/04-sanallastirma-vmware.md` |
| 5 | 10/07/2026 | Fiziksel switch bağlantıları, port senkronizasyon testleri | `docs/05-switch-temel-konfigurasyon.md` |
| 6 | 13/07/2026 | IPv4 adresleme, statik IP tanımlama | `docs/05-switch-temel-konfigurasyon.md` |
| 7 | 14/07/2026 | ICMP/ARP testleri, komut satırı sorun giderme | `docs/11-wireshark-analiz-troubleshooting.md` |
| 8 | 16/07/2026 | Switch CLI, temel güvenlik, yönetim IP'si (SVI) | `configs/switch/01-baseline.txt` |
| 9 | 17/07/2026 | Cisco Packet Tracer dijital ikiz tasarımı | `packet-tracer/topology-description.md` |
| 10 | 20/07/2026 | PDU/OSI katman analizi, CAM tablosu | `docs/07-inter-vlan-routing.md` |
| 11 | 21/07/2026 | VLAN 10/20 tanımlama, access port konfigürasyonu | `configs/switch/02-vlan.txt` |
| 12 | 22/07/2026 | VLAN izolasyon testleri (Katman 2 doğrulama) | `docs/06-vlan-segmentasyon.md` |
| 13 | 23/07/2026 | 802.1Q Trunking, Router-on-a-Stick, Inter-VLAN Routing | `configs/router/router-on-a-stick.txt` |
| 14 | 24/07/2026 | VM–fiziksel ağ entegrasyonu (Bridged mod) | `docs/04-sanallastirma-vmware.md` |
| 15 | 27/07/2026 | Hibrit ağ haberleşme testleri (SMB) | `docs/04-sanallastirma-vmware.md` |
| 16 | 28/07/2026 | Windows Defender Firewall Inbound/Outbound kuralları | `scripts/windows-firewall-rules.ps1` |
| 17 | 29/07/2026 | Wireshark paket analizi, arıza senaryoları | `docs/11-wireshark-analiz-troubleshooting.md` |
| 18 | 30/07/2026 | SNMP/Syslog ile ağ izleme, log yönetimi | `configs/switch/04-snmp-syslog.txt`, `scripts/syslog_listener.py` |
| 19 | 31/07/2026 | Port Security, sticky MAC, err-disable | `configs/switch/03-trunk-portsecurity.txt` |
| 20 | 03/08/2026 | Proje sonuç raporu, kurum onay süreçleri | `docs/12-sonuc-degerlendirme.md` |

## 6. Komisyon Değerlendirme Kriterleriyle Eşleştirme

Staj defterindeki resmi değerlendirme tablosuna göre bu depo şu başlıkları karşılar:

| Kriter | Bu Depodaki Karşılığı |
|---|---|
| Kurumun Tanıtımı | Bölüm 2 (yukarıda) + `docs/01-kurum-tanitimi.md` |
| İş Planı Yazımı | Bölüm 5 tablosu + `docs/` altındaki 12 doküman |
| Staj Değerlendirmesi | `docs/12-sonuc-degerlendirme.md` |
| Sunum Biçimi | Diyagramlar, config dosyaları, çalışan Python aracı ile somut kanıt |
| İmla ve Dil Kurallarına Uyum | Tüm dokümanlar Türkçe teknik yazım kurallarına uygun hazırlanmıştır |

## 7. GitHub'a Yükleme

```bash
cd darphane-hardware-network-staj
git init
git add .
git commit -m "Darphane BİDB Donanım Stajı - Ağ ve Sistem Yönetimi Projesi"
git branch -M main
git remote add origin https://github.com/YavuzSelimOzel/darphane-hardware-network-staj.git
git push -u origin main
```

## 8. Notlar

- Konfigürasyon dosyaları gerçek Cisco IOS komut sözdizimi ile yazılmıştır; bir Cisco 2960 Katman-2 switch veya Cisco Packet Tracer üzerinde doğrudan uygulanabilir.
- `scripts/syslog_listener.py` gerçekten çalışan bir araçtır — `python3 syslog_listener.py` ile başlatılıp switch/router üzerinden `logging host <bu_makinenin_ip'si>` komutuyla gönderilen logları gerçek zamanlı toplar ve `logs-sample/` klasörüne kaydeder.
- Öğrenci imzası ve kurum kaşesi bu dijital projeye dahil edilmemiştir; bunlar fiziksel staj defterinde ıslak imza/kaşe ile tamamlanmıştır.
- Konfigürasyon dosyalarındaki parolalar ve SNMP community değeri güvenlik nedeniyle `<...>` biçiminde yer tutucu olarak bırakılmıştır; uygularken kendi değerlerinizle değiştiriniz.
