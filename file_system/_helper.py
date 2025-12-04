from pathlib import Path

def resolve_path(path: str|Path) -> Path:
    if path is str:
        return Path(path).resolve()
    elif path is Path:
        return path
    else:
        raise TypeError('path must be str or Path, not ' + str(type(path)))