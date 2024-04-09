#!/usr/bin/env python3

import argparse
import json
import os

from palworld_save_tools.json_tools import CustomEncoder
from palworld_save_tools.paltypes import PALWORLD_CUSTOM_PROPERTIES
from palworld_save_tools.dictsav import read_sav_to_dict, write_dict_to_sav


def main():
    parser = argparse.ArgumentParser(
        prog="palworld-save-tools",
        description="Converts Palworld save files to and from JSON",
    )
    parser.add_argument("filename")
    parser.add_argument(
        "--to-json",
        action="store_true",
        help="Override heuristics and convert SAV file to JSON",
    )
    parser.add_argument(
        "--from-json",
        action="store_true",
        help="Override heuristics and convert JSON file to SAV",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file (default: <filename>.json or <filename>.sav)",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Force overwriting output file if it already exists without prompting",
    )
    parser.add_argument(
        "--convert-nan-to-null",
        action="store_true",
        help="Convert NaN/Inf/-Inf floats to null when converting from SAV to JSON. This will lose information in the event Inf/-Inf is in the sav file (default: false)",
    )
    parser.add_argument(
        "--custom-properties",
        default=",".join(PALWORLD_CUSTOM_PROPERTIES.keys()),
        type=lambda t: [s.strip() for s in t.split(",")],
        help="Comma-separated list of custom properties to decode, or 'all' for all known properties. This can be used to speed up processing by excluding properties that are not of interest. (default: all)",
    )

    parser.add_argument("--minify-json", action="store_true", help="Minify JSON output")
    args = parser.parse_args()

    if args.to_json and args.from_json:
        print("Cannot specify both --to-json and --from-json")
        exit(1)

    if not os.path.exists(args.filename):
        print(f"{args.filename} does not exist")
        exit(1)
    if not os.path.isfile(args.filename):
        print(f"{args.filename} is not a file")
        exit(1)

    if args.to_json or args.filename.endswith(".sav"):
        if not args.output:
            output_path = args.filename + ".json"
        else:
            output_path = args.output
        convert_sav_to_json(
            args.filename,
            output_path,
            force=args.force,
            minify=args.minify_json,
            allow_nan=(not args.convert_nan_to_null),
            custom_properties_keys=args.custom_properties,
        )

    if args.from_json or args.filename.endswith(".json"):
        if not args.output:
            output_path = args.filename.replace(".json", "")
        else:
            output_path = args.output
        convert_json_to_sav(args.filename, output_path, force=args.force)


def convert_sav_to_json(
    filename,
    output_path,
    force=False,
    minify=False,
    allow_nan=True,
    custom_properties_keys=["all"],
):
    print(f"Converting {filename} to JSON, saving to {output_path}")
    if os.path.exists(output_path):
        print(f"{output_path} already exists, this will overwrite the file")
        if not force:
            if not confirm_prompt("Are you sure you want to continue?"):
                exit(1)
    pal_dict = read_sav_to_dict(filename, allow_nan=allow_nan, custom_properties_keys=custom_properties_keys)
    print(f"Writing JSON to {output_path}")
    with open(output_path, "w", encoding="utf8") as f:
        indent = None if minify else "\t"
        json.dump(
            pal_dict,
            f,
            indent=indent,
            cls=CustomEncoder,
            allow_nan=allow_nan,
        )


def convert_json_to_sav(filename, output_path, force=False):
    print(f"Converting {filename} to SAV, saving to {output_path}")
    if os.path.exists(output_path):
        print(f"{output_path} already exists, this will overwrite the file")
        if not force:
            if not confirm_prompt("Are you sure you want to continue?"):
                exit(1)
    print(f"Loading JSON from {filename}")
    with open(filename, "r", encoding="utf8") as f:
        pal_dict = json.load(f)
    write_dict_to_sav(pal_dict, output_path)


def confirm_prompt(question: str) -> bool:
    reply = None
    while reply not in ("y", "n"):
        reply = input(f"{question} (y/n): ").casefold()
    return reply == "y"


if __name__ == "__main__":
    main()
