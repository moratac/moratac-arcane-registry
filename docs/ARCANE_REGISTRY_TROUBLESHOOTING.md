# Arcane Registry Troubleshooting

v0.6 makes registry.json schema-clean.

Removed from registry.json:
- category
- target_vm
- maturity
- updated_at

Those fields remain in manifest.json and templates/<id>/template.json.

Test URLs:

```text
https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/registry.json
https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/templates/it-tools/compose.yaml
https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/templates/it-tools/.env.example
```

After uploading v0.6:
1. Remove old Moratac registry in Arcane.
2. Add it again:
   https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/registry.json
3. Refresh templates.
4. Test IT-Tools first.
