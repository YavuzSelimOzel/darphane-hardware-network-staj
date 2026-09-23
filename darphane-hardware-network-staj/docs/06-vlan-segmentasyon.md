# 6. VLAN Segmentasyonu ve Katman 2 İzolasyon Testleri

**Tarih:** 21/07/2026 – 22/07/2026 (Staj Günü 11–12)

## Amaç

Ağ üzerindeki gereksiz broadcast trafiğini sınırlamak, bant genişliği verimliliğini artırmak ve farklı birimler (Personel / Misafir) arasında Katman 2 düzeyinde erişim kontrolü sağlayarak ağ güvenliğini artırmak.

## Konfigürasyon

Varsayılan olarak tüm switch portları VLAN 1 üyesidir ve aynı broadcast domain'ini paylaşır. Bu nedenle:

- `vlan 10` → **PERSONEL**
- `vlan 20` → **MISAFIR**

PC-1 (Fa0/1) → VLAN 10, PC-2 (Fa0/2) → VLAN 20 access moduna atanmıştır.

Detaylı komutlar: [`configs/switch/02-vlan.txt`](../configs/switch/02-vlan.txt)

## İzolasyon Doğrulama Testi

PC-1'den PC-2'ye `ping 192.168.1.20` komutu çalıştırılmış:

| Sonuç | Gözlem |
|---|---|
| Paket iletimi | **Başarısız** — 4 paketin %100'ü kayıp |
| Hata mesajı | `Request Timed Out` |
| Packet Tracer Simulation Mode analizi | Switch, Fa0/1 (VLAN 10) portundan gelen çerçeveyi Fa0/2 (VLAN 20) portuna iletmiyor — Katman 2 seviyesinde veri geçişi doğrudan engelleniyor |

## Sonuç

Ek bir fiziksel switch veya donanımsal maliyet oluşturmadan, sadece **yazılımsal VLAN yapılandırması** ile kurumsal ağda birimler arası yüksek seviyeli güvenlik izolasyonu ve bant genişliği verimliliği uygulamalı olarak doğrulanmıştır.

> İzolasyonun kaldırılıp kontrollü haberleşmenin sağlanması için bkz. [`07-inter-vlan-routing.md`](07-inter-vlan-routing.md)
