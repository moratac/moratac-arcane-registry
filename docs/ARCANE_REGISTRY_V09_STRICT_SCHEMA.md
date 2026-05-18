# Arcane Registry v0.9 Strict Schema

This version follows the Arcane registry docs strictly.

## Top-level fields

- $schema
- name
- description
- version
- author
- url
- templates

## Template fields

- id
- name
- description
- version
- author
- compose_url
- env_url
- documentation_url
- tags

No content_hash, category, target_vm, maturity, or updated_at in registry.json.

## Required template files

- docker-compose.yml
- .env.example
- README.md

## Test URLs

https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/registry.json
https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/templates/it-tools/docker-compose.yml
https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/templates/it-tools/.env.example
https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/templates/it-tools/README.md
