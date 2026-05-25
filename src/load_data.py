import pickle
from pathlib import Path


def load_pickle(path: Path):
    with open(path, "rb") as f:
        return pickle.load(f)


def inspect_object(obj):
    print("type:", type(obj))

    if hasattr(obj, "shape"):
        print("shape:", obj.shape)

    if isinstance(obj, dict):
        keys = list(obj.keys())
        print("num keys:", len(keys))
        print("first keys:", keys[:20])

    elif isinstance(obj, list):
        print("length:", len(obj))
        if len(obj) > 0:
            print("first item type:", type(obj[0]))