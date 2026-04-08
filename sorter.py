import argparse
import re
from pathlib import Path


LINE_PATTERN = re.compile(r"^(?P<name>.+?)\s*:\s*OK:\s*(?P<ok>\d+),")


def extract_ok_count(line: str) -> int:
    match = LINE_PATTERN.search(line.strip())
    if not match:
        return -1
    return int(match.group("ok"))


def sort_lines(lines: list[str]) -> list[str]:
    filtered_lines = [
        line.rstrip("\n")
        for line in lines
        if line.strip() and extract_ok_count(line) > 0
    ]
    return sorted(
        filtered_lines,
        key=extract_ok_count,
        reverse=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sort lines by OK count in descending order."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="list.txt",
        help="Path to the source file. Default: list.txt",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Optional output file. If omitted, prints to stdout.",
    )
    args = parser.parse_args()

    input_path = Path(args.input_file)
    lines = input_path.read_text(encoding="utf-8").splitlines()
    sorted_lines = sort_lines(lines)
    result = "\n".join(sorted_lines)

    if args.output:
        Path(args.output).write_text(result + "\n", encoding="utf-8")
    else:
        print(result)


if __name__ == "__main__":
    main()
