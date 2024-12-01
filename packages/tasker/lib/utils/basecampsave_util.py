from lib.sav_types.BaseCampSaveDataType import RawBaseCampData
from lib.sav_types.type import LevelSav

def getRawBaseCampSaveData(inputLevel: LevelSav)->RawBaseCampData:
    rawBaseCampData = inputLevel.properties.worldSaveData.value.BaseCampSaveData.value
    return rawBaseCampData