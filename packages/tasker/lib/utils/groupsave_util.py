from lib.sav_types.GroupSaveDataMapType import RawGroupDataList
from lib.sav_types.type import LevelSav

def getRawGroupData(inputLevel: LevelSav)->RawGroupDataList:
    rawGroupData = inputLevel.properties.worldSaveData.value.GroupSaveDataMap.value
    return rawGroupData

def getRawGroupDataById(inputGroupId: str, inputRawGroupData: RawGroupDataList):
    for rawGroupData in inputRawGroupData:
        if rawGroupData.key == inputGroupId : 
            return rawGroupData
        
def getPlayerGuildByGroupId(inputGroupId: str, inputRawGroupData: RawGroupDataList):
    for rawGroupData in inputRawGroupData:
        if rawGroupData.key == inputGroupId and rawGroupData.value.GroupType.value.value == "EPalGroupType::Guild":
            return rawGroupData

def removeRawGroupDataById(inputInstanceId: str, inputRawGroupData: RawGroupDataList):
    index_to_remove = None
    for index, rawGroupData in enumerate(inputRawGroupData):
        if rawGroupData.key == inputInstanceId:
            index_to_remove = index
            break 
    if index_to_remove is not None:
        removed_object = inputRawGroupData.pop(index_to_remove)
        return removed_object
    return None 