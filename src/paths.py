from pathlib import Path


def get_project_root() -> Path:
    cwd = Path.cwd()

    if cwd.name == "notebooks":
        return cwd.parent

    return cwd


def get_data_dir() -> Path:
    project_root = get_project_root()

    candidates = [
        project_root / "data" / "external" / "MentalPong" / "data",
        project_root / "data" / "external" / "data",
        project_root / "data" / "data",
    ]

    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError("Could not find MentalPong data directory.")


def get_source_data_path() -> Path:
    return get_data_dir() / "Source_Data.xlsx"