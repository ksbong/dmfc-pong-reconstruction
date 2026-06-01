def summarize_dict(d, max_depth=2, indent=0):
    prefix = " " * indent

    for key, value in d.items():
        shape = getattr(value, "shape", None)

        if isinstance(value, dict) and max_depth > 0:
            print(f"{prefix}{key}: dict ({len(value)} keys)")
            summarize_dict(value, max_depth=max_depth - 1, indent=indent + 2)
        else:
            print(f"{prefix}{key}: {type(value).__name__}, shape={shape}")