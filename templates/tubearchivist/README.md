# TubeArchivist

Category: **Media**  
Recommended target: **VM102**  
Image: `bbilly1/tubearchivist:latest`  
Maturity: **review**

> ⚠️ Review before deploy. This template may need supporting services or careful media path setup.

## Summary

Self-hosted YouTube archive with metadata, channel sync, subtitles, and indexing.

## One-click guidance

Needs companion services such as Redis/Elasticsearch in production; use for content you have rights to archive.

## Recommended use

This replaces the previous Stash entry with a general-purpose video platform component suitable for normal video libraries, YouTube archives, media requests, and transcoding workflows.

## Deploy checklist

1. Review `.env.example`.
2. Set `MEDIA_PATH` to your NAS/media path.
3. Deploy through Arcane.
4. Add Uptime Kuma monitor if important.
