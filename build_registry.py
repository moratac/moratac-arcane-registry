#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from datetime import datetime, timezone

parser = argparse.ArgumentParser()
parser.add_argument("--base-url", default="https://raw.githubusercontent.com/moratac/moratac-arcane-registry/main/templates")
args = parser.parse_args()

root = Path(__file__).parent
registry = json.loads((root / "registry.json").read_text())
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
registry["updated_at"] = now
for item in registry["templates"]:
    tid = item["id"]
    item["compose_url"] = f"{args.base_url.rstrip('/')}/{tid}/compose.yaml"
    item["env_url"] = f"{args.base_url.rstrip('/')}/{tid}/.env.example"
    item["documentation_url"] = f"{args.base_url.rstrip('/')}/{tid}/README.md"
    item["updated_at"] = now
(root / "registry.json").write_text(json.dumps(registry, indent=2, ensure_ascii=False))
print(f"Updated {len(registry['templates'])} templates")
