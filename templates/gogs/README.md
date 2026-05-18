# Gogs

Category: **Developer Tools / DevOps**  
Recommended target: **VM104**  
Image: `gogs/gogs:latest`  
Maturity: **ready**

## Summary

Very lightweight self-hosted Git service.

## One-click guidance

Good one-click candidate. Lighter than Gitea, smaller ecosystem.

## Deploy checklist

1. Review `.env.example`.
2. Edit ports, secrets, domain values, and storage paths.
3. Confirm target VM role matches this app.
4. Deploy through Arcane Templates or Projects.
5. Add Uptime Kuma monitor if the service is important.

## Ownership rule

- Runtipi-managed apps: observe in Arcane, but avoid editing/updating from Arcane unless intentionally migrating ownership.
- Arcane-managed apps: deploy/update through Arcane.
