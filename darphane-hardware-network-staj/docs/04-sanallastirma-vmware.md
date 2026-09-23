# 4. Sanallaştırma Mimarisi ve VMware Kurulumu

**Tarih:** 09/07/2026, 24/07/2026, 27/07/2026 (Staj Günü 4, 14, 15)

## Hypervisor Mimarileri

| Tip | Tanım | Örnekler |
|---|---|---|
| Bare-Metal / Native (Type-1) | Doğrudan fiziksel donanım üzerine kurulur, ev sahibi OS gerektirmez | VMware ESXi, Proxmox VE, Hyper-V Server |
| Hosted (Type-2) | Mevcut bir ev sahibi (Host) işletim sistemi üzerinde uygulama gibi çalışır | VMware Workstation, Oracle VirtualBox |

Donanım Soyutlama Katmanı (HAL) ile CPU/RAM/depolama kaynaklarının VM'lere mantıksal dağıtımı ve Thin Provisioning (dinamik disk tahsisi) yöntemleri incelenmiştir.

## BIOS/UEFI Sanallaştırma Ayarları

Advanced CPU Configuration menüsünden:
- **Intel VT-x** (Virtualization Technology) → Enabled
- **Intel VT-d** (Direct I/O) → Enabled

## VMware Workstation Pro Kurulumu ve VM Konfigürasyonu

İlk sanal makine (New Virtual Machine Wizard) şu kaynaklarla oluşturulmuştur:

| Kaynak | Değer |
|---|---|
| vCPU | 2 çekirdek (1 Socket - 2 Cores) |
| vRAM | 4 GB |
| vDK (Sanal Disk) | 40 GB, Thin Provisioned (.vmdk) |

Kurulum sonrası **VMware Tools** paketi yüklenerek grafik/fare/ağ adaptörü performans testleri yapılmıştır.

## Hibrit Ağ Entegrasyonu (Bridged Mode)

Virtual Network Editor üzerinde vNIC **Bridged (Köprü)** moda alınarak, sanal makinenin fiziksel Host NIC ile Katman 2 seviyesinde eşleşmesi sağlanmıştır.

- Sanal makineye statik IP: **192.168.1.30/24**
- Trafik akışı: VM → vSwitch0 → PC-1 Fiziksel NIC → Cat6 UTP → Cisco Switch → PC-2 (192.168.1.20)

### Doğrulama Testleri

- ICMP ping testi: VM (192.168.1.30) ↔ PC-2 (192.168.1.20) — başarılı, paket kaybı yok
- Katman 7 servis testi: VM ↔ PC-2 arası **SMB (TCP/445)** protokolü ile paylaşımlı klasör erişimi ve dosya aktarımı — başarılı

Bu çalışma, sanallaştırılmış bir sunucu altyapısının fiziksel ağ donanımları üzerinden gerçek dünya cihazlarıyla sorunsuz haberleşebildiğini kanıtlamıştır.
