# -*- coding: utf-8 -*-
from dataclasses import dataclass, fields
from typing import Optional

from .CharacterSaveParameterMap import ICSPMap
from .GroupSaveDataMapType import IGSDMap
from .MapObjectSaveType import IMOSData
from .BaseCampSaveDataType import IBCSD

@dataclass
class properties_Version:
    id: Optional[None]
    value: int
    type: str

@dataclass
class properties_Timestamp:
    struct_type: str
    struct_id: str
    id: Optional[None]
    value: int
    type: str

@dataclass
class WorldSaveData_Value:
    CharacterSaveParameterMap: ICSPMap
    GroupSaveDataMap: IGSDMap
    MapObjectSaveData: IMOSData
    BaseCampSaveData: IBCSD
    FoliageGridSaveDataMap: Optional[None] = None
    MapObjectSpawnerInStageSaveData: Optional[None] = None
    WorkSaveData: Optional[None] = None
    ItemContainerSaveData: Optional[None] = None
    DynamicItemSaveData: Optional[None] = None
    CharacterContainerSaveData: Optional[None] = None
    GameTimeSaveData: Optional[None] = None
    EnemyCampSaveData: Optional[None] = None
    DungeonPointMarkerSaveData: Optional[None] = None
    DungeonSaveData: Optional[None] = None
    CharacterParameterStorageSaveData: Optional[None] = None
    BossSpawnerSaveData: Optional[None] = None

    def __post_init__(self):
        self.CharacterSaveParameterMap = ICSPMap(**self.CharacterSaveParameterMap)
        self.GroupSaveDataMap = IGSDMap(**self.GroupSaveDataMap)
        self.MapObjectSaveData = IMOSData(**self.MapObjectSaveData)
        self.BaseCampSaveData = IBCSD(**self.BaseCampSaveData)

@dataclass
class properties_WorldSaveData:
    struct_type: str
    struct_id: str
    id: Optional[None]
    value: WorldSaveData_Value
    type: str
    def __post_init__(self):
        self.value = WorldSaveData_Value(**self.value)

@dataclass
class Header:
    magic: int
    save_game_version: int
    package_file_version_ue4: int
    package_file_version_ue5: int
    engine_version_major: int
    engine_version_minor: int
    engine_version_patch: int
    engine_version_changelist: int
    engine_version_branch: str
    custom_version_format: int
    custom_versions: list
    save_game_class_name: str

@dataclass
class level_Properties:
    Version: properties_Version
    Timestamp: properties_Timestamp
    worldSaveData: properties_WorldSaveData

    def __post_init__(self):
        self.Version = properties_Version(**self.Version)
        self.Timestamp = properties_Timestamp(**self.Timestamp)
        self.worldSaveData = properties_WorldSaveData(**self.worldSaveData)

@dataclass
class LevelSav:
    header: Header
    properties: level_Properties
    trailer: str
    def __post_init__(self):
        self.header = Header(**self.header)
        self.properties = level_Properties(**self.properties)

import json
from dataclasses import asdict

