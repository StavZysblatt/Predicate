from typing import Any


def resolve_feature_path(root: object, path: str) -> Any:
    if not path:
        return root

    if not path.startswith("."):
        raise ValueError("Feature path must start with a '.'")

    parts = path[1:].split(".")

    current = root

    for part in parts:
        if not part.isidentifier():
            raise ValueError(f"Invalid attribute name: '{part}'")

        if isinstance(current, dict):
            current = current[part]

        else:
            current = getattr(current, part)

    return current

