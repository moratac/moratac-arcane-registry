# Overseerr

Category: **Download & ARR**  
Recommended target: **VM102**  
Image: `lscr.io/linuxserver/overseerr:latest`  
Maturity: **ready**

## Summary

Media request portal commonly used with Plex/Radarr/Sonarr; can still fit broader ARR workflows.

## One-click guidance

Good one-click candidate; best with Plex but useful as request-portal reference.

## Recommended use

This replaces the previous Stash entry with a general-purpose video platform component suitable for normal video libraries, YouTube archives, media requests, and transcoding workflows.

## Deploy checklist

1. Review `.env.example`.
2. Set `MEDIA_PATH` to your NAS/media path.
3. Deploy through Arcane.
4. Add Uptime Kuma monitor if important.
