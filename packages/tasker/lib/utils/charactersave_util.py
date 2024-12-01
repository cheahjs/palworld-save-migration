from typing import List

from lib.sav_types.CharacterSaveParameterMap import RawChars, RawCharDetailData, RawChar
from lib.sav_types.type import LevelSav

def getRawCharacters(inputLevel: LevelSav)->RawChars:
    rawChars = inputLevel.properties.worldSaveData.value.CharacterSaveParameterMap.value
    return rawChars

def getRawChracterData(inputRawChars: RawChars)->RawCharDetailData:
    rawCharData = inputRawChars.value.RawData.value.object.SaveParameter.value
    return rawCharData

def getRawCharById(inputId: str, inputLevel:LevelSav):
    rawChars = getRawCharacters(inputLevel)
    for rawChar in rawChars:
        if getRawCharId(rawChar) == inputId:
            return rawChar

def getRawCharId(inputRawChar: RawChar):
    return inputRawChar.key.PlayerUId.value

def getRawCharGroupId(inputRawChar: RawChar):
    return inputRawChar.value.RawData.value.group_id

def getRawPlayers(inputLevel: LevelSav):
    rawChars = getRawCharacters(inputLevel)
    players: RawChars = []
    for rawChar in rawChars :
        rawCharData = getRawChracterData(rawChar)
        if rawCharData.IsPlayer :
            players.append(rawChar)
    return players
