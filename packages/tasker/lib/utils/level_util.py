from dataclasses import is_dataclass

from lib.sav_types.type import LevelSav
from lib.sav_types.utilType import Null

import json

def dataclass_to_dict(instance):
    if isinstance(instance, list):
        return [dataclass_to_dict(item) for item in instance]
    elif is_dataclass(instance):
        return {
            key: dataclass_to_dict(getattr(instance, key)) 
            for key in instance.__dataclass_fields__ 
            if getattr(instance, key) is not None
        }
    elif isinstance(instance, dict):
        return {
            key: dataclass_to_dict(value) 
            for key, value in instance.items() 
            if value is not None
        }
    else:
        return instance
    
def __json_decode_hook__(dct):
    for key, value in dct.items():
        if value is None:
            dct[key] = Null()
    return dct

def __json_encode_default__(obj):
    if isinstance(obj, Null):
        return None
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def loadSavJson(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        jsonData = json.load(file, object_hook=__json_decode_hook__)
    return jsonData

def dumpSavJson(filePath, inputLevelSav: LevelSav):
    saveData_dict = dataclass_to_dict(inputLevelSav)
    with open(filePath, "w", encoding="utf8") as f:
        json.dump(saveData_dict, f, default=__json_encode_default__, indent=2, ensure_ascii=False)
        print(f"Data successfully written to {filePath}")