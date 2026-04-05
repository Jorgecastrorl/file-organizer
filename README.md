# File Organizer

A simple Python project to organize files automatically by category, with support for simulation mode and undoing the last batch of moved files.

## Overview

This project scans a target folder, classifies files based on their extensions, moves them into category folders, and records all movements in a log file.

Each execution generates a unique `batch_id`, which allows the program to undo the most recent batch of file movements safely.

## Features

- List files from an input folder
- Classify files by extension
- Move files into category folders automatically
- Simulation mode to preview changes without moving files
- Movement log stored in a `.log` file
- Undo the last batch of moved files
- Clear and modular project structure

## Project Structure

```text
file-organizer/
│
├─ src/
│  ├─ classifier.py
│  ├─ config.py
│  ├─ file_manager.py
│  ├─ log_file.py
│  ├─ main.py
│  └─ undo.py
│
├─ logs/
│  └─ file_movements.log
│
├─ .gitignore
├─ .python-version
├─ pyproject.toml
├─ uv.lock
└─ README.md
```

## How It Works

The program follows this flow:

1. Read all files from the input folder
2. Classify each file according to its extension
3. Move the file to the matching destination folder
4. Save each movement to a log file
5. Group all movements from the same execution using a unique `batch_id`
6. Allow the last execution to be undone later

## Current Categories

The categories are defined in `config.py`:

- `Documents`
- `Images`
- `Executables`
- `Projects`
- `Compressed`

Files that do not match any category are sent to:

- `99_Review`

## Configuration

The project settings are stored in `src/config.py`.

Example:

```python
from pathlib import Path

SIMULATE = False  # Set to True to simulate file movements without actually moving files

DOWNLOADS_FOLDER = Path.home() / "Downloads"
INPUT_FOLDER = DOWNLOADS_FOLDER
INPUT_FOLDER.mkdir(exist_ok=True)

LOG_FOLDER = Path(__file__).resolve().parent.parent / "logs"
LOG_FOLDER.mkdir(exist_ok=True)

FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Executables": [".exe", ".dll", ".sys"],
    "Projects": [".dwg", ".dxf", ".step", ".stl", ".dwl", ".dwl2"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
}
```

### Configuration Notes

- `SIMULATE = True` runs the program without actually moving files
- `DOWNLOADS_FOLDER` defines the base folder where categorized folders are created
- `INPUT_FOLDER` is the folder that will be scanned
- `LOG_FOLDER` stores the movement log file
- `FILE_CATEGORIES` maps file extensions to destination folders

## Requirements

- Python 3.13+
- `uv` recommended for running the project

Standard library modules used:

- `pathlib`
- `shutil`
- `json`
- `uuid`

No external dependencies are required for the core functionality.

## Running the Project

### Organize files

```bash
uv run .\src\main.py
```

### Undo the last moved batch

```bash
uv run .\src\undo.py
```

## Simulation Mode

To test the behavior without moving files, set this in `config.py`:

```python
SIMULATE = True
```

In simulation mode, the program only prints what it would do.

Example:

```text
Simulation: The file 'project.dwg' would be moved to 'C:\Users\Name\Downloads\Projects'
```

## Example Output

```text
File: report.pdf - Destination: Documents
File: image.jpg - Destination: Images
File: model.dwg - Destination: Projects
Processing finished.
Batch ID: 87df62f4-f99b-48bf-aa34-f833f756cabb
```

## Log System

All movements are recorded in:

```text
logs/file_movements.log
```

Each line stores a JSON object like this:

```json
{
  "batch_id": "87df62f4-f99b-48bf-aa34-f833f756cabb",
  "source": "C:\\Users\\Name\\Downloads\\report.pdf",
  "destination": "C:\\Users\\Name\\Downloads\\Documents\\report.pdf"
}
```

This makes it possible to undo the last execution reliably.

## Modules

### `main.py`

The entry point of the project.

Responsibilities:

- generate a `batch_id`
- list files from the input folder
- classify files
- move files
- print the final execution summary

### `classifier.py`

Responsible for classifying a file based on its extension.

### `file_manager.py`

Responsible for:

- listing files
- moving files to destination folders

### `log_file.py`

Responsible for writing file movement records to the log file.

### `undo.py`

Responsible for undoing the last batch of file movements based on the log.

### `config.py`

Stores:

- paths
- simulation mode
- file categories

## Why Use `batch_id`

Every execution gets a unique `batch_id` generated with `uuid4()`.

This is useful because:

- multiple files moved in the same run belong to the same batch
- undo can revert the entire last run, not just one file
- the log remains simple and reliable

## Possible Improvements

Future versions could include:

- duplicate filename handling
- recursive organization of subfolders
- configuration via `.json` or `.toml`
- unit tests
- command-line arguments
- graphical user interface
- customizable folder naming
- ignore list for specific files or extensions

## Author

Jorge Castro

## Purpose

This project was created to practice:

- Python fundamentals
- file handling
- project structure
- separation of responsibilities
- logging and undo workflows
