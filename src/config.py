from pathlib import Path

SIMULATE = False  # Set to True to simulate file movements without actually moving files

WINDOWS_USER = "Jorge Castro"
DOWNLOADS_FOLDER = Path(f"/mnt/c/Users/{WINDOWS_USER}/Downloads")
INPUT_FOLDER = DOWNLOADS_FOLDER
# INPUT_FOLDER.mkdir(exist_ok=True)

LOG_FOLDER = Path(__file__).resolve().parent.parent / "logs"
LOG_FOLDER.mkdir(exist_ok=True)

FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Executables": [".exe", ".dll", ".sys"],
    "Projects": [".dwg", ".dxf", ".step", ".stl", ".dwl", ".dwl2"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

if __name__ == "__main__":
    print(DOWNLOADS_FOLDER)