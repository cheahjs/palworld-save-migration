"""get all Players nickname and PlayerUID
"""

from lib.sav_types.type import LevelSav
from lib.sav_types.utilType import Null

from lib.utils.level_util import loadSavJson, dumpSavJson
from lib.utils.charactersave_util import getRawPlayers

def getPlayersInfo(inputJsonFilePath, outputFilePath=None):
    print("LETS GO!")
    file_path = inputJsonFilePath
    output_file_path = "playerinfo.txt"

    jsonData = loadSavJson(file_path)
    saveData = LevelSav(**jsonData)
    rawPlayers = getRawPlayers(saveData)
    if outputFilePath: output_file_path = outputFilePath

    playerInfo = []

    for rawPlayer in rawPlayers:
        nickname=""
        playerUid=""
        rawData = rawPlayer.value.RawData.value.object.SaveParameter.value
        if rawData:
            if rawData.NickName:
                if rawData.NickName.value:
                    nickname=rawData.NickName.value
        if rawPlayer.key:
            if rawPlayer.key.PlayerUId:
                if rawPlayer.key.PlayerUId.value:
                    playerUid=rawPlayer.key.PlayerUId.value
        if nickname:
            playerInfo.append([nickname, playerUid])
    with open(output_file_path, "w", encoding="utf8") as f:
        for info in playerInfo:
            line = f"{info[0]}, {info[1]}\n"  # 닉네임과 PlayerUID를 콤마와 함께 한 줄로 변환
            f.write(line)
        print(f"Data successfully written to {output_file_path}")