""" This taks to remove every pal beacon. it just remove beacon. 
do not players and players pals
"""
import os

from typing import List

from lib.sav_types.type import LevelSav
from lib.sav_types.CharacterSaveParameterMap import RawChar
from lib.sav_types.GroupSaveDataMapType import RawGroupDataList

from lib.utils.level_util import dataclass_to_dict, loadSavJson, dumpSavJson
from lib.utils.charactersave_util import getRawPlayers, getRawCharId, getRawCharGroupId
from lib.utils.groupsave_util import getPlayerGuildByGroupId, getRawGroupData
from lib.utils.mapobjectsave_util import getRawMapObjectData, removeRawMapObjectById
from lib.utils.basecampsave_util import getRawBaseCampSaveData

file_path = os.path.join(os.path.dirname(__file__), "initedPlayersPoint.json")
jsonData = loadSavJson(file_path)

saveData = LevelSav(**jsonData)
rawGroupData = getRawGroupData(saveData)
rawMapObjectData = getRawMapObjectData(saveData)
rawBaseCampData = getRawBaseCampSaveData(saveData)

rawPlayers = getRawPlayers(saveData)

playerIds:List[RawChar]  = []
guilds:RawGroupDataList = []
baseCampInstanceIdss:List[List[str]] = []

for player in rawPlayers:
    playerId = getRawCharId(player)
    groupId = getRawCharGroupId(player)
    playerIds.append([playerId, groupId])

for playerId, groupId in playerIds:
    guilds.append(getPlayerGuildByGroupId(groupId, rawGroupData))

for guild in guilds:
    if guild:
        if guild.value.RawData:
            baseCampInstanceIdss.append(guild.value.RawData.value.map_object_instance_ids_base_camp_points)

# Move Pal workers to pal container
# @haveto

# Remove BaseCamps on GroupData::Guild
## Delete base_ids
## Delete map_object_instance_ids_base_camp_points
for guild in guilds:
    guild.value.RawData.value.base_ids = []
    guild.value.RawData.value.map_object_instance_ids_base_camp_points = []

# Remove BaseCampSaveData
saveData.properties.worldSaveData.value.BaseCampSaveData.value = []

# Remove BaseCamp on World
for baseCampInstanceIds in baseCampInstanceIdss:
    for baseCampId in baseCampInstanceIds:
        removeRawMapObjectById(baseCampId, rawMapObjectData)

output_path = "removedAllPlayerBaseCamp.json"
dumpSavJson(output_path, saveData)
