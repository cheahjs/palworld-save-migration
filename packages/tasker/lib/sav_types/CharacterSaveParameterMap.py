from dataclasses import dataclass, fields
from typing import List, Optional

"""
   Parsing Section 😫🤢🥺
"""
@dataclass
class LevelType:
    id: Optional[None]
    value: int
    type: str

@dataclass
class GotStatusPointListType_Value_Values_StatusPoint:
    id: Optional[None]
    value: int
    type: str

@dataclass
class GotStatusPointListType_Value_Values_StatusName:
    id: Optional[None]
    value: str
    type: str

@dataclass
class GotStatusPointListType_Value_Values:
    StatusName: GotStatusPointListType_Value_Values_StatusName
    StatusPoint: GotStatusPointListType_Value_Values_StatusPoint
    def __post_init__(self):
        self.StatusName = GotStatusPointListType_Value_Values_StatusName(**self.StatusName)
        self.StatusPoint = GotStatusPointListType_Value_Values_StatusPoint(**self.StatusPoint)

@dataclass
class GotStatusPointListType_Value:
    prop_name: str
    prop_type: str
    values: List[GotStatusPointListType_Value_Values]
    type_name: str
    id: Optional[None]

    def __post_init__(self):
        self.values = [GotStatusPointListType_Value_Values(**x) for x in self.values]


@dataclass
class GotStatusPointListType:
    array_type: str
    id: Optional[None]
    value: GotStatusPointListType_Value
    type: str
    def __post_init__(self):
        self.value = GotStatusPointListType_Value(**self.value)

@dataclass
class UnusedStatusPointType:
    id: Optional[None]
    value: int
    type: str

@dataclass
class NickNameType:
    id: Optional[None]
    value: str
    type: str

@dataclass
class ICSPMap_Value_Value_RawData_Value_Object_SaveParameter_Value:
    Level:Optional[LevelType] = None
    UniqueNPCID: Optional[UnusedStatusPointType] = None
    UnusedStatusPoint: Optional[UnusedStatusPointType] = None
    GotStatusPointList: Optional[GotStatusPointListType] = None
    NickName: Optional[NickNameType]= None
    ############################################################################
    Rank: Optional[None] = None
    Rank_Defence: Optional[None] = None
    Rank_HP:Optional[None] = None
    Rank_CraftSpeed: Optional[None] = None
    Tiemr_FoodWithStatusEffect: Optional[None] = None
    FoodWithStatusEffect: Optional[None] = None
    IsRarePal: Optional[None] = None
    PalReviveTimer: Optional[None] = None
    CurrentWorkSuitability: Optional[None] = None
    Rank_Attack: Optional[None] = None
    BaseCampWorkerEventProgressTime: Optional[None] = None
    BaseCampWorkerEventType: Optional[None] = None
    WorkerSick: Optional[None] = None
    MaxFullStomach: Optional[None] = None
    Exp: Optional[None] = None
    HP: Optional[None]= None
    FullStomach: Optional[None]= None
    IsPlayer: Optional[None]= None
    MaxHP: Optional[None]= None
    MaxSP: Optional[None]= None
    Support: Optional[None]= None
    CraftSpeed: Optional[None]= None
    CraftSpeeds: Optional[None]= None
    LastJumpedLocation: Optional[None]= None
    VoiceID: Optional[None]= None
    SanityValue: Optional[None]= None
    DecreaseFullStomachRates: Optional[None]= None
    CraftSpeedRates: Optional[None]= None
    CharacterID: Optional[None]= None
    Gender: Optional[None]= None
    EquipWaza: Optional[None]= None
    MasteredWaza: Optional[None]= None
    Talent_HP: Optional[None]= None
    ShieldHP: Optional[None]= None
    ShieldMaxHP: Optional[None]= None
    Talent_Melee: Optional[None]= None
    Talent_Shot: Optional[None]= None
    Talent_Defense: Optional[None]= None
    FullStomach: Optional[None]= None
    MP: Optional[None]= None
    OwnedTime: Optional[None]= None
    OwnerPlayerUId: Optional[None]= None
    OldOwnerPlayerUIds: Optional[None]= None
    EquipItemContainerId: Optional[None]= None
    ItemContainerId: Optional[None]= None
    SlotID: Optional[None]= None
    PassiveSkillList: Optional[None]= None
    AffectSanityRates: Optional[None]= None
    PhysicalHealth: Optional[None] = None
    HungerType: Optional[None] = None
    def __post_init__(self):
        self.UnusedStatusPoint = UnusedStatusPointType(**self.UnusedStatusPoint) if self.UnusedStatusPoint else self.UnusedStatusPoint
        self.GotStatusPointList = GotStatusPointListType(**self.GotStatusPointList) if self.GotStatusPointList else self.GotStatusPointList
        self.Level = LevelType(**self.Level) if self.Level else self.Level
        self.NickName = NickNameType(**self.NickName) if self.NickName else self.NickName
    
