# Steam Game Dmenu

## Description

- This script scans the `~/.steam/` directory and finds available games to launch. It then displays them on dmenu and launches the game selected.
- If you'd like any extra game executables to be included, list them in the 'extras' array. They should be added in a new tuple, in the format `(name, command_to_execute)`.
- If you'd like to exclude any games, list their names in the 'omit' array. I have already included a couple of 'games' that this script finds that are useless.

## To install:
Downgrade to pip 9.0.1, install steamfiles, and upgrade pip back to the most recent version:
```
python3 -m pip install --force-reinstall pip==9.0.1
pip3 install steamfiles
python3 -m pip install --upgrade pip
```

## To bind in i3wm (for example)
`bindsym $mod+g exec python3 <path_to_script>`
