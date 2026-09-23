# 12. Proje Sonuç Raporu ve Staj Değerlendirmesi

**Tarih:** 03/08/2026 (Staj Günü 20)

## Kılavuz Uyumu

Staj çalışması, Bilgisayar Mühendisliği Bölümü Uygulamalı Eğitimler Komisyonu Donanım Stajı Esasları Kılavuzu'nda yer alan **D-3** (Bilgisayar Ağ Donanımlarının Tasarımı, Konfigürasyonu, Yönetilmesi ve Test Edilmesi) ve **D-4** (Sistem Kurulumu, Sanallaştırma ve Donanım Kaynakları Analizi) maddelerine uyumlu, bütünleşik bir Mühendislik Projesi konseptinde yürütülmüştür. Yönetmelikte belirtilen "basit düzeydeki masaüstü kurulumların staj için yetersiz kabul edilmesi" ilkesi dikkate alınarak, tüm teknik çalışmalar katmanlı mimariler ve güvenlik protokolleri çerçevesinde ele alınmıştır.

## Ana Başlıklar Altında Kazanımlar

1. **Donanım ve Sistem Altyapısı Analizi (D-4):** İstemci bilgisayarların fiziki donanım parçaları sökülüp incelenmiş; veri yolu (PCIe) mimarileri ve POST süreçleri analiz edilmiş; BIOS/UEFI seviyesinde donanımsal sanallaştırma (Intel VT-x) aktif edilmiştir.

2. **Sanallaştırma ve Kaynak Yönetimi (D-4):** VMware Type-2 Hypervisor platformu kurularak fiziki kaynakların sanal katmana soyutlanması (vCPU, vRAM, vDK) incelenmiş; sanal makinenin vNIC'i Bridged moda alınarak fiziksel Switch üzerinden dış ağdaki gerçek bilgisayarlarla iletişimi sağlanmıştır.

3. **Fiziksel Ağ, İmalat ve Katman 2/3 Konfigürasyonu (D-3):** UTP Cat6 kablo imalatı T568B standardında gerçekleştirilmiş; 2 PC ve 1 Yönetilebilir Switch ile fiziksel test ağı kurulmuştur. Cisco IOS CLI üzerinden Switch temel güvenlik konfigürasyonları yapılmış; VLAN 10 (PERSONEL) ve VLAN 20 (MISAFIR) ile mantıksal ağ izolasyonu sağlanmış; IEEE 802.1Q Trunking ve Router-on-a-Stick yöntemiyle Inter-VLAN Routing uygulanmıştır.

4. **Cisco Packet Tracer Simülasyonu ve PDU Analizi (D-3):** Kurulan fiziki topolojinin Cisco Packet Tracer üzerinde dijital ikizi modellenmiş; ICMP paketlerinin OSI katmanlarındaki PDU başlık yapıları, Switch'in CAM tablosu doldurma mantığı ve Broadcast/Unicast geçiş süreçleri analiz edilmiştir.

5. **Ağ Güvenliği, İzleme ve Sorun Giderme (D-3):** Switch portlarına Port Security ve sticky MAC adresi sınırlaması uygulanarak izinsiz cihaz erişimlerinde portun err-disable moduna geçmesi sağlanmıştır. Windows Defender Firewall üzerinde Inbound/Outbound port filtreleme kuralları işletilmiştir. Wireshark ile canlı ARP, ICMP ve TCP 3-Way Handshake paketleri izlenmiş; kablo temassızlığı, yanlış VLAN ve IP çakışması gibi arıza senaryolarında OSI katmanları sırasıyla takip edilerek troubleshooting metodolojileri uygulanmıştır.

## Genel Değerlendirme

T.C. Hazine ve Maliye Bakanlığı — Darphane ve Damga Matbaası Genel Müdürlüğü Bilgi İşlem Daire Başkanlığı bünyesinde gerçekleştirilen 20 günlük Donanım Stajı süreci, üniversite eğitimi boyunca edinilen teorik mühendislik bilgilerinin kurumsal, yüksek güvenlikli ve kritik bir kamu altyapısında nasıl karşılık bulduğunu uygulamalı olarak deneyimleme açısından verimli geçmiştir.

Bu staj yalnızca ağ cihazlarının kullanımı konusundaki pratik tecrübeyi artırmakla kalmamış; aynı zamanda kurumsal bir veri merkezindeki bilgi güvenliği kültürünü, sanallaştırmanın donanım verimliliğine katkısını ve bir bilgisayar mühendisinin sahip olması gereken sistemli problem çözme disiplinini kazandırmıştır.

## Proje Çıktılarının Özeti

| Kategori | Çıktı |
|---|---|
| Yapılandırma dosyaları | 4 switch config + 1 router config (gerçek Cisco IOS sözdizimi) |
| Otomasyon/İzleme aracı | Çalışan Python Syslog dinleyicisi, PowerShell Firewall script'i |
| Dokümantasyon | 12 bölümden oluşan teknik doküman seti |
| Diyagram | Mermaid ile ağ topolojisi ve VLAN şeması |
