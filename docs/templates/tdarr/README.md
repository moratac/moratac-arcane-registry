# Tdarr

Category: **Media**  
Recommended target: **VM102**  
Image: `ghcr.io/haveagitgat/tdarr:latest`  
Maturity: **review**

> ⚠️ Review before deploy. This template may need supporting services or careful media path setup.

## Summary

Distributed video transcoding, library optimization, and codec normalization platform.

## One-click guidance

Needs careful library path mapping and optional GPU transcoding setup.

## Recommended use

This replaces the previous Stash entry with a general-purpose video platform component suitable for normal video libraries, YouTube archives, media requests, and transcoding workflows.

## Deploy checklist

1. Review `.env.example`.
2. Set `MEDIA_PATH` to your NAS/media path.
3. Deploy through Arcane.
4. Add Uptime Kuma monitor if important.
