# file_system/_helper.py
from pathlib import Path
from typing import Union

def resolve_path(path: Union[str, Path]) -> Path:
    """
    The `resolve_path` function accepts a string or Path object, converts it to a Path object, expands
    `~`, resolves any relative components, and returns the normalized path.
    @param path (Union[str, Path]) - The `path` parameter can be either a string or a `Path` object. The
    function `resolve_path` will convert the input into a `Path` object, expand any `~` characters, and
    resolve any relative components like `..`. Finally, it will return the normalized and resolved `
    @returns The function `resolve_path` returns a `Path` object after converting the input path to a
    `Path`, expanding `~`, and resolving any relative components like `..`. The returned `Path` object
    is the normalized and resolved version of the input path.
    Danny - 12/04/2025
    """
    # Accept both ``str`` and ``Path`` – the original code used a wrong
    # ``type(path) is str`` check which rejected strings.
    if not isinstance(path, (str, Path)):
        raise TypeError(f"path must be str or Path, not {type(path)}")

    # Turn the input into a Path, expand ``~`` and resolve any relative
    # components (``..`` etc.).  ``resolve()`` also normalises the path.
    return Path(path).expanduser().resolve()