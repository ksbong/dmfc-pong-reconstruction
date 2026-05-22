from pathlib import Path

DATA_DIR = Path("data")

print("Data directory exists:", DATA_DIR.exists())

if not DATA_DIR.exists():
    raise FileNotFoundError("data/ directory does not exist.")

print("\nFiles under data/:")
for path in DATA_DIR.rglob("*"):
    if path.is_file():
        print(path)