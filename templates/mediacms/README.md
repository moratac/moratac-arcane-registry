# MediaCMS

Category: **Media**  
Recommended target: **VM102**  
Image: `mediacms/mediacms:latest`  
Maturity: **review**

> ⚠️ Review before deploy. This template may need supporting services or careful media path setup.

## Summary

Self-hosted video CMS, like a private YouTube for personal, family, learning, or dataset videos.

## One-click guidance

Production deployment may need Postgres, Redis, workers, and transcoding tuning.

## Recommended use

This replaces the previous Stash entry with a general-purpose video platform component suitable for normal video libraries, YouTube archives, media requests, and transcoding workflows.

## Deploy checklist

1. Review `.env.example`.
2. Set `MEDIA_PATH` to your NAS/media path.
3. Deploy through Arcane.
4. Add Uptime Kuma monitor if important.
