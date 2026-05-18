# Unmanic

Category: **Media**  
Recommended target: **VM102**  
Image: `josh5/unmanic:latest`  
Maturity: **starter**

## Summary

Simple automatic video library optimizer/transcoder.

## One-click guidance

Easier than Tdarr, but still needs careful media path and plugin setup.

## Recommended use

This replaces the previous Stash entry with a general-purpose video platform component suitable for normal video libraries, YouTube archives, media requests, and transcoding workflows.

## Deploy checklist

1. Review `.env.example`.
2. Set `MEDIA_PATH` to your NAS/media path.
3. Deploy through Arcane.
4. Add Uptime Kuma monitor if important.
