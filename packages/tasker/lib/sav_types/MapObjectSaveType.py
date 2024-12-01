from dataclasses import dataclass
from typing import List, Optional

"""
   Parsing Section 😫🤢🥺
"""
@dataclass
class MapObjectInstanceIdType:
    struct_type: str
    struct_id: str
    id: Optional[None]
    value: str
    type: str

@dataclass
class IMOSData_Values_Value:
    WorldLocation: Optional[None]
    WorldRotation: Optional[None]
    WorldScale3D: Optional[None]
    MapObjectId: Optional[None]
    MapObjectInstanceId: MapObjectInstanceIdType
    MapObjectConcreteModelInstanceId: Optional[None]
    Model: Optional[None]
    ConcreteModel: Optional[None]

    def __post_init__(self):
        self.MapObjectInstanceId = MapObjectInstanceIdType(**self.MapObjectInstanceId)

@dataclass
class IMOSData_Value:
    prop_name: str
    prop_type: str
    values: List[IMOSData_Values_Value]
    type_name: str
    id: str
    def __post_init__(self):
        self.values = [IMOSData_Values_Value(**x) for x in self.values]

@dataclass
class IMOSData:
    array_type: str
    id: Optional[None]
    value: IMOSData_Value
    type: str
    
    def __post_init__(self):
        self.value = IMOSData_Value(**self.value)
"""
   Parsed
"""

RawMapData=List[IMOSData_Values_Value]
RawMapObject=IMOSData_Values_Value