# Soft Router Guide

These are not Arcane one-click Docker templates because they are router operating systems. Install them as Proxmox VMs, bare-metal router OSes, or appliance images.

| Option | Best role | Recommendation | Source |
|---|---|---|---|
| OPNsense | Main production gateway/firewall | Best default choice | https://opnsense.org/ |
| OpenWrt | Lightweight router / side-router | Best lightweight/experimental choice | https://openwrt.org/ |
| iStoreOS | OpenWrt-based friendly app-router UI | Best Chinese-friendly OpenWrt derivative | https://www.istoreos.com/ |
| pfSense | Classic enterprise firewall | Stable, but secondary choice here | https://www.pfsense.org/ |

## Recommended plan

1. Deploy OPNsense first as a Proxmox VM in lab mode.
2. Use a test subnet before replacing your real gateway.
3. Use OpenWrt or iStoreOS later as a side-router/experiment node.
4. Keep Arcane for Docker apps, not router OS management.
