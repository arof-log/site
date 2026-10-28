#!/usr/bin/env python3
"""Build a public Works index from one JSON file per Pages CMS entry."""
import json
from pathlib import Path
source = Path("content/works")
target = Path("_site/works.json")
works = []
ids = set()
for file in sorted(source.glob("*.json")):
    item = json.loads(file.read_text(encoding="utf-8"))
    assert isinstance(item, dict), f"Expected object: {file}"
    for key in ("id", "title", "category", "image", "description", "url", "published", "order"):
        assert key in item, f"{file}: missing {key}"
    assert item["id"] not in ids, f"Duplicate id: {item['id']}"
    ids.add(item["id"])
    if item["published"]:
        works.append(item)
works.sort(key=lambda w: (w["order"], w["id"]))
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(works, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Built {len(works)} published Works from {len(ids)} JSON entries")
