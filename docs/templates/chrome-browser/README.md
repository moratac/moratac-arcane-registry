# Chrome Browser

Category: **Developer Tools**  
Recommended target: **VM104**  
Image: `lscr.io/linuxserver/chromium:latest`  
Maturity: **ready**

## Summary

Browser in container. Chromium image used as Chrome-compatible option.

## Deploy checklist

1. Review `.env.example`.
2. Edit ports, secrets, domain values, and storage paths.
3. Confirm target VM role matches this app.
4. Deploy through Arcane Templates or Projects.

## Ownership rule

- Runtipi-managed apps: observe in Arcane, but avoid editing/updating from Arcane unless intentionally migrating ownership.
- Arcane-managed apps: deploy/update through Arcane.
- High-risk apps: AI agents, browsers, downloaders, redroid, Virtual DSM, LanCache, GPU inference.
