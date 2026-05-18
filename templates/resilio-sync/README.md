# Resilio Sync

Category: **Storage & Sync**  
Recommended target: **VM101**  
Image: `lscr.io/linuxserver/resilio-sync:latest`  
Maturity: **ready**

## Summary

P2P file synchronization based on BitTorrent technology.

## Deploy checklist

1. Review `.env.example`.
2. Edit ports, secrets, domain values, and storage paths.
3. Confirm target VM role matches this app.
4. Deploy through Arcane Templates or Projects.

## Ownership rule

- Runtipi-managed apps: observe in Arcane, but avoid editing/updating from Arcane unless intentionally migrating ownership.
- Arcane-managed apps: deploy/update through Arcane.
- High-risk apps: AI agents, browsers, downloaders, redroid, Virtual DSM, LanCache, GPU inference.
