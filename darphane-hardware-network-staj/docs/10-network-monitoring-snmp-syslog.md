# 10. SNMP / Syslog ile Ağ İzleme ve Log Yönetimi

**Tarih:** 30/07/2026 (Staj Günü 18)

## Kavramsal Çerçeve

- **SNMP** (Simple Network Management Protocol): MIB (Management Information Base) ve OID (Object Identifier) kavramlarıyla cihaz durumunun merkezi izlenmesi
- **Syslog** (System Logging Protocol): Ağ cihazlarının bellekte (RAM) tuttuğu log kayıtları, cihaz yeniden başlatıldığında kaybolur → kurumsal güvenlik standartları gereği logların **merkezi bir sunucuda** toplanması gerekir

## Switch Tarafı Konfigürasyonu

- `logging host <syslog_sunucu_ip>` — log mesajlarının merkezi sunucuya yönlendirilmesi
- `logging trap informational` — log detay seviyesi (seviye 6)
- `service timestamps log datetime msec` — zaman damgalı kayıt

Konfigürasyon: [`configs/switch/04-snmp-syslog.txt`](../configs/switch/04-snmp-syslog.txt)

## Merkezi Log Toplama Aracı

Projede, gerçekten çalışan bir Python tabanlı Syslog dinleyici geliştirilmiştir: [`scripts/syslog_listener.py`](../scripts/syslog_listener.py)

Özellikleri:
- UDP 514 portunu dinler, gelen RFC3164 formatlı log mesajlarını ayrıştırır (facility/severity)
- Olay tipini otomatik sınıflandırır: `LINK_DOWN`, `LINK_UP`, `UNAUTHORIZED_LOGIN_ATTEMPT`, `PORT_SECURITY_VIOLATION`, `CONFIG_CHANGED`
- Terminalde renkli olarak gösterir, `logs-sample/` klasörüne kalıcı olarak kaydeder
- Çıkışta olay özetini (kaç adet hangi tip olay) raporlar

## Test Senaryoları ve Doğrulanan Log Çıktıları

| Senaryo | Üretilen Log |
|---|---|
| Port düşmesi (`shutdown`) / kalkması (`no shutdown`) | `%LINK-3-UPDOWN: Interface FastEthernet0/1, changed state to down/up` |
| Hatalı parola ile yetkisiz erişim denemesi | `%SEC_LOGIN-4-LOGIN_FAILED` |

Bu loglar UDP 514 üzerinden `syslog_listener.py`'ye anlık ve eksiksiz olarak ulaştığı doğrulanarak ağ izleme mekanizmasının sorunsuz çalıştığı kanıtlanmıştır.
