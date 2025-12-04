import shutil
import zipfile
from pathlib import Path
from file_system._helper import resolve_path

def create(folder_path: str|Path) -> None:
    """
    The function creates a folder at the specified path if it does not already exist.
    @param folder_path (str|Path) - The `folder_path` parameter in the `create` function is the path to
    the folder that you want to create. It can be either a string representing the path or a `Path`
    object from the `pathlib` module.
    Danny - 12/04/2025
    """
    _folder_path = resolve_path(folder_path)
    if not _folder_path.exists():
        _folder_path.mkdir()
    else:
        raise FileExistsError(f"Folder {folder_path} already exists.")

def remove(folder_path: str|Path) -> None:
    """
    The function `remove` takes a folder path as input and deletes the folder if it exists, raising a
    `FileNotFoundError` if the folder does not exist.
    @param folder_path (str|Path) - The `folder_path` parameter in the `remove` function is a string or
    a `Path` object representing the path to the folder that needs to be removed.
    Danny - 12/04/2025
    """
    _folder_path = resolve_path(folder_path)
    if _folder_path.exists():
        shutil.rmtree(_folder_path)
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def to_list(folder_path: str|Path) -> list[str]:
    """
    The function `to_list` takes a folder path as input, resolves it, and returns a list of file names
    in the folder or raises a `FileNotFoundError` if the folder does not exist.
    @param folder_path (str|Path) - The `folder_path` parameter in the `to_list` function is expected to
    be a string representing a folder path or a `Path` object from the `pathlib` module.
    @returns A list of file names within the specified folder path is being returned.
    Danny - 12/04/2025
    """
    _folder_path = resolve_path(folder_path)
    if _folder_path.exists():
        return [str(file) for file in _folder_path.iterdir()]
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def to_str(folder_path: str|Path, sep: str="\n") -> str:
    """
    The function `to_str` takes a folder path as input, resolves it, and returns a string containing the
    paths of all files and directories within that folder separated by a specified separator.
    @param folder_path (str|Path) - The `folder_path` parameter is the path to a folder whose contents
    you want to convert to a string. It can be provided as a string or a `Path` object.
    @param sep (str) - The `sep` parameter in the `to_str` function is a string that specifies the
    separator to be used when concatenating the paths of files or directories within the specified
    folder. By default, the separator is set to `"\n"`, which means that each path will be separated by
    a newline
    @returns The `to_str` function returns a string containing the paths of all files and directories
    within the specified `folder_path`, separated by a newline character (`\n`). If the folder does not
    exist, a `FileNotFoundError` is raised with a message indicating that the folder does not exist.
    Danny - 12/04/2025
    """
    _folder_path = resolve_path(folder_path)
    contents = ""
    if _folder_path.exists():
        for path in _folder_path.iterdir():
            contents += str(path) + "\n"
        return contents
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def move(src_path: str|Path, dst_path: str|Path, copy: bool=False) -> None:
    """
    The function `move` moves or copies a file from a source path to a destination path in Python.
    @param src_path (str|Path) - The `src_path` parameter represents the source file or directory path
    that you want to move or copy. It can be either a string or a `Path` object specifying the location
    of the source file or directory.
    @param dst_path (str|Path) - The `dst_path` parameter in the `move` function represents the
    destination path where the file or directory specified by `src_path` will be moved or copied to. It
    can be either a string representing the path or a `Path` object.
    @param copy (bool) - The `copy` parameter in the `move` function is a boolean parameter that
    determines whether the file should be copied to the destination path (`dst_path`) instead of moving
    it. If `copy` is set to `True`, the function will use `shutil.copy` to copy the file from
    Danny - 12/04/2025
    """
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
    """
    The `delete` function deletes a folder at the specified path if it exists, raising a
    `FileNotFoundError` if the folder does not exist.
    @param folder_path (str|Path) - The `folder_path` parameter in the `delete` function is a string or
    a `Path` object representing the path to the folder that needs to be deleted.
    Danny - 12/04/2025
    """
    _folder_path = resolve_path(folder_path)
    if _folder_path.exists():
        shutil.rmtree(_folder_path)
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def rename(folder_path: str|Path, name: str) -> None:
    """
    The function `rename` takes a folder path and a new name, renames the folder with the new name, and
    raises a `FileNotFoundError` if the folder does not exist.
    @param folder_path (str|Path) - The `folder_path` parameter is a string or a `Path` object
    representing the path to the folder that you want to rename.
    @param name (str) - The `name` parameter in the `rename` function represents the new name that you
    want to assign to the folder located at the `folder_path`. This function takes the existing folder
    at `folder_path` and renames it to the specified `name`.
    Danny - 12/04/2025
    """
    _folder_path = resolve_path(folder_path)
    _name = _folder_path.name.replace(_folder_path.name, name)
    if _folder_path.exists():
        _folder_path.rename(_name)
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def compress(folder_path: str|Path, output_zip: str|Path) -> None:
    """
    The function compresses a folder into a zip file using LZMA compression in Python.
    @param folder_path (str|Path) - The `folder_path` parameter in the `compress` function is the path
    to the folder that you want to compress into a ZIP file. It can be either a string representing the
    path to the folder or a `Path` object from the `pathlib` module.
    @param output_zip (str|Path) - The `output_zip` parameter in the `compress` function is the path to
    the ZIP file that will be created to store the compressed contents of the folder specified by the
    `folder_path` parameter. This parameter should be a string or a `Path` object representing the
    location where the ZIP file will
    Danny - 12/04/2025
    """
    _folder_path = resolve_path(folder_path)
    if _folder_path.exists():
        with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_LZMA) as z:
            for file in _folder_path.rglob("*"):
                z.write(file, file.relative_to(_folder_path))
    else:
        raise FileNotFoundError(f"Folder {folder_path} does not exist.")

def decompress(folder_path: str|Path, output_folder: str|Path) -> None:
    """
    The function decompresses a zip file located at the specified folder path and extracts its contents
    to the output folder.
    @param folder_path (str|Path) - The `folder_path` parameter is a string or Path object that
    represents the path to the compressed zip file that you want to decompress.
    @param output_folder (str|Path) - The `output_folder` parameter in the `decompress` function is the
    destination folder where the contents of the compressed zip file will be extracted to. It should be
    a string or a `Path` object representing the path to the output folder.
    Danny - 12/04/2025
    """
    zip_path = resolve_path(folder_path)
    if zip_path.exists():
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(output_folder)
    else:
        raise FileNotFoundError(f"Zip file {folder_path} does not exist.")


