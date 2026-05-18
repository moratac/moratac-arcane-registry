# GitLab CE

Category: **Developer Tools / DevOps**  
Recommended target: **VM104**  
Image: `gitlab/gitlab-ce:latest`  
Maturity: **review**

> ⚠️ Review before deploy. This template may need official production compose, secrets, high resources, or supporting services.

## Summary

Full-featured self-hosted GitLab Community Edition.

## One-click guidance

Heavy. Recommend dedicated VM with at least 4C/8G RAM. Review before deployment.

## Deploy checklist

1. Review `.env.example`.
2. Edit ports, secrets, domain values, and storage paths.
3. Confirm target VM role matches this app.
4. Deploy through Arcane Templates or Projects.
5. Add Uptime Kuma monitor if the service is important.

## Ownership rule

- Runtipi-managed apps: observe in Arcane, but avoid editing/updating from Arcane unless intentionally migrating ownership.
- Arcane-managed apps: deploy/update through Arcane.
