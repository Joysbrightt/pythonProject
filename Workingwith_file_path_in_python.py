import csv
from os import path
from pathlib import Path
new_dir = Path.home() / "new_directory"
# new_dir.mkdir(exist_ok=True)
#
# new_dir.is_dir()
#
# nested_dir = new_dir /"flder_a" / "folder_b"
# nested_dir.mkdir(parents=True)
# path.mkdir(parents=True, exis_ok=True)
file_path = new_dir/ "file1.txt"
file_path.touch()
file_path.exists()
print(file_path.exists())


for path in new_dir.iterdir():

    list(new_dir.iterdir())
    print(path)

    name, department, salary
    Lee, Operations, 75000.00
    Jane, Engineering, 85000.00
    Diego, Sales, 80000.00
    csv