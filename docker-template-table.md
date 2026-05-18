| Category | Template | VM | Maturity | Description | One-click guidance |
|---|---|---|---|---|---|
| AI & Automation | AnythingLLM | VM103 | ready | Private RAG and AI workspace. |  |
| AI & Automation | BabelDuck | VM103 | external | AI language/productivity tool placeholder; verify upstream image before use. |  |
| AI & Automation | Dify | VM103 | review | LLM app platform. Full production stack requires multiple services. |  |
| AI & Automation | Hermes Agent | VM103 | review | Hermes Agent. Verify official image and compose before production use. |  |
| AI & Automation | Open WebUI | VM103 | ready | Web UI for Ollama and OpenAI-compatible APIs. |  |
| AI & Automation | OpenClaw | VM103 | review | AI agent platform. High privilege; review official docs before deploy. |  |
| AI & Automation | n8n | VM103 | ready | Workflow automation. |  |
| AI Inference | LM Studio | Mac/VM103 | external | LM Studio is usually desktop-native; template is an external service placeholder. |  |
| AI Inference | SGLang | VM103 | review | High-performance LLM serving runtime. GPU recommended. |  |
| AI Inference | llama.cpp Server | VM103 | starter | llama.cpp HTTP server. CPU/GPU variants may differ. |  |
| AI Inference | vLLM | VM103 | review | High-throughput OpenAI-compatible LLM inference server. GPU recommended. |  |
| Business & Finance | Actual Budget | VM104 | ready | Self-hosted personal budgeting app. |  |
| Business & Finance | Ghostfolio | VM104 | review | Personal finance dashboard. Requires database/Redis for production. |  |
| Business & Finance | Odoo | VM104 | ready | Business apps / ERP. Includes Postgres service. |  |
| Business & Finance | Wallos | VM104 | ready | Subscription and recurring expense tracker. |  |
| Dashboard | Homarr | VM101 | ready | Dashboard for homelab services. |  |
| Dashboard | Homepage | VM101 | ready | Highly customizable application dashboard. |  |
| Developer Tools | Brave Browser | VM104 | ready | Brave browser in container. |  |
| Developer Tools | Chrome Browser | VM104 | ready | Browser in container. Chromium image used as Chrome-compatible option. |  |
| Developer Tools | Code Server | VM104 | ready | VS Code in browser. |  |
| Developer Tools | IT-Tools | VM101/VM104 | ready | Useful developer and sysadmin web tools. |  |
| Developer Tools | redroid | VM104 | review | Android in Docker. Requires privileged/kernel binder support. |  |
| Developer Tools / DevOps | GitLab CE | VM104 | review | Full-featured self-hosted GitLab Community Edition. | Heavy. Recommend dedicated VM with at least 4C/8G RAM. Review before deployment. |
| Developer Tools / DevOps | Gitea Server | VM104/VM101 | ready | Lightweight self-hosted Git server. Best first choice for homelab Git. | Good one-click candidate. Set ROOT_URL and SSH port before production. |
| Developer Tools / DevOps | Gogs | VM104 | ready | Very lightweight self-hosted Git service. | Good one-click candidate. Lighter than Gitea, smaller ecosystem. |
| Download & ARR | Aria2 Pro | VM102 | ready | Aria2 downloader with RPC support. |  |
| Download & ARR | AriaNg | VM102 | ready | Web UI for Aria2. |  |
| Download & ARR | Bazarr | VM102 | ready | Subtitle management for Sonarr/Radarr. |  |
| Download & ARR | Jellyseerr | VM102 | ready | Media request portal for Jellyfin, Sonarr, and Radarr. | Good one-click candidate; connect to Jellyfin, Sonarr, and Radarr after deployment. |
| Download & ARR | MeTube | VM102 | ready | Web UI for yt-dlp video downloads. |  |
| Download & ARR | MoviePilot v2 | VM102 | review | Chinese media automation ecosystem. Needs careful env setup. |  |
| Download & ARR | Overseerr | VM102 | ready | Media request portal commonly used with Plex/Radarr/Sonarr; can still fit broader ARR workflows. | Good one-click candidate; best with Plex but useful as request-portal reference. |
| Download & ARR | Pinchflat | VM102 | ready | YouTube channel/playlist downloader designed for media-server integration. |  |
| Download & ARR | Prowlarr | VM102 | ready | Indexer manager for ARR stack. |  |
| Download & ARR | Radarr | VM102 | ready | Movie management. |  |
| Download & ARR | Sonarr | VM102 | ready | TV series management. |  |
| Download & ARR | Transmission | VM102 | ready | BitTorrent client. |  |
| Download & ARR | qBittorrent | VM102 | ready | BitTorrent client. |  |
| Gaming & Retro | Gameyfin | VM102 | starter | Game library and download/share manager. |  |
| Gaming & Retro | RetroAssembly | VM102 | starter | Browser-based retro game cabinet for personal ROM collections. |  |
| Gaming & Retro | RomM | VM102 | review | ROM library manager with metadata and browser play support. Full stack requires DB/Redis in production. |  |
| Gaming & Retro | webRcade | VM102 | external | Web-based retro gaming frontend placeholder; mount built webRcade files. |  |
| Home & Family | Gramps Web | VM104 | starter | Family tree and genealogy web app. |  |
| Home & Family | Grocy | VM104 | ready | Home ERP for pantry, groceries, chores, and inventory. |  |
| Home & Family | Homebox | VM104 | ready | Home inventory and asset manager. |  |
| Home & Family | Monica | VM104 | starter | Personal CRM. |  |
| Media | Emby | VM102 | ready | Media server alternative to Jellyfin. |  |
| Media | Immich | VM102 | review | Photo and video backup system. Full stack requires Postgres and Redis. |  |
| Media | Jellyfin | VM102 | ready | Media server. |  |
| Media | Kavita | VM102 | ready | Reading server for manga, comics, and books. |  |
| Media | Komga | VM102 | ready | Comics and manga server. |  |
| Media | LANraragi | VM102 | ready | Archive and manga/doujin library manager. |  |
| Media | LibreTV | VM102 | review | Video aggregation app; source availability may be unstable. |  |
| Media | MediaCMS | VM102 | review | Self-hosted video CMS, like a private YouTube for personal, family, learning, or dataset videos. | Production deployment may need Postgres, Redis, workers, and transcoding tuning. |
| Media | Streamyfin | VM102 | external | Enhanced Jellyfin client ecosystem. Usually client-side/mobile; template is a placeholder/link entry. |  |
| Media | Suwayomi | VM102 | ready | Manga source server. |  |
| Media | Tdarr | VM102 | review | Distributed video transcoding, library optimization, and codec normalization platform. | Needs careful library path mapping and optional GPU transcoding setup. |
| Media | TubeArchivist | VM102 | review | Self-hosted YouTube archive with metadata, channel sync, subtitles, and indexing. | Needs companion services such as Redis/Elasticsearch in production; use for content you have rights to archive. |
| Media | Unmanic | VM102 | starter | Simple automatic video library optimizer/transcoder. | Easier than Tdarr, but still needs careful media path and plugin setup. |
| Monitoring | Beszel | VM101 | starter | Lightweight server monitoring hub. |  |
| Monitoring | Diun | VM101 | ready | Docker image update notifier. |  |
| Monitoring | Dozzle | VM101 | ready | Real-time Docker logs viewer. |  |
| Monitoring | GoSpeed | VM101/VM102 | starter | Network speed test / file transfer helper. |  |
| Monitoring | Grafana | VM101 | ready | Observability dashboard platform. |  |
| Monitoring | HertzBeat | VM101 | starter | Universal monitoring platform for HTTP, DB, network, and services. |  |
| Monitoring | Netdata | VM101 | ready | Real-time infrastructure monitoring. |  |
| Monitoring | Uptime Kuma | VM101 | ready | Self-hosted uptime monitoring. |  |
| Monitoring | Watchtower | VM101 | starter | Docker auto-update tool. Recommended notification-only mode first. |  |
| NAS Infrastructure | Virtual DSM | VM104 | review | Virtual Synology DSM. Requires KVM/privileged setup; experimental. |  |
| Networking & Reverse Proxy | Caddy Manager | VM101 | starter | UI for managing Caddy configuration. |  |
| Networking & Reverse Proxy | Caddy Server | VM101 | ready | Caddy web server and reverse proxy. |  |
| Networking & Reverse Proxy | Cloudflare Tunnel | VM101 | ready | Cloudflare Tunnel connector. |  |
| Networking & Reverse Proxy | LanCache | VM102 | review | LAN cache for game/platform downloads. Requires DNS planning. |  |
| Networking & Reverse Proxy | Tailscale | All VMs | starter | Mesh VPN. Usually installed on host OS; Docker template included for subnet-router/container cases. |  |
| Office & Collaboration | Collabora CODE | VM104 | ready | LibreOffice Online / Collabora document server. |  |
| Office & Collaboration | OnlyOffice Docs | VM104 | ready | Online office document server. |  |
| Office & Collaboration | Univer | VM104 | review | Open-source office/collaboration suite. Verify upstream image for your region. |  |
| Platform | Arcane | VM101/VM104 | ready | Modern Docker management control plane. |  |
| Platform | Arcane Agent | All Docker VMs | review | Arcane remote Docker host agent. Verify official pairing flow. |  |
| Search & RAG | Langfuse | VM103 | review | LLM observability. Production stack requires supporting services. |  |
| Search & RAG | LiteLLM | VM103 | starter | LLM gateway/proxy. |  |
| Search & RAG | Qdrant | VM103 | ready | Vector database for AI/RAG. |  |
| Search & RAG | SearXNG | VM103 | ready | Privacy-respecting metasearch engine. |  |
| Security & Identity | 2FAuth | VM101 | ready | Self-hosted TOTP/2FA account manager. |  |
| Security & Identity | Authentik | VM101 | ready | Identity provider and SSO platform. |  |
| Security & Identity | Safeline WAF | VM101 | review | Web application firewall stack. Review official multi-service compose before production. |  |
| Security & Identity | Vaultwarden | VM101 | ready | Lightweight Bitwarden-compatible password manager. |  |
| Storage & Files | AList | VM101/VM102 | ready | File list and WebDAV gateway for cloud drives and local storage. |  |
| Storage & Files | BaiduNetDisk | VM102 | review | Baidu Netdisk desktop client in browser container. |  |
| Storage & Files | File Browser | VM101 | ready | Web file manager. |  |
| Storage & Files | NextExplorer | VM101 | starter | Native file browser for mounted NAS paths. |  |
| Storage & Files | OpenCloud | VM101/VM102 | review | Cloud file collaboration platform. Verify production compose before use. |  |
| Storage & Files | SFTPGo | VM101 | ready | SFTP, WebDAV and file transfer server. |  |
| Storage & Sync | Resilio Sync | VM101 | ready | P2P file synchronization based on BitTorrent technology. |  |
| Storage & Sync | Syncthing | VM101/VM102 | ready | Open-source peer-to-peer file synchronization. |  |