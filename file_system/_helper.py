# file_system/_helper.py
from pathlib import Path
from typing import Union

def resolve_path(path: Union[str, Path]) -> Path:
    """
    Convert *path* to an absolute :class:`pathlib.Path` object.

    Parameters
    ----------
    path : str | pathlib.Path
        The path supplied by the user.

    Returns
    -------
    pathlib.Path
        An absolute, resolved path.

    Raises
    ------
    TypeError
        If *path* is not a ``str`` or ``Path``.
    """
    # Accept both ``str`` and ``Path`` – the original code used a wrong
    # ``type(path) is str`` check which rejected strings.
    if not isinstance(path, (str, Path)):
        raise TypeError(f"path must be str or Path, not {type(path)}")

    # Turn the input into a Path, expand ``~`` and resolve any relative
    # components (``..`` etc.).  ``resolve()`` also normalises the path.
    return Path(path).expanduser().resolve()