@dataclass
class ICSPMap_Value_Value_RawData_Value_Object_SaveParameter:
    struct_type: str
    struct_id: str
    id: Optional[None]
    value: Optional[ICSPMap_Value_Value_RawData_Value_Object_SaveParameter_Value]
    type: str
    def __post_init__(self):
        self.value = ICSPMap_Value_Value_RawData_Value_Object_SaveParameter_Value(**self.value)

@dataclass
class ICSPMap_Value_Value_RawData_Value_Object:
    SaveParameter:ICSPMap_Value_Value_RawData_Value_Object_SaveParameter
    def __post_init__(self):
        self.SaveParameter = ICSPMap_Value_Value_RawData_Value_Object_SaveParameter(**self.SaveParameter)


@dataclass
class ICSPMap_Value_Value_RawData_Value:
    object: ICSPMap_Value_Value_RawData_Value_Object
    unknown_bytes: list[int]
    group_id: str

    def __post_init__(self):
        self.object = ICSPMap_Value_Value_RawData_Value_Object(**self.object)

@dataclass
class ICSPMap_Value_Value_RawData:
    array_type: str
    id: Optional[None]
    value: ICSPMap_Value_Value_RawData_Value
    type: str
    custom_type: str
    def __post_init__(self):
        self.value = ICSPMap_Value_Value_RawData_Value(**self.value)


@dataclass
class ICSPMap_Value_Value:
    RawData: ICSPMap_Value_Value_RawData
    def __post_init__(self):
        self.RawData = ICSPMap_Value_Value_RawData(**self.RawData)

@dataclass
class PlayerUIdType:
    struct_type: str
    struct_id: str
    id: Optional[None]
    value: str
    type: str

@dataclass
class ICSPMap_Value_Key:
    PlayerUId: PlayerUIdType
    InstanceId: Optional[None]
    DebugName: Optional[None]
    def __post_init__(self):
        self.PlayerUId = PlayerUIdType(**self.PlayerUId)

@dataclass
class ICSPMap_Value:
    key: Optional[ICSPMap_Value_Key]
    value: ICSPMap_Value_Value
    def __post_init__(self):
        self.key = ICSPMap_Value_Key(**self.key)
        self.value = ICSPMap_Value_Value(**self.value)

# CharacterSaveParameterMap
@dataclass
class ICSPMap:
    key_type: str
    value_type: str
    key_struct_type: str
    value_struct_type: str
    id: Optional[None]
    value: List[ICSPMap_Value]
    type: str
    def __post_init__(self):
        self.value = [ICSPMap_Value(**x) for x in self.value]
"""
   Parsed
"""

RawChars = List[ICSPMap_Value]
RawChar = ICSPMap_Value
RawCharKey = ICSPMap_Value_Key
RawCharDetailData = ICSPMap_Value_Value_RawData_Value_Object_SaveParameter_Value