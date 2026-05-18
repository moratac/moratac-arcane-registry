# SGLang

Category: **AI Inference**  
Recommended target: **VM103**  
Image: `lmsysorg/sglang:latest`  
Maturity: **review**

> ⚠️ Review before deploy. This template may need official production compose, secrets, GPU/KVM/privileged mode, or supporting services.

## Summary

High-performance LLM serving runtime. GPU recommended.

## Deploy checklist

1. Review `.env.example`.
2. Edit ports, secrets, domain values, and storage paths.
3. Confirm target VM role matches this app.
4. Deploy through Arcane Templates or Projects.

## Ownership rule

- Runtipi-managed apps: observe in Arcane, but avoid editing/updating from Arcane unless intentionally migrating ownership.
- Arcane-managed apps: deploy/update through Arcane.
- High-risk apps: AI agents, browsers, downloaders, redroid, Virtual DSM, LanCache, GPU inference.
