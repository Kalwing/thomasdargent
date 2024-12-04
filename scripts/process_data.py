import sys
import os
import shutil
from pathlib import Path
import json

def move_files(origin, destination):
    files = list(origin.iterdir())
    N = len(files)
    for i, file_path in enumerate(files):
        print(f"{ i } / { N }", end="\r")
        if file_path.name[:6] == 'script':
            continue
        if file_path.suffix == ".json":
            with open(file_path, "r") as file:
                file_json = json.dumps(json.loads(file.read()), separators=(',', ':'))
            if not destination.exists():
                os.makedirs(destination)
            with open(destination / file_path.name, "w") as output:
                output.write(file_json)
            print(f"- \033[1;34m{file_path} minified and copied\033[0m")
        else:
            shutil.copy(file_path, destination)
            print(f"- \033[1;34m{file_path} copied.\033[0m")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\033[0;31m\033[1mPlease give the path of origin and destination.\033[0m")
        sys.exit(2)
    origin = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    if not origin.is_dir() or (destination.exists() and not destination.is_dir()):
        print("\033[0;31m\033[1morigin and destination must be directories.\033[0m")
        print("Origin:", origin.is_dir())
        print("Destination:", destination.exists(), destination.is_dir())
        sys.exit(1)
    try:
        move_files(origin, destination)
    except FileNotFoundError:
        print("\033[0;31m\033[1mFile wasn't found.\033[0m")
        sys.exit(3)
    except:
        print("\033[0;31m\033[1mProcess Failed.\033[0m")
        sys.exit(4)
    print("Data successfully processed")
    sys.exit(0)

