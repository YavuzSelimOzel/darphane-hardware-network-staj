# 9. İşletim Sistemi Güvenlik Duvarı (Host-Based Firewall) Yapılandırması

**Tarih:** 28/07/2026 (Staj Günü 16)

## Kavramsal Çerçeve

Windows Defender Firewall with Advanced Security (WFAS) konsolu üzerinden incelenen bileşenler:

- **Inbound Rules** (gelen bağlantı kuralları) / **Outbound Rules** (giden bağlantı kuralları)
- **Profil Yapıları:** Domain, Private, Public
- **Stateful Packet Inspection:** bağlantı durumunu takip ederek karar verme

## Uygulanan Güvenlik Politikası

1. **Keşif/Tarama Gizliliği:** Varsayılan ICMPv4 (Echo Request) Inbound izin kuralı devre dışı bırakılıp **Block** kuralı tanımlandı → cihaz dışarıdan ping ile keşfedilemez hale geldi.
2. **Kısıtlayıcı Port Filtreleme:** Yalnızca uzaktan yönetim için gereken güvenli portlara izin verildi:
   - **RDP** (Remote Desktop Protocol) — TCP 3389
   - **SSH** (Secure Shell) — TCP 22
   - Bunlar dışındaki tüm tanınmayan TCP/UDP bağlantı talepleri kısıtlandı.

Uygulama script'i: [`scripts/windows-firewall-rules.ps1`](../scripts/windows-firewall-rules.ps1)

## Doğrulama Testleri (Penetrasyon/Erişim Testi)

| Test | Beklenen Sonuç | Gözlem |
|---|---|---|
| `ping <hedef_ip>` | Request Timed Out | ✅ Engellendi |
| RDP bağlantısı (3389) | Bağlanabilir | ✅ Kesintisiz çalıştı |
| SSH bağlantısı (22) | Bağlanabilir | ✅ Kesintisiz çalıştı |
| Tanımsız port (örn. 8080) | Reddedilir | ✅ Reddedildi |
