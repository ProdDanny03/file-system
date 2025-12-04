import shutil
import os
import subprocess
from pathlib import Path
from file_system._helper import resolve_path

def to_list(file_path: str|Path) -> list[str]:
    """
    The function `to_list` reads the contents of a file specified by the file path and returns them as a
    list of strings.
    @param file_path (str|Path) - The `file_path` parameter is a string or a `Path` object that
    represents the path to a file that you want to read.
    @returns A list of strings is being returned. Each string represents a line from the file located at
    the specified file path.
    Danny - 12/04/2025
    """
    _file_path = resolve_path(file_path)
    with open(_file_path, 'r') as f:
        return f.readlines()

def to_str(file_path: str|Path) -> str:
    """
    The function `to_str` reads and returns the contents of a file specified by the input file path.
    @param file_path (str|Path) - The `file_path` parameter in the `to_str` function is expected to be a
    string representing the path to a file. It can also be a `Path` object from the `pathlib` module.
    The function will resolve the path and then read the contents of the file located at that
    @returns The function `to_str` is returning the content of the file located at the given `file_path`
    as a string.
    Danny - 12/04/2025
    """
    _file_path = resolve_path(file_path)
    with open(_file_path, 'r') as f:
        return f.read()


def from_list(file_path: str|Path, lines: list[str], overwrite: bool=False, endl: str='\n') -> None:
    """
    The function `from_list` writes lines from a list to a file specified by the file path, either
    overwriting the existing content or appending to it based on the `overwrite` parameter.
    @param file_path (str|Path) - The `file_path` parameter in the `from_list` function is the path to
    the file where the lines will be written. It can be either a string representing the file path or a
    `Path` object.
    @param lines (list[str]) - The `lines` parameter in the `from_list` function is a list of strings
    that contains the content that you want to write to a file. Each element in the list represents a
    line of text that will be written to the file.
    @param overwrite (bool) - The `overwrite` parameter in the `from_list` function is a boolean flag
    that determines whether the content of the file at the specified `file_path` should be overwritten
    with the new `lines` or if the new `lines` should be appended to the existing content of the file.
    If `
    @param endl (str) - The `endl` parameter in the `from_list` function is used to specify the line
    ending character that will be appended to each line before writing it to the file. By default, it is
    set to `'\n'`, which represents the newline character. This character is used to indicate the end
    Danny - 12/04/2025
    """
    _file_path = resolve_path(file_path)
    _lines = []
    if overwrite:
        with open(_file_path, 'w') as f:
            for line in lines:
                _lines.append(f'{line}{endl}')
            f.writelines(_lines) 
    else:
        with open(_file_path, 'a') as f:
            for line in lines:
                _lines.append(f'{line}{endl}')
            f.writelines(_lines)

def from_str(file_path: str|Path, line: str, overwrite: bool=False) -> None:
    """
    This Python function writes a specified line to a file, either overwriting the existing content or
    appending to it based on the `overwrite` parameter.
    @param file_path (str|Path) - The `file_path` parameter is the path to the file where the `line`
    will be written. It can be either a string representing the file path or a `Path` object.
    @param line (str) - The `line` parameter in the `from_str` function represents the string that you
    want to write to the file specified by the `file_path` parameter. This string will be written either
    to the beginning of the file (if `overwrite` is set to `True`) or appended to the end
    @param overwrite (bool) - The `overwrite` parameter in the `from_str` function is a boolean
    parameter with a default value of `False`. When `overwrite` is set to `True`, the function will
    write the specified `line` to the file at the given `file_path`, overwriting any existing content in
    the
    Danny - 12/04/2025
    """
    _file_path = resolve_path(file_path)
    if overwrite:
        with open(_file_path, 'w') as f:
            f.write(line)
    else:
        with open(_file_path, 'a') as f:
            f.write(line)

def create(file_path: str|Path) -> None:
    """
    The function creates a new file at the specified file path or Path object.
    @param file_path (str|Path) - The `file_path` parameter in the `create` function is a string or a
    `Path` object that represents the path to the file that will be created.
    Danny - 12/04/2025
    """
    _file_path = resolve_path(file_path)
    with open(_file_path, 'w') as f:
        f.write('')

def move(src_path: str|Path, dst_path: str|Path, copy: bool=False) -> None:
    """
    The function `move` moves or copies a file from the source path to the destination path based on the
    specified parameters.
    @param src_path (str|Path) - The `src_path` parameter in the `move` function represents the source
    path of the file or directory that you want to move or copy. It can be either a string or a `Path`
    object specifying the location of the source file or directory.
    @param dst_path (str|Path) - The `dst_path` parameter in the `move` function represents the
    destination path where the file or directory will be moved or copied to. It can be either a string
    or a `Path` object specifying the location where the source file or directory will be moved or
    copied to.
    @param copy (bool) - The `copy` parameter in the `move` function is a boolean parameter that
    determines whether the file should be copied to the destination path (`dst_path`) or moved. If
    `copy` is set to `True`, the function will copy the file from the source path (`src_path`) to the
    Danny - 12/04/2025
    """
    _src_path = resolve_path(src_path)
    _dst_path = resolve_path(dst_path)
    if copy:
        shutil.copy(_src_path, _dst_path)
    else:
        shutil.move(_src_path, _dst_path)

def delete(file_path: str|Path) -> None:
    """
    The function `delete` deletes a file located at the specified file path.
    @param file_path (str|Path) - The `file_path` parameter in the `delete` function is a string or a
    `Path` object that represents the path to the file that you want to delete.
    Danny - 12/04/2025
    """
    _file_path = resolve_path(file_path)
    os.remove(_file_path)

def rename(file_path: str|Path, name: str) -> None:
    """
    The function `rename` takes a file path and a new name, resolves the path, and renames the file with
    the new name.
    @param file_path (str|Path) - The `file_path` parameter is a string or a `Path` object representing
    the path to the file that you want to rename.
    @param name (str) - The `name` parameter in the `rename` function is a string that represents the
    new name that you want to assign to the file located at the `file_path`.
    Danny - 12/04/2025
    """
    _file_path = resolve_path(file_path)
    _name = _file_path.name.replace(_file_path.name, name)
    os.rename(_file_path, _name)

def run(file_path: str|Path, wait: bool=True) -> None:
    """
    The function `run` executes a file at the specified path either synchronously or asynchronously
    based on the `wait` parameter.
    @param file_path (str|Path) - The `file_path` parameter is a string or a `Path` object that
    represents the path to the file that you want to run using the `run` function.
    @param wait (bool) - The `wait` parameter in the `run` function is a boolean parameter with a
    default value of `True`. If `wait` is set to `True`, the function will wait for the subprocess to
    complete before continuing. If `wait` is set to `False`, the function will start the
    Danny - 12/04/2025
    """
    _file_path = resolve_path(file_path)
    if wait:
        subprocess.run([_file_path])
    else:
        subprocess.Popen([_file_path])
