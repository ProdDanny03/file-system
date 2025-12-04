# file‑system  

A tiny pure‑Python utility library that provides simple, high‑level helpers for common file‑ and folder‑operations.

---

## 📦 Installation  

```bash
pip install git+https://github.com/ProdDanny03/file-system.git
```

---

## 🚀 Quick start  

```python
# Import the public modules
from file_system import file, folder
```

Now you can call any helper directly, e.g.:

```python
lines = file.to_list("data/input.txt")
print(lines)
```

---

## 📂 `file` – file helpers  

| Function | Description | Example |
|----------|-------------|---------|
| `to_list(path)` | Return a list of lines (including newline characters) from *path*. | ```python\nlines = file.to_list("notes.txt")\nprint(lines)\n``` |
| `to_str(path)` | Return the whole file content as a single string. | ```python\ncontent = file.to_str("notes.txt")\nprint(content)\n``` |
| `from_list(path, lines, overwrite=False, endl='\n')` | Write a list of strings to *path*. `overwrite=True` truncates the file; otherwise the data is appended. | ```python\nfile.from_list("out.txt", [\"first\", \"second\"], overwrite=True)\n``` |
| `from_str(path, line, overwrite=False)` | Write a single string to *path*. | ```python\nfile.from_str("out.txt", \"hello world\", overwrite=False)\n``` |
| `create(path)` | Create an empty file (or truncate an existing one). | ```python\nfile.create("empty.txt")\n``` |
| `move(src, dst, copy=False)` | Move a file, or copy it when `copy=True`. | ```python\nfile.move(\"old.txt\", \"new.txt\")          # move\nfile.move(\"old.txt\", \"copy.txt\", copy=True)  # copy\n``` |
| `delete(path)` | Delete a file. | ```python\nfile.delete(\"tmp.txt\")\n``` |
| `rename(path, new_name)` | Rename a file while keeping its directory. | ```python\nfile.rename(\"data/report.txt\", \"final_report.txt\")\n``` |
| `run(path, wait=True)` | Execute a file as a subprocess. `wait=False` launches it asynchronously. | ```python\nfile.run(\"script.sh\")               # wait for completion\nfile.run(\"script.sh\", wait=False)   # fire‑and‑forget\n``` |

---

## 📁 `folder` – folder helpers  

| Function | Description | Example |
|----------|-------------|---------|
| `create(path)` | Create a new empty directory. Raises `FileExistsError` if it already exists. | ```python\nfolder.create(\"logs\")\n``` |
| `remove(path)` | Recursively delete a directory and all its contents. | ```python\nfolder.remove(\"old_data\")\n``` |
| `to_list(path)` | Return a list of absolute paths (as strings) for the immediate children of *path*. | ```python\nfiles = folder.to_list(\"src\")\nprint(files)\n``` |
| `to_str(path, sep="\\n")` | Return a single string containing one entry per line for the directory contents. | ```python\nprint(folder.to_str(\"src\"))\n``` |
| `move(src, dst, copy=False)` | Move a file or sub‑directory, or copy it when `copy=True`. | ```python\nfolder.move(\"tmp/file.txt\", \"archive/file.txt\")\nfolder.move(\"tmp\", \"backup\", copy=True)\n``` |
| `delete(path)` | Alias for `remove`; recursively delete a directory. | ```python\nfolder.delete(\"temp_folder\")\n``` |
| `rename(path, new_name)` | Rename a directory while preserving its parent path. | ```python\nfolder.rename(\"data/old\", \"new\")\n``` |
| `compress(path, output_zip)` | Create a **.zip** archive (LZMA‑compressed) of the directory tree. | ```python\nfolder.compress(\"project\", \"project.zip\")\n``` |
| `decompress(zip_path, output_folder)` | Extract a zip archive into *output_folder*. | ```python\nfolder.decompress(\"project.zip\", \"project_unpacked\")\n``` |

---

## 📄 License  

MIT – see the `LICENSE` file in the repository.