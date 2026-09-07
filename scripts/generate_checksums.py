from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "models.json"
MODELS_DIR = ROOT / "models"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        while chunk := file.read(1024 * 1024):
            digest.update(chunk)

    return digest.hexdigest()


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text())

    for model in registry["models"].values():
        for backend in ("pytorch", "litert"):
            artifact = model.get(backend)

            if artifact is None:
                continue

            path = MODELS_DIR / artifact["filename"]

            if not path.exists():
                print(f"Skipping missing file: {path}")
                continue

            checksum = sha256_file(path)

            artifact["sha256"] = checksum

            print(
                f"{artifact['filename']}: "
                f"{checksum}"
            )

    REGISTRY_PATH.write_text(
        json.dumps(
            registry,
            indent=2,
        )
        + "\n"
    )


if __name__ == "__main__":
    main()