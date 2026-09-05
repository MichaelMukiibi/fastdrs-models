from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "models.json"
MODELS_DIR = ROOT / "models"


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text())

    failed = False

    for name, model in registry["models"].items():
        print(f"\nChecking {name}")

        for backend in ("pytorch", "litert"):
            artifact = model.get(backend)

            if artifact is None:
                continue

            path = MODELS_DIR / artifact["filename"]

            if not path.exists():
                print(
                    f"  [FAIL] {backend}: "
                    f"{artifact['filename']} missing"
                )
                failed = True
            else:
                print(
                    f"  [OK] {backend}: "
                    f"{artifact['filename']}"
                )

    if failed:
        raise SystemExit(1)

    print("\nAll registered artifacts are present.")


if __name__ == "__main__":
    main()