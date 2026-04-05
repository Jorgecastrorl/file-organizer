import shutil
from pathlib import Path

from src.config import DOWNLOADS_FOLDER, SIMULATE
from src.log_file import log_file_movement


def list_files(folder_path: Path) -> list[dict]:
    file_list = []

    for file_path in folder_path.iterdir():
        if file_path.is_file():
            file_list.append(
                {
                    "name": file_path.name,
                    "path": file_path,
                    "destination": "",
                }
            )

    return file_list


def move_file(file_info: dict, log_path: Path, batch_id: str) -> None:
    destination_folder = DOWNLOADS_FOLDER / file_info["destination"]
    destination_folder.mkdir(parents=True, exist_ok=True)

    source_path = file_info["path"]
    destination_path = destination_folder / file_info["name"]

    if SIMULATE:
        print(
            f"Simulation: The file '{file_info['name']}' would be moved to "
            f"'{destination_folder}'"
        )
        return

    shutil.move(str(source_path), str(destination_path))

    log_file_movement(
        source_path=source_path,
        destination_path=destination_path,
        log_path=log_path,
        batch_id=batch_id,
    )

    print(
        f"The file '{file_info['name']}' was moved to the folder "
        f"'{file_info['destination']}'"
    )


def remove_empty_folders(root_folder: Path) -> None:
    for folder_path in sorted(root_folder.rglob("*"), reverse=True):
        if folder_path.is_dir() and not any(folder_path.iterdir()):
            folder_path.rmdir()
            print(f"Removed empty folder: {folder_path}")
