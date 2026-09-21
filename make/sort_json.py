#!/usr/bin/env python3

__all__: list[str] = [
    "main",
    "run",
    "sort_data",
    "sort_file",
]

import argparse
import json
import logging
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
    try:
        run(*space.files)
    except Exception as exc:
        logging.exception(exc)


def run(*files: str) -> None:
    for path in files:
        sort_file(path)


def sort_data(data: Any, /) -> dict[str, Any] | list[Any]:
    if isinstance(data, dict):
        return dict[str, Any](sorted(data.items()))
    if isinstance(data, list):
        data.sort()
        return data
    raise TypeError(f"JSON type {type(data)} is not supported for sorting.")


def sort_file(path: str, /) -> None:
    data: Any
    with open(path, "r", encoding="utf-8") as stream:
        data = json.load(stream)
    data = sort_data(data)
    with open(path, "w", encoding="utf-8") as stream:
        json.dump(
            data,
            stream,
            indent=4,
        )
        stream.write("\n")


if __name__ == "__main__":
    main()
