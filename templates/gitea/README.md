# Gitea Server

Category: **Developer Tools / DevOps**  
Recommended target: **VM104/VM101**  
Image: `gitea/gitea:latest`  
Maturity: **ready**

## Summary

Lightweight self-hosted Git server. Best first choice for homelab Git.

## One-click guidance

Good one-click candidate. Set ROOT_URL and SSH port before production.

## Deploy checklist

1. Review `.env.example`.
2. Edit ports, secrets, domain values, and storage paths.
3. Confirm target VM role matches this app.
4. Deploy through Arcane Templates or Projects.
5. Add Uptime Kuma monitor if the service is important.

## Ownership rule

- Runtipi-managed apps: observe in Arcane, but avoid editing/updating from Arcane unless intentionally migrating ownership.
- Arcane-managed apps: deploy/update through Arcane.
