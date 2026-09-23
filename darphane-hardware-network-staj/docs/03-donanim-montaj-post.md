# 3. Donanım Analizi, Montaj ve POST Doğrulaması

**Tarih:** 07/07/2026 – 08/07/2026 (Staj Günü 2–3)

## İSG ve ESD Güvenlik Önlemleri

Hassas elektronik bileşenler üzerinde çalışırken Elektrostatik Deşarj (ESD) riskine karşı antistatik mat ve ESD bilekliği kullanılmıştır.

## Donanım Bileşen Analizi

İki adet istemci test bilgisayarının donanım bileşenleri sökülerek incelenmiştir:

| Bileşen | Detay |
|---|---|
| Anakart (Motherboard) | Mimari inceleme, PCIe hatları |
| İşlemci | Intel Core i7, soket yapısı |
| RAM | DDR4, çift kanal (Dual-Channel) — DIMM A2/B2 yuvaları |
| Depolama | NVMe M.2 SSD, doğrudan PCIe veriyolu |
| Ağ Kartı (NIC) | Gigabit Ethernet |

Arızalı donanım tespiti için sinyal ve bip kodları (Beep Codes) teknik dokümanlardan incelenmiştir.

## Montaj Adımları

1. Kasa iç toz temizliği (basınçlı hava, antistatik fırça)
2. CPU soğutucu sökümü, eski termal macun temizliği (izopropil alkol), yeni termal macun uygulaması
3. Soğutucu fan bağlantısı — CPU_FAN soketi, tork değerlerine dikkat
4. RAM modüllerinin DIMM A2/B2 yuvalarına yerleştirilmesi (Dual-Channel aktivasyonu)
5. NVMe M.2 SSD montajı, soğutucu blok sabitleme
6. PSU güç kabloları — 24-Pin ATX ana güç, 8-Pin CPU güç
7. Kablo düzenleme (Cable Management) — kasa içi hava akışını engellememesi için

## POST (Power-On Self-Test) Doğrulaması

İlk güç verildikten sonra DEL/F2 ile BIOS/UEFI arayüzüne girilerek kontrol edilenler:

- İşlemci frekansı, çekirdek sıcaklığı, voltaj değerleri
- RAM modüllerinin XMP/DOCP profil frekans değerleri ve toplam kapasite
- M.2 SSD S.M.A.R.T. sağlık parametreleri ve PCIe hat çalışma modu
- Sistem fan devir hızları (RPM)
- Boot Order — harici USB medyaların ilk sıraya alınması (OS kurulumuna hazırlık)

Stres ve kararlılık testleri sonucunda donanımsal bileşenlerin sorunsuz çalıştığı doğrulanmıştır.
