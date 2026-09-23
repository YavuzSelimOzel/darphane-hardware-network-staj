# 8. Switch Port Güvenliği (Port Security)

**Tarih:** 31/07/2026 (Staj Günü 19)

## Amaç

Kurumsal ağlarda fiziki portlara yetkisiz cihazların (izinsiz kişisel bilgisayarlar veya rogue cihazlar) takılmasını engellemek amacıyla Katman 2 düzeyinde Port Security mimarisi uygulanmıştır.

## Güvenlik Modları

Cisco IOS'ta port ihlali (violation) durumunda uygulanabilecek 3 mod incelenmiştir:

| Mod | Davranış |
|---|---|
| Protect | İzinsiz trafiği sessizce düşürür, log üretmez |
| Restrict | İzinsiz trafiği düşürür + log/SNMP trap üretir |
| **Shutdown** (bu projede kullanılan) | Portu tamamen kapatır (err-disable), manuel müdahale gerektirir |

## Konfigürasyon

FastEthernet 0/1 portu üzerinde uygulanan ayarlar:

- `switchport port-security` — özelliği aktif etme
- `switchport port-security mac-address sticky` — ilk öğrenilen MAC adresini kalıcı olarak kabul etme
- `switchport port-security maximum 1` — porta bağlı olabilecek maksimum cihaz sayısı
- `switchport port-security violation shutdown` — ihlalde portu err-disable moduna alma

Tam konfigürasyon: [`configs/switch/03-trunk-portsecurity.txt`](../configs/switch/03-trunk-portsecurity.txt)

## Test ve Doğrulama

Port üzerine farklı bir MAC adresine sahip izinsiz cihaz bağlama senaryosu simüle edilmiş; Switch'in portu derhal **err-disable** moduna alarak trafiği kestiği doğrulanmıştır. Port durumları ve testler Wireshark üzerinden paket düzeyinde de analiz edilerek rapora kaydedilmiştir.

Doğrulama komutu: `show port-security interface FastEthernet0/1`
