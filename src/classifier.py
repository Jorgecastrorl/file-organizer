from src.config import FILE_CATEGORIES


def classify_file(file_info: dict) -> dict:
    file_name = file_info["name"]

    for category, extensions in FILE_CATEGORIES.items():
        if file_name.lower().endswith(tuple(extensions)):
            file_info["destination"] = category
            return file_info

    file_info["destination"] = "99_Review"
    return file_info
