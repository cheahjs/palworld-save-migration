# palworld-save-tools
Tools for converting Palworld .sav files to JSON and back.

This tool currently supports additional parsing of the following data in the `Level.sav` not handled by `uesave` or other non-Palworld aware Unreal save editors:

1. `GroupSaveDataMap`
    - Groups such as in-game organizations and guilds
1. `CharacterSaveParameterMap`
    - Characters such as players and pals
1. `MapObjectSaveData.MapObjectSaveData.Model`
1. `ItemContainerSaveData`
1. `CharacterContainerSaveData`
1. `DynamicItemSaveData`
1. `FoliageGridSaveDataMap`
1. `BaseCampSaveData`
1. `WorkSaveData`

Some fields that are not currently parsed:

1. `BaseCampSaveData.Value.ModuleMap`
1. `MapObjectSaveData.MapObjectSaveData.ConcreteModel`

## Converting co-op saves to dedicated server saves

Please follow the instructions provided over at https://github.com/xNul/palworld-host-save-fix

## Instructions

> [!IMPORTANT]
> Converting `Level.sav` files to JSON will result in very large files, and may require significant amounts of RAM to process. Use a modern text editor such as Visual Studio Code or a Jetbrains IDE to open these files.

### Prerequisites

1. Python 3.9 or newer.
    - Windows users: You can install [Python 3.12 from the Microsoft Store](https://apps.microsoft.com/detail/9NCVDN91XZQP) or from [python.org](https://www.python.org/)

### Windows GUI steps

1. Download the latest release from [https://github.com/cheahjs/palworld-save-tools/releases/latest].
1. Unzip the file into a folder.
1. Drag and drop your `.sav` file (for Steam on Windows, these are located at `%LOCALAPPDATA%\Pal\Saved\SaveGames\<SteamID>\<SaveID>`) onto `convert.cmd` to convert the file into JSON.
1. To convert the `.sav.json` file back into a `.sav` file, drag and drop your `.sav.json` file onto `convert.cmd`.

> [!NOTE]
> In the event that the `convert.cmd` fails to function correctly, try to disable Python's app execution aliases ("Manage app execution aliases"), or failing that, please use the [Terminal](#terminal) instructions below

### Terminal

1. Download the latest release from [https://github.com/cheahjs/palworld-save-tools/releases/latest].
1. Unzip the file into a folder.
1. Open a terminal in the folder you just unzipped.
1. Depending on how Python is installed, the next steps should use either `python`, `python3`, or `py`.
1. Run `python convert.py <path to .sav file>` to convert the `.sav` file to a `.sav.json` file.
1. Run `python convert.py <path to .json file>` to convert the `.sav.json` file to a `.sav` file.

> [!NOTE]
> On Windows, you can drag and drop the `convert.py` file and the `.sav`/`.sav.json` file to avoid typing out the path.

Additional command line arguments:

1. `--to-json`: Force SAV to JSON conversion regardless of file extension
1. `--from-json`: Force JSON to SAV conversion regardless of file extension
1. `--output`: Override the default output path
1. `--minify-json`: Minify output JSON to help speed up processing by other tools consuming JSON
1. `--force`: Overwrite output files if they exist without prompting

### Cleanup Tools

This tools is for cleanup the unreference item, rename the player name, migrate player and delete the player.

For cleaning the character and the guild, use the follow command `python palworld-cleanup-tools.py --fix-missing --fix-capture Level.sav`

For modifiy the `Level.sav` file, use the follow command
`python -i palworld-cleanup-tools.py Level.sav`

The tools have the following commands in interactive mode:

1. `ShowPlayers()`: List the Players
1. `FixMissing()`: Remove missing player instance
1. `ShowGuild(fix_capture=False)`: List the Guild and members
1. `RenamePlayer(uid,new_name)`: Rename player to new_name
1. `DeletePlayer(uid,InstanceId=None, dry_run=False)`: Wipe player data from save InstanceId: delete specified InstanceId
1. `EditPlayer(uid)`: Allocate player base meta data to variable 'player'
1. `OpenBackup(filename)`: Open Backup Level.sav file and assign to backup_wsd
1. `MigratePlayer(old_uid,new_uid)`: Migrate the player from old PlayerUId to new PlayerUId
1. `CopyPlayer(old_uid,new_uid, backup_wsd)`: Copy the player from old PlayerUId to new PlayerUId
1. `Save()`: Save the file and exit
