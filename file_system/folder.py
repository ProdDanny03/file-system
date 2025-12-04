import shutil
import zipfile
from pathlib import Path
from file_system._helper import resolve_path

def create(folder_path: str|Path) -> None:
    _folder_path = resolve_path(folder_path)
    if not _folder_path.exists():
        _folder_path.mkdir()
    else:
        raise FileExistsError(f"Folder {folder_path} already exists.")

def remove(folder_path: str|Path) -> None:
    _folder_path = resolve_path(folder_path)
    if _folder_path.exists():
        shutil.rmtree(_folder_path)
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def to_list(folder_path: str|Path) -> list[str]:
    _folder_path = resolve_path(folder_path)
    if _folder_path.exists():
        return [str(file) for file in _folder_path.iterdir()]
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def to_str(folder_path: str|Path, sep: str="\n") -> str:
    _folder_path = resolve_path(folder_path)
    contents = ""
    if _folder_path.exists():
        for path in _folder_path.iterdir():
            contents += str(path) + "\n"
        return contents
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def move(src_path: str|Path, dst_path: str|Path, copy: bool=False) -> None:
    _src_path = resolve_path(src_path)
    _dst_path = resolve_path(dst_path)
    if _src_path.exists():
        if copy:
            shutil.copy(_src_path, _dst_path)
        else:
            shutil.move(_src_path, _dst_path)
    else:
        raise FileNotFoundError(f"File {src_path} does not exist.")

def delete(folder_path: str|Path) -> None:
    _folder_path = resolve_path(folder_path)
    if _folder_path.exists():
        shutil.rmtree(_folder_path)
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def rename(folder_path: str|Path, name: str) -> None:
    _folder_path = resolve_path(folder_path)
    _name = _folder_path.name.replace(_folder_path.name, name)
    if _folder_path.exists():
        _folder_path.rename(_name)
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def compress(folder_path: str|Path, output_zip: str|Path) -> None:
    _folder_path = resolve_path(folder_path)
    if _folder_path.exists():
        with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_LZMA) as z:
            for file in _folder_path.rglob("*"):
                z.write(file, file.relative_to(_folder_path))
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def decompress(folder_path: str|Path, output_folder: str|Path) -> None:
    zip_path = resolve_path(folder_path)
    if zip_path.exists():
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(output_folder)
    else:
        raise FileNotFoundError(f"Zip file {folder_path} does not exist.")


