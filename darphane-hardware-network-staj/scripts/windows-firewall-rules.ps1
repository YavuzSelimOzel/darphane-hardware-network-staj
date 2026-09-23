<#
=====================================================================
 Windows Defender Firewall (WFAS) - Inbound/Outbound Port Filtreleme
 Kaynak: Staj Günü 16 (28/07/2026)

 Amaç:
   1) Cihazın dışarıdan keşif/tarama (ICMP ping) faaliyetlerine karşı
      "gizlenmesi" — varsayılan ICMP Echo Request Inbound kuralı
      devre dışı bırakılır ve engelleme kuralı eklenir.
   2) Yalnızca yönetim amaçlı güvenli servislere (RDP, SSH) izin
      verilir; bunlar dışındaki tüm portlar kapalı kalır.

 Çalıştırma: PowerShell'i Yönetici (Administrator) olarak açıp
   .\windows-firewall-rules.ps1 komutuyla çalıştırınız.
=====================================================================
#>

# --- 1) ICMPv4 (ping) isteklerini engelle ---
New-NetFirewallRule -DisplayName "Darphane-Block-ICMPv4-Echo" `
    -Direction Inbound `
    -Protocol ICMPv4 `
    -IcmpType 8 `
    -Action Block `
    -Profile Any

# --- 2) RDP (Uzak Masaüstü) yönetim erişimine izin ver ---
New-NetFirewallRule -DisplayName "Darphane-Allow-RDP" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 3389 `
    -Action Allow `
    -Profile Any

# --- 3) SSH ile güvenli komut satırı yönetimine izin ver ---
New-NetFirewallRule -DisplayName "Darphane-Allow-SSH" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 22 `
    -Action Allow `
    -Profile Any

# --- 4) Syslog (UDP 514) trafiğine izin ver (log toplama için) ---
New-NetFirewallRule -DisplayName "Darphane-Allow-Syslog" `
    -Direction Inbound `
    -Protocol UDP `
    -LocalPort 514 `
    -Action Allow `
    -Profile Any

Write-Host "Firewall kuralları başarıyla uygulandı." -ForegroundColor Green
Write-Host "Doğrulamak için: Get-NetFirewallRule -DisplayName 'Darphane-*'" -ForegroundColor Cyan

<#
=====================================================================
 Doğrulama testleri:
   - Karşı bilgisayardan: ping <bu_makine_ip>          -> Request timed out (beklenen)
   - Karşı bilgisayardan: mstsc /v:<bu_makine_ip>       -> Bağlanabilmeli
   - Karşı bilgisayardan: ssh user@<bu_makine_ip>       -> Bağlanabilmeli
   - Tanımsız bir port (örn. 8080) üzerinden bağlantı   -> Reddedilmeli
=====================================================================
#>
