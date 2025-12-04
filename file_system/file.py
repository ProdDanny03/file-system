import shutil
import os
import subprocess
from pathlib import Path
from file_system._helper import resolve_path

def to_list(file_path: str|Path) -> list[str]:
    _file_path = resolve_path(file_path)
    with open(_file_path, 'r') as f:
        return f.readlines()

def to_str(file_path: str|Path) -> str:
    _file_path = resolve_path(file_path)
    with open(_file_path, 'r') as f:
        return f.read()


def from_list(file_path: str|Path, lines: list[str], overwrite: bool=False, endl: str='\n') -> None:
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
    _file_path = resolve_path(file_path)
    if overwrite:
        with open(_file_path, 'w') as f:
            f.write(line)
    else:
        with open(_file_path, 'a') as f:
            f.write(line)

def create(file_path: str|Path) -> None:
    _file_path = resolve_path(file_path)
    with open(_file_path, 'w') as f:
        f.write('')

def move(src_path: str|Path, dst_path: str|Path, copy: bool=False) -> None:
    _src_path = resolve_path(src_path)
    _dst_path = resolve_path(dst_path)
    if copy:
        shutil.copy(_src_path, _dst_path)
    else:
        shutil.move(_src_path, _dst_path)

def delete(file_path: str|Path) -> None:
    _file_path = resolve_path(file_path)
    os.remove(_file_path)

def rename(file_path: str|Path, name: str) -> None:
    _file_path = resolve_path(file_path)
    _name = _file_path.name.replace(_file_path.name, name)
    os.rename(_file_path, _name)

def run(file_path: str|Path, wait: bool=True) -> None:
    _file_path = resolve_path(file_path)
    if wait:
        subprocess.run([_file_path])
    else:
        subprocess.Popen([_file_path])
