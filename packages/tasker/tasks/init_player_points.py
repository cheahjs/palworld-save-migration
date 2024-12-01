""" Init (all)Players all skill and status point
"""
import os

from lib.sav_types.type import LevelSav
from lib.sav_types.utilType import Null

from lib.utils.level_util import loadSavJson, dumpSavJson
from lib.utils.charactersave_util import getRawPlayers

def initPlayerPoints(inputJsonFilePath, outputJsonFile=None):
    file_path = inputJsonFilePath

    jsonData = loadSavJson(file_path)
    saveData = LevelSav(**jsonData)
    rawPlayers = getRawPlayers(saveData)

    for rawPlayer in rawPlayers:
        rawData = rawPlayer.value.RawData.value.object.SaveParameter.value
        if rawData and rawData.Level:
            initPoint = rawData.Level.value - 1 or 0
            rawPlayer.value.RawData.value.object.SaveParameter.value.UnusedStatusPoint = {"id": Null(), "value": initPoint, "type": "IntProperty"}
            if rawData.GotStatusPointList:
                for rawStatusPoint in rawData.GotStatusPointList.value.values:
                    if rawStatusPoint.StatusName.value == "\u6355\u7372\u7387":
                        continue
                    rawStatusPoint.StatusPoint.value = 0
    name_without_ext = os.path.splitext(os.path.basename(inputJsonFilePath))
    output_path = f"{name_without_ext}.intiated.json"
    if outputJsonFile: output_path = outputJsonFile
    dumpSavJson(output_path, saveData)
