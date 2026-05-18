# Arcane Usage Guide

## Ownership rule

- Runtipi apps: Runtipi manages install/update/uninstall.
- Arcane apps: Arcane manages deploy/update/delete.
- Arcane can observe all local Docker containers, including Runtipi containers, but avoid editing Runtipi-owned stacks.

## Recommended VM placement

| VM | Role |
|---|---|
| VM101 | Infra control plane |
| VM102 | Media, downloads, retro gaming |
| VM103 | AI plane |
| VM104 | Business, office, DevOps, experiments |

## First templates to test

1. IT-Tools
2. Dozzle
3. Gitea
4. Pinchflat
5. File Browser

Avoid first tests with Dify, Immich, GitLab CE, redroid, Virtual DSM, or GPU inference.
