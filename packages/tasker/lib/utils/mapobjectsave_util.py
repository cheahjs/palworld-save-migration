from lib.sav_types.MapObjectSaveType import RawMapData
from lib.sav_types.type import LevelSav

def getRawMapObjectData(inputLevel: LevelSav)->RawMapData:
    rawMapObjectData = inputLevel.properties.worldSaveData.value.MapObjectSaveData.value.values
    return rawMapObjectData

def getRawMapObjectById(inputInstanceId: str, inputRawMapData: RawMapData):
    for rawMapObject in inputRawMapData:
        if rawMapObject.MapObjectInstanceId.value == inputInstanceId:
            return rawMapObject
        
def removeRawMapObjectById(inputInstanceId: str, inputRawMapData: RawMapData):
    index_to_remove = None
    for index, rawMapObject in enumerate(inputRawMapData):
        if rawMapObject.MapObjectInstanceId.value == inputInstanceId:
            index_to_remove = index
            break 
    if index_to_remove is not None:
        removed_object = inputRawMapData.pop(index_to_remove)
        return removed_object
    return None 