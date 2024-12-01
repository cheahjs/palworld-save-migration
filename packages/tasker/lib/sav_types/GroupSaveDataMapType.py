from dataclasses import dataclass, fields
from typing import List, Optional

"""
   Parsing Section 😫🤢🥺
"""
@dataclass
class IndividualCharacterHandleIds:
    guid: str
    instance_id: str

@dataclass
class Players_PlayerInfo:
    last_online_real_time: int
    player_name: str

@dataclass
class Players:
    player_uid: str
    player_info: Players_PlayerInfo
    def __post_init__(self):
        self.player_info = Players_PlayerInfo(**self.player_info)

@dataclass
class IGSDMap_Value_Value_RawData_Value:
    group_type: str
    group_id: str
    group_name: str
    individual_character_handle_ids: list
    org_type: Optional[int] = None
    base_ids: Optional[list[int]] = None
    base_camp_level: Optional[int] = None
    map_object_instance_ids_base_camp_points: Optional[int] = None
    guild_name: Optional[str] = None
    admin_player_uid: Optional[str] = None
    players: Optional[Players] = None

    def __post_init__(self):
        self.players = [Players(**x) for x in self.players] if self.players else self.players
        for field in fields(self):
            if getattr(self, field.name) is None:
                delattr(self, field.name)

@dataclass
class GroupType_value:
    type:str
    value:str

@dataclass
class GroupTypeType:
    id: Optional[None]
    type: Optional[None]
    value: GroupType_value
    def __post_init__(self):
        self.value = GroupType_value(**self.value)

@dataclass
class IGSDMap_Value_Value_RawData:
    array_type: str
    id: Optional[None]
    value: Optional[IGSDMap_Value_Value_RawData_Value]
    type: Optional[None]
    
    def __post_init__(self):
        self.value = IGSDMap_Value_Value_RawData_Value(**self.value)

@dataclass
class IGSDMap_Value_Value:
    GroupType: Optional[GroupTypeType] = None
    RawData: Optional[IGSDMap_Value_Value_RawData] = None
    def __post_init__(self):
        self.GroupType = GroupTypeType(**self.GroupType);
        self.RawData = IGSDMap_Value_Value_RawData(**self.RawData)
        for field in fields(self):
            if getattr(self, field.name) is None:
                delattr(self, field.name)

@dataclass
class IGSDMap_Value:
    key: str
    value: Optional[IGSDMap_Value_Value] = None
    def __post_init__(self):
        self.value = IGSDMap_Value_Value(**self.value) 
        for field in fields(self):
            if getattr(self, field.name) is None:
                delattr(self, field.name)

@dataclass
class IGSDMap:
    key_type: str
    value_type: str
    key_struct_type: str
    value_struct_type: str
    id: Optional[None]
    value: List[IGSDMap_Value]
    type: str
    custom_type: str
    
    def __post_init__(self):
        self.value = [IGSDMap_Value(**x) for x in self.value]
"""
   Parsed
"""

RawGroupDataList = List[IGSDMap_Value]
RawGroupData = IGSDMap_Value