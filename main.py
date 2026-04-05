from uuid import uuid4

from src.classifier import classify_file
from src.config import DOWNLOADS_FOLDER, INPUT_FOLDER, LOG_FOLDER, SIMULATE
from src.file_manager import list_files, move_file, remove_empty_folders

LOG_FILE = LOG_FOLDER / "file_movements.log"

def main() -> None:

    batch_id = str(uuid4())
    file_list = list_files(INPUT_FOLDER)

    if not file_list:
        print("No files found. Ending the program.")
        return

    for file_info in file_list:
        file_info = classify_file(file_info)
        print(f"File: {file_info['name']} - Destination: {file_info['destination']}")
        move_file(file_info, LOG_FILE, batch_id)

    remove_empty_folders(DOWNLOADS_FOLDER)

    print("Processing finished.")
    print(f"Batch ID: {batch_id}")


if __name__ == "__main__":
    main()
