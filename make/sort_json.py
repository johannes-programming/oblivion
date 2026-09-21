#!/usr/bin/env python3

__all__:list[str] = [
    "main",
    "run",
    "sort_json_file",
]

import argparse
import json
from typing import Any


def main() -> None:
    parser: argparse.ArgumentParser
    space: argparse.Namespace
    parser = argparse.ArgumentParser(
        description="Sort top-level keys in JSON files in place.",
        fromfile_prefix_chars="@",
    )
    parser.add_argument(
        "files",
        help="JSON files to sort in place",
        nargs="*",
    )
    space = parser.parse_args()
    run(*space.files)


def run(*files:str) -> None:
    for path in files:
        sort_json_file(path)


def sort_json_file(path) -> None:
    data:Any
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise TypeError(f"{path}: top-level JSON value is not an object")

    data = dict(sorted(data.items()))

    with open(path, "w", encoding="utf-8") as stream:
        json.dump(
            data,
            stream,
            indent=4,
            ensure_ascii=False,
        )
        stream.write("\n")


if __name__ == "__main__":
    main()
