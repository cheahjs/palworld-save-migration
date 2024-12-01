from dataclasses import dataclass, fields
from typing import List, Optional

"""
   Parsing Section 😫🤢🥺
"""
@dataclass
class IBCSD_Value_Value:
    WorkerDirector: Optional[None]
    WorkCollection: Optional[None]
    ModuleMap: Optional[None]
    RawData: Optional[None]

@dataclass
class IBCSD_Value:
    key: str
    value: IBCSD_Value_Value
    def __post_init__(self):
        self.value = IBCSD_Value_Value(**self.value)

@dataclass
class IBCSD:
    key_type: str
    value_type: str
    key_struct_type: str
    value_struct_type: str
    id: Optional[None]
    value: List[IBCSD_Value]
    type: str
    def __post_init__(self):
        self.value = [IBCSD_Value(**x) for x in self.value]
"""
   Parsed
"""

RawBaseCampData = List[IBCSD_Value]
RawBaseCamp = IBCSD_Value
RawBaseCampData = IBCSD_Value_Value