import os
from steamfiles import acf


#########################################################
# To install:                                           #
# Downgrade to pip 9.0.1 and install steamfiles         #
#   python3 -m pip install --force-reinstall pip==9.0.1 #
#   pip3 install steamfiles                             #
# Upgrade pip back to the most recent version           #
#   python3 -m pip install --upgrade pip                #
#########################################################
    

# Extra games not on Steam
#           Name            Command
extras = [("Minecraft", "minecraft-launcher")]

# Games to omit
omit = ["Proton 3.16", "Steamworks Common Redistributables"]

#####################################################3

# Format for each case to be in:
#       "<title>") run_game <app_id>;;
case_format = lambda game: f"\"{game[0]}\") {game[1]};;"

if __name__ == "__main__":
    # Initial variables
    base_dir = os.path.expanduser("~/.steam/debian-installation/steamapps")
    files = os.listdir(base_dir)
    games = [game for game in files if "appmanifest" in game]

    game_list = []
    for game in games:
        path = os.path.join(base_dir, game)
        with open(path, "r") as g:
            json = acf.load(g)
            # For each game, need the title and the app id
            title = json["AppState"]["name"]
            cmd = "run_game " + json["AppState"]["appid"]
            if title not in omit:
                game_list.append((title, cmd))

    # Extract all of the names. This is for dmenu to list everything that's presently installed
    names = "\n".join([game[0] for game in game_list])
    # Extract all of the names + ids for use later. Will help determine what to do on selection
    cases = "\n".join([case_format(game) for game in game_list])

    # Handle extra games
    for extra in extras:
        names = names + ("\n" + extra[0])
        cases = cases + "\n" + case_format(extra)

    # This is the only way to run dmenu
    os.system(f"""
    run_game() {{
    steam steam://rungameid/$1 & disown; exit
    }}

    case "$(echo "{names}" | dmenu -i -nb '#1e1e1e' -sf '#aaff77' -sb '#1e1e1e' -nf '#ffffff' -p "Launch Game:")" in
    {cases}
    esac""")
