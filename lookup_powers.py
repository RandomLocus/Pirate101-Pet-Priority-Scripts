# power_search.py

# Dictionary of powers and their associated numbers
power_data = """
Nautilus Lunge,1
Chiton Blast,2
Kappa's Caper,3
Nautilus Leap,4
Chiton Burst,5
Kappa's Waltz,6
Cuttlefish Grasp,7
Mako Shot,8
Narwhal's Spell,9
Tentacular Spectacular,10
Mako Storm,11
Narwhal's Song,12
Blackwater Deeps,13
Jonah's Curse,14
Kraken's Cave,15
Fathomless Deeps,16
Jonah's Hex,17
Kraken's Grotto,18
Sargasso Strike,19
Sargasso Shot,20
Cachalot's Grip,21
Cachalot's Grasp,22
Lightning Strike,23
Lightning Shot,24
Thunderstrike,25
Lightning Surge,26
Lightning Storm,27
Thunderclap,28
Tailwinds,29
Skyfall,30
Stormburst,31
Muckblast,32
Entangling Muck,33
Oozeburst,34
Entangling Ooze,35
Darksky Strike,36
Darksky Shot,37
Darksky Spell,38
Surge of Despair,39
Storm of Despair,40
Song of Despair,41
Spirited Surge,42
Spirited Screech,43
Spirited Song,44
Unbalancing Shout,45
Black Kestrel Call,46
Owl's Prey,47
Black Roc Call,48
Black Kestrel Screech,49
Black Hawk Screech,50
Black Roc Screech,51
Hunter's Bane,52
Harrier's Bane,53
Hector's Bane,54
Windstalker,55
Cloudstalker,56
Skystalker,57
Sidewinder Strike,58
Cobra Strike,59
Basilisk Strike,60
Sidewinder's Favor,61
Cobra's Favor,62
Basilisk's Favor,63
Shattering Strike,64
Shattering Shot,65
Shattering Spell,66
Blade of 100 Ninjas,67
Blade of 1000 Ninjas,68
Blade of 10000 Ninjas,69
Enfeebling Bite,70
Enfeebling Spines,71
Enfeebling Shriek,72
Sorrowful Touch,73
Shadowy Touch,74
Spectral Touch,75
Sorrowful Aura,76
Shadowy Aura,77
Spectral Aura,78
Ancestral Strike,79
Ancestral Shot,80
Ancestral Spell,81
Shambling Corpse,82
Zombie's Curse,83
Shambling Horde,84
Epic Shot,85
Mega Shot,86
Super Shot,87
Epic Storm,88
Mega Storm,89
Super Storm,90
Epic Strike,91
Mega Strike,92
Super Strike,93
Epic Surge,94
Mega Surge,95
Super Surge,96
Kestrel's Prey,97
Owl's Cry,98
Eagle's Prey,99
Kestrel's Clutches,100
Owl's Clutches,101
Eagle's Clutches,102
Toxic Touch,103
Toxic Spittle,104
Virulent Claws,105
Virulent Musk,106
Epic Spell,107
Mega Spell,108
Super Spell,109
Epic Song,110
Mega Song,111
Super Song,112
Banshee Shriek,113
Banshee Wail,114
Vampiric Touch,115
Vampiric Gaze,116
Vampiric Umbra,117
Ravenous Maw,118
Ravenous Gaze,119
Ravenous Frenzy,120
Kraken's Lament,121
Wind Spirit,122
Cloud Spirit,123
Sneak Attack,124
Sneak Attack,125
Triton's Song,126
Jobu's Breath,127
Jobu's Kiss,128
Mojo Strike,129
Ghostwail,130
Rouse,131
Refresh,132
Mighty Charge,133
Assassin's Mist,134
Kraken's Coils,135
Hoodoo Touch,136
Calm the Troops,137
Steadying Speech,138
Mutineer's Grasp,139
Shark's Fury,140
Assassin's Gloom,141
Brutal Charge,142
Regroup,143
Rally,144
Soulreaver,145
Mojo Blast,146
Grants Calm the Troops,147
Grants Hoodoo Touch,148
Grants Kraken's Coils,149
Grants Assassin's Mist,150
Grants Mighty Charge,151
Grants Refresh,152
Grants Rouse,153
Grants Ghostwail,154
Grants Mojo Strike,155
Grants Jobu's Breath,156
Grants Triton's Song,157
Grants Sneak Attack,158
Grants Wind Spirit,159
Grants Steadying Speech,160
Grants Mutineer's Grasp,161
Grants Shark's Fury,162
Grants Assassin's Gloom,163
Grants Brutal Charge,164
Grants Regroup,165
Grants Rally,166
Grants Soulreaver,167
Grants Mojo Blast,168
Grants Jobu's Kiss,169
Grants Kraken's Lament,170
Grants Back Stab,171
Grants Cloud Spirit,172
Victory Pie,173
Sweet Meteor of Doom,174
Fandango,175
Get Chummy,176
Lionheart,177
Time Warp,178
Ice-O-Lation,179
Sandstorm,180
Earthquack,181
Rainbow Blessing,182
"""

# Build dictionary
powers = {}
for line in power_data.strip().splitlines():
    name, number = line.strip().rsplit(',', 1)
    powers[name.strip().lower()] = number.strip()

# Search loop
def search_powers():
    while True:
        user_input = input("Enter power name (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            break

        if user_input == "grants":
            print("All powers that start with 'Grants':")
            for name, number in powers.items():
                if name.startswith("grants"):
                    print(f"{name.title()}: {number}")
        else:
            result = powers.get(user_input)
            if result:
                print(f"Power '{user_input.title()}' has number: {result}")
            else:
                # Fallback: fuzzy match for suggestions
                suggestions = [name.title() for name in powers if user_input in name]
                if suggestions:
                    print("Did you mean:")
                    for suggestion in suggestions:
                        print(f"  - {suggestion}")
                else:
                    print("Power not found.")

# Run the script
if __name__ == "__main__":
    search_powers()
