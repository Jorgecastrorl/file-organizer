import json
from pathlib import Path


def log_file_movement(
    source_path: Path,
    destination_path: Path,
    log_path: Path,
    batch_id: str,
) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)

    log_entry = {
        "batch_id": batch_id,
        "source": str(source_path),
        "destination": str(destination_path),
    }

    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
