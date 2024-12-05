import json
import sys
from pathlib import Path

def sort_quotes(path_in=Path("./quotes.json"), path_out=Path("./quotes_sorted.json")):
    with open(path_in, "r") as file:
        tags = {}
        file = json.loads(file.read())
        for obj in file:
            if obj["tag"] not in tags.keys():
                tags[obj["tag"]] = []
            if ("date" in obj) :
                tags[obj["tag"]].append(
                    {
                        "lines": obj["lines"],
                        "date": obj["date"]
                    }
                )
            else:
                tags[obj["tag"]].append(
                    {
                        "lines": obj["lines"]
                    }
                )



    with open(path_out, "w") as file:
        file.write(json.dumps(tags))


if __name__ == "__main__":
    help_line = "Split the quote by tag. Usage: python script_sort_quote.py <file_path_in> <file_path_out>"
    if sys.argv[1] == "--help":
        print(help_line)

    if len(sys.argv) < 3:
        print(help_line)
        sys.exit(1)

    file_path_in = Path(sys.argv[1])
    file_path_out = Path(sys.argv[2])

    processed = sort_quotes(file_path_in, file_path_out)
    print(f"Quotes splitted for {str(file_path_in.name)}")