# Moratac Arcane Registry

Curated Docker Compose templates for [Arcane](https://getarcane.app).

## Registry URL

```text
https://moratac.github.io/moratac-arcane-registry/registry.json
```

## Features

- Arcane registry schema compatible
- GitHub Pages static hosting for registry, compose files, env files, and icons
- Localized Arcane UI icons via `x-arcane.icon`
- Full Docker Compose files restored from clean v1.0 source
- `pull_policy: always` added after image declarations
- `TZ=UTC` defaults with compose-level `${TZ:-UTC}` where supported
- `DATA_PATH=./data` convention in `.env.example`
- Version bumped to `2.1.1`

## Featured Apps

| App | Category |
|---|---|
| Arcane | Platform |
| Authentik | Security & Identity |
| Caddy Server | Networking & Reverse Proxy |
| Caddy Server Stack | Networking & Reverse Proxy / Experimental |
| File Browser | Storage & Files |
| Homarr | Dashboard |
| Homepage | Dashboard |
| Immich | Media |
| IT-Tools | Developer Tools |
| Jellyfin | Media |
| NextExplorer | Storage & Files |
| Open WebUI | AI & Automation |
| SFTPGo | Storage & Files |
| Uptime Kuma | Monitoring |

## Categories

### AI & Automation

| App | Description |
|---|---|
| AnythingLLM | Private RAG and AI workspace. |
| BabelDuck | AI language/productivity tool placeholder; verify upstream image before use. |
| Dify | LLM app platform. Full production stack requires multiple services. |
| Hermes Agent | Hermes Agent. Verify official image and compose before production use. |
| n8n | Workflow automation. |
| Open WebUI | Web UI for Ollama and OpenAI-compatible APIs. |
| OpenClaw | AI agent platform. High privilege; review official docs before deploy. |

### AI Inference

| App | Description |
|---|---|
| llama.cpp Server | llama.cpp HTTP server. CPU/GPU variants may differ. |
| LM Studio | LM Studio is usually desktop-native; template is an external service placeholder. |
| SGLang | High-performance LLM serving runtime. GPU recommended. |
| vLLM | High-throughput OpenAI-compatible LLM inference server. GPU recommended. |

### Business & Finance

| App | Description |
|---|---|
| Actual Budget | Self-hosted personal budgeting app. |
| Ghostfolio | Personal finance dashboard. Requires database/Redis for production. |
| Odoo | Business apps / ERP. Includes Postgres service. |
| Wallos | Subscription and recurring expense tracker. |

### Dashboard

| App | Description |
|---|---|
| Homarr | Dashboard for homelab services. |
| Homepage | Highly customizable application dashboard. |

### Developer Tools

| App | Description |
|---|---|
| Brave Browser | Brave browser in container. |
| Chrome Browser | Browser in container. Chromium image used as Chrome-compatible option. |
| Code Server | VS Code in browser. |
| Docker Android | Android emulator in Docker. Replaces Redroid template. |
| IT-Tools | Useful developer and sysadmin web tools. |

### Developer Tools / DevOps

| App | Description |
|---|---|
| Gitea Server | Lightweight self-hosted Git server. Best first choice for homelab Git. |
| GitLab CE | Full-featured self-hosted GitLab Community Edition. |
| Gogs | Very lightweight self-hosted Git service. |

### Download & ARR

| App | Description |
|---|---|
| Aria2 Pro | Aria2 downloader with RPC support. |
| AriaNg | Web UI for Aria2. |
| Bazarr | Subtitle management for Sonarr/Radarr. |
| Jellyseerr | Media request portal for Jellyfin, Sonarr, and Radarr. |
| MeTube | Web UI for yt-dlp video downloads. |
| MoviePilot v2 | Chinese media automation ecosystem. Needs careful env setup. |
| Overseerr | Media request portal commonly used with Plex/Radarr/Sonarr; can still fit broader ARR workflows. |
| Pinchflat | YouTube channel/playlist downloader designed for media-server integration. |
| Prowlarr | Indexer manager for ARR stack. |
| qBittorrent | BitTorrent client. |
| Radarr | Movie management. |
| Sonarr | TV series management. |
| Transmission | BitTorrent client. |

### Gaming & Retro

| App | Description |
|---|---|
| Gameyfin | Game library and download/share manager. |
| RetroAssembly | Browser-based retro game cabinet for personal ROM collections. |
| RomM | ROM library manager with metadata and browser play support. Full stack requires DB/Redis in production. |
| webRcade | Web-based retro gaming frontend placeholder; mount built webRcade files. |

### Home & Family

| App | Description |
|---|---|
| Gramps Web | Family tree and genealogy web app. |
| Grocy | Home ERP for pantry, groceries, chores, and inventory. |
| Homebox | Home inventory and asset manager. |
| Monica | Personal CRM. |

### Media

| App | Description |
|---|---|
| Emby | Media server alternative to Jellyfin. |
| Immich | Photo and video backup system. Full stack requires Postgres and Redis. |
| Jellyfin | Media server. |
| Kavita | Reading server for manga, comics, and books. |
| Komga | Comics and manga server. |
| LANraragi | Archive and manga/doujin library manager. |
| LibreTV | Video aggregation app; source availability may be unstable. |
| MediaCMS | Self-hosted video CMS, like a private YouTube for personal, family, learning, or dataset videos. |
| Streamyfin | Enhanced Jellyfin client ecosystem. Usually client-side/mobile; template is a placeholder/link entry. |
| Suwayomi | Manga source server. |
| Tdarr | Distributed video transcoding, library optimization, and codec normalization platform. |
| TubeArchivist | Self-hosted YouTube archive with metadata, channel sync, subtitles, and indexing. |
| Unmanic | Simple automatic video library optimizer/transcoder. |

### Monitoring

| App | Description |
|---|---|
| Beszel | Lightweight server monitoring hub. |
| Diun | Docker image update notifier. |
| Dozzle | Real-time Docker logs viewer. |
| GoSpeed | Network speed test / file transfer helper. |
| Grafana | Observability dashboard platform. |
| HertzBeat | Universal monitoring platform for HTTP, DB, network, and services. |
| Netdata | Real-time infrastructure monitoring. |
| Uptime Kuma | Self-hosted uptime monitoring. |
| Watchtower | Docker auto-update tool. Recommended notification-only mode first. |

### NAS Infrastructure

| App | Description |
|---|---|
| Virtual DSM | Virtual Synology DSM. Requires KVM/privileged setup; experimental. |

### Networking & Reverse Proxy

| App | Description |
|---|---|
| Caddy Manager | UI for managing Caddy configuration. |
| Caddy Server | Caddy web server and reverse proxy. |
| Caddy Server Stack | Caddy Server + Caddy Manager. Experimental, use with caution. |
| Cloudflare Tunnel | Cloudflare Tunnel connector. |
| LanCache | LAN cache for game/platform downloads. Requires DNS planning. |
| Tailscale | Mesh VPN. Usually installed on host OS; Docker template included for subnet-router/container cases. |

### Office & Collaboration

| App | Description |
|---|---|
| Collabora CODE | LibreOffice Online / Collabora document server. |
| OnlyOffice Docs | Online office document server. |
| Univer | Open-source office/collaboration suite. Verify upstream image for your region. |

### Platform

| App | Description |
|---|---|
| Arcane | Modern Docker management control plane. |
| Arcane Agent | Arcane remote Docker host agent. Verify official pairing flow. |

### Search & RAG

| App | Description |
|---|---|
| Langfuse | LLM observability. Production stack requires supporting services. |
| LiteLLM | LLM gateway/proxy. |
| Qdrant | Vector database for AI/RAG. |
| SearXNG | Privacy-respecting metasearch engine. |

### Security & Identity

| App | Description |
|---|---|
| 2FAuth | Self-hosted TOTP/2FA account manager. |
| Authentik | Identity provider and SSO platform. |
| Safeline WAF | Web application firewall stack. Review official multi-service compose before production. |
| Vaultwarden | Lightweight Bitwarden-compatible password manager. |

### Storage & Files

| App | Description |
|---|---|
| AList | File list and WebDAV gateway for cloud drives and local storage. |
| BaiduNetDisk | Baidu Netdisk desktop client in browser container. |
| File Browser | Web file manager. |
| NextExplorer | Native file browser for mounted NAS paths. |
| OpenCloud | Cloud file collaboration platform. Verify production compose before use. |
| SFTPGo | SFTP, WebDAV and file transfer server. |

### Storage & Sync

| App | Description |
|---|---|
| Resilio Sync | P2P file synchronization based on BitTorrent technology. |
| Syncthing | Open-source peer-to-peer file synchronization. |

## License

MIT
\n## Notes\n\n- Authentik is pinned to a stable patch version. Update `AUTHENTIK_VERSION` manually, then Pull → Redeploy.\n- Caddy Server Stack is experimental. Do not expose Caddy Admin API port 2019 publicly.\n

## Caddy UI Templates

### Caddy UI Zackwag

Experimental Caddy UI with frontend and backend. It is intended to manage an existing Caddy Server through Caddy Admin API.

### Caddy UI Static

Experimental pure static SPA for Caddy Admin API. Best used behind Caddy with HTTPS and BasicAuth.

Production note: keep Caddy Admin API private. Do not expose port 2019 publicly.


## CaddyManager rhad00

Experimental Alpha reverse proxy manager built on Caddy Server.

- Source: https://github.com/rhad00/CaddyManager
- First deploy builds from GitHub source and may take longer.
- Default login: `admin@caddymanager.local` / `changeme123`
- Change the default password immediately.
- Ports are offset to avoid conflict with existing Caddy Server.
