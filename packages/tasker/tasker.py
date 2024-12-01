import argparse
import json
import os

from tasks.init_player_points import initPlayerPoints
from tasks.get_player_info import getPlayersInfo

def main():
    parser = argparse.ArgumentParser(
        prog="palworld-save-tools/tasker",
        description="Execute predefined tasks for palworld save file.",
    )
    parser.add_argument("taskname", nargs="?")
    parser.add_argument("jsonfile", nargs="?")
    parser.add_argument(
        "--task-list",
        action="store_true",
        help="show task lists",
    )
    parser.add_argument(
        "--output",
        action="store_true",
        help="output filename",
    )
    args = parser.parse_args()
    if(args.task_list):
        print("Task List")
        print("\t- get_player_info ${LevelJsonFile} \n\t\t remove players\n")
        print("\t- init_player_points ${LevelJsonFile}\n\t\t init all players status point.\n")
        print("\t- remove_all_pal_beacon ${LevelJsonFile}\n\t\t remove all players pal beacon.\n")
        # print("\t- remove_player ${removePlayersJsonDirectory} ${LevelJsonFile}\n\t\t remove players\n")
    if args.taskname == "get_player_info":
        getPlayersInfo(args.jsonfile)

    if args.taskname == "init_player_points":
        initPlayerPoints(args.jsonfile, args.output)

    return 0

if __name__ == "__main__":
    main()
