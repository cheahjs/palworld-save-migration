from typing import Any, Sequence

from palworld_save_tools.archive import *
from palworld_save_tools.rawdata import (
    build_process,
    connector,
    map_concrete_model,
    map_model,
)


def decode(
    reader: FArchiveReader, type_name: str, size: int, path: str
) -> dict[str, Any]:
    if type_name != "ArrayProperty":
        raise Exception(f"Expected ArrayProperty, got {type_name}")
    value = reader.property(type_name, size, path, nested_caller_path=path)
    for map_object in value["value"]["values"]:
        # Decode Model
        map_object["Model"]["value"]["RawData"]["value"] = map_model.decode_bytes(
            reader, map_object["Model"]["value"]["RawData"]["value"]["values"]
        )
        # Decode Model.Connector
        map_object["Model"]["value"]["Connector"]["value"]["RawData"]["value"] = (
            connector.decode_bytes(
                reader,
                map_object["Model"]["value"]["Connector"]["value"]["RawData"]["value"][
                    "values"
                ],
            )
        )
        # Decode Model.BuildProcess
        map_object["Model"]["value"]["BuildProcess"]["value"]["RawData"]["value"] = (
            build_process.decode_bytes(
                reader,
                map_object["Model"]["value"]["BuildProcess"]["value"]["RawData"][
                    "value"
                ]["values"],
            )
        )
        # Decode ConcreteModel
        map_object_id = map_object["MapObjectId"]["value"]
        map_object["ConcreteModel"]["value"]["RawData"]["value"] = (
            map_concrete_model.decode_bytes(
                reader,
                map_object["ConcreteModel"]["value"]["RawData"]["value"]["values"],
                map_object_id,
            )
        )
    return value


def encode(
    writer: FArchiveWriter, property_type: str, properties: dict[str, Any]
) -> int:
    if property_type != "ArrayProperty":
        raise Exception(f"Expected ArrayProperty, got {property_type}")
    del properties["custom_type"]
    encoded_bytes = encode_bytes(properties["value"])
    properties["value"] = {"values": [b for b in encoded_bytes]}
    return writer.property_inner(property_type, properties)
