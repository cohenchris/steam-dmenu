# Steam Game Dmenu

## To install:
- Downgrade to pip 9.0.1 and install steamfiles
`python3 -m pip install --force-reinstall pip==9.0.1`
`pip3 install steamfiles`
- Upgrade pip back to the most recent version
`python3 -m pip install --upgrade pip`

## To bind in i3wm (for example)
`bindsym $mod+g exec python3 <path_to_script>`
