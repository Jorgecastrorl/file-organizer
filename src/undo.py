import json
import shutil
from pathlib import Path

from src.config import DOWNLOADS_FOLDER, LOG_FOLDER, SIMULATE
from src.file_manager import remove_empty_folders


def undo_last_batch(log_path: Path) -> None:
    if not log_path.exists():
        print("No log file found.")
        return

    with log_path.open("r", encoding="utf-8") as log_file:
        lines = [line.strip() for line in log_file if line.strip()]

    if not lines:
        print("No actions found to undo.")
        return

    log_entries = [json.loads(line) for line in lines]
    last_batch_id = log_entries[-1]["batch_id"]

    last_batch_entries = [
        entry for entry in log_entries if entry["batch_id"] == last_batch_id
    ]
    remaining_entries = [
        entry for entry in log_entries if entry["batch_id"] != last_batch_id
    ]

    for entry in reversed(last_batch_entries):
        source_path = Path(entry["source"])
        destination_path = Path(entry["destination"])

        if not destination_path.exists():
            print(f"File not found for undo: {destination_path}")
            continue

        source_path.parent.mkdir(parents=True, exist_ok=True)

        if SIMULATE:
            print(
                f"Simulation: '{destination_path.name}' would be moved back to "
                f"'{source_path}'"
            )
        else:
            shutil.move(str(destination_path), str(source_path))
            print(
                f"Undone: '{destination_path.name}' was moved back to "
                f"'{source_path.parent}'"
            )

    with log_path.open("w", encoding="utf-8") as log_file:
        for entry in remaining_entries:
            log_file.write(json.dumps(entry, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    undo_last_batch(LOG_FOLDER / "file_movements.log")
    remove_empty_folders(DOWNLOADS_FOLDER)
