import pandas as pd
from pathlib import Path


def size_category(size_mb: float) -> str:
    if size_mb < 10:
        return "safe"
    elif size_mb < 100:
        return "moderate"
    elif size_mb < 500:
        return "large"
    else:
        return "very_large"


def build_file_inventory(data_dir: Path, project_root: Path | None = None) -> pd.DataFrame:
    file_rows = []

    if project_root is None:
        project_root = data_dir.parent

    for path in data_dir.rglob("*"):
        if path.is_file():
            size_mb = path.stat().st_size / (1024 ** 2)

            file_rows.append({
                "name": path.name,
                "relative_path": str(path.relative_to(project_root)),
                "suffix": path.suffix,
                "size_mb": size_mb,
            })

    files_df = pd.DataFrame(file_rows)

    if len(files_df) == 0:
        return files_df

    files_df = files_df.sort_values("size_mb", ascending=False)
    files_df["load_policy"] = files_df["size_mb"].apply(size_category)

    return files_df