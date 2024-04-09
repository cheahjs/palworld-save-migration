from typing import Any, Dict

from palworld_save_tools.gvas import GvasFile
from palworld_save_tools.palsav import compress_gvas_to_sav, decompress_sav_to_gvas
from palworld_save_tools.paltypes import PALWORLD_CUSTOM_PROPERTIES, PALWORLD_TYPE_HINTS


def read_sav_to_dict(
    filename,
    allow_nan=True,
    custom_properties_keys=["all"],
) -> Dict[str, Any]:
    print(f"Decompressing sav file")
    with open(filename, "rb") as f:
        data = f.read()
        raw_gvas, _ = decompress_sav_to_gvas(data)
    print(f"Loading GVAS file")
    custom_properties = {}
    if len(custom_properties_keys) > 0 and custom_properties_keys[0] == "all":
        custom_properties = PALWORLD_CUSTOM_PROPERTIES
    else:
        for prop in PALWORLD_CUSTOM_PROPERTIES:
            if prop in custom_properties_keys:
                custom_properties[prop] = PALWORLD_CUSTOM_PROPERTIES[prop]
    gvas_file = GvasFile.read(
        raw_gvas, PALWORLD_TYPE_HINTS, custom_properties, allow_nan=allow_nan
    )
    return gvas_file.dump()


def write_dict_to_sav(pal_dict: Dict[str, Any], output_path):
    gvas_file = GvasFile.load(pal_dict)
    print(f"Compressing SAV file")
    if (
        "Pal.PalWorldSaveGame" in gvas_file.header.save_game_class_name
        or "Pal.PalLocalWorldSaveGame" in gvas_file.header.save_game_class_name
    ):
        save_type = 0x32
    else:
        save_type = 0x31
    sav_file = compress_gvas_to_sav(
        gvas_file.write(PALWORLD_CUSTOM_PROPERTIES), save_type
    )
    print(f"Writing SAV file to {output_path}")
    with open(output_path, "wb") as f:
        f.write(sav_file)
