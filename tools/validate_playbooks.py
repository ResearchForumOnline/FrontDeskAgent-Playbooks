from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAYBOOKS = ROOT / "playbooks"
REQUIRED = {"id", "name", "version", "industry", "opening_message", "required_fields", "urgency_rules", "handoff_summary"}


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = REQUIRED - data.keys()
    if missing:
        errors.append(f"{path.name}: missing {', '.join(sorted(missing))}")
    if not isinstance(data.get("required_fields"), list) or not data.get("required_fields"):
        errors.append(f"{path.name}: required_fields must be a non-empty list")
    for index, field in enumerate(data.get("required_fields", []), start=1):
        for key in ("key", "label", "question"):
            if key not in field:
                errors.append(f"{path.name}: required_fields[{index}] missing {key}")
    if not isinstance(data.get("urgency_rules"), list):
        errors.append(f"{path.name}: urgency_rules must be a list")
    return errors


def main() -> int:
    paths = sorted(PLAYBOOKS.glob("*.json"))
    if not paths:
        print("No playbooks found.")
        return 1
    errors: list[str] = []
    for path in paths:
        errors.extend(validate_file(path))
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated {len(paths)} playbooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
