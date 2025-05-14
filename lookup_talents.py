# talent_search.py

# Dictionary of talents and their associated numbers
talent_data = """
Blade Storm 1,1
Blade Storm 2,2
Grants Blade Storm,3
Vengeance Strike 1,4
Vengeance Strike 2,5
Grants Vengeance Strike,6
Riposte 1,7
Riposte 2,8
Grants Riposte,9
Second Chance 1,10
Second Chance 2,11
Grants Second Chance,12
Relentless 1,13
Relentless 2,14
Grants Relentless,15
Repel Boarders 1,16
Repel Boarders 2,17
Grants Repel Boarders,18
Cheap Shot 1,19
Cheap Shot 2,20
Grants Cheap Shot,21
Flanking 1,22
Flanking 2,23
Grants Flanking,24
Witch Hunter 1,25
Witch Hunter 2,26
Grants Witch Hunter,27
Double Tap 1,28
Double Tap 2,29
Grants Double Tap,30
Quick Draw 1,31
Quick Draw 2,32
Grants Quick Draw,33
True Grit 1,34
True Grit 2,35
Grants True Grit,36
Return Fire 1,37
Return Fire 2,38
Grants Return Fire,39
Quick Adjust 1,40
Quick Adjust 2,41
Grants Quick Adjust,42
Burst Fire 1,43
Burst Fire 2,44
Grants Burst Fire,45
Overwatch 1,46
Overwatch 2,47
Grants Overwatch,48
Parting Shot 1,49
Parting Shot 2,50
Grants Parting Shot,51
Crossfire 1,52
Crossfire 2,53
Grants Crossfire,54
First Strike 1,55
First Strike 2,56
Grants First Strike,57
Turn the Tide 1,88
Turn the Tide 2,89
Hold the Line 1,59
Hold the Line 2,61
Webs 1,60
Bloodsucker 1,62
Bloodsucker 2,63
Charming Gaze 1,64
Charming Gaze 2,65
Cornered! 1,66
Cornered! 2,67
Eagle Eyes 1,68
Eagle Eyes 2,69
Elusive 1,70
Elusive 2,71
Feeding Frenzy 1,72
Feeding Frenzy 2,73
Follow Through 1,74
Follow Through 2,75
Merciless 1,76
Merciless 2,77
Pirate 1,78
Pirate 2,79
Poisonous 1,80
Poisonous 2,81
Scent 1,82
Scent 2,83
Sneaky Sneaky 1,84
Sneaky Sneaky 2,85
Death Throes 1,86
Death Throes 2,87
Grants Armored 1,90
Grants Armored 2,91
Grants Tough 1,92
Grants Tough 2,93
Grants Dodgy 1,94
Grants Dodgy 2,95
Grants Resistant 1,96
Grants Resistant 2,97
Grants Accurate 1,98
Grants Accurate 2,99
Extra Accuracy 1,100
Extra Agility 1,101
Enhanced Armor 1,102
Enhanced Damage 1,103
Extra Dodgy 1,104
Loyal 1,105
Naturally Agile 1,106
Extra Gritty 1,107
Extra Guile 1,108
Extra Gutsy 1,109
Naturally Gifted 1,110
Naturally Strong 1,111
Naturally Tough 1,112
Naturally Spirited 1,113
Enhanced Movement 1,114
Gifted 1,115
Enhanced Magic Resist 1,116
Extra Strength 1,117
Enhanced Toughness 1,118
Extra Will 1,119
Enhanced Movement 2,120
Enhanced Movement 3,121
Enhanced Armor 2,122
Enhanced Armor 3,123
Extra Accuracy 2,124
Extra Accuracy 3,125
Enhanced Magic Resist 2,126
Enhanced Magic Resist 3,127
Extra Agility 2,128
Extra Agility 3,129
Extra Dodgy 2,130
Extra Dodgy 3,131
Extra Will 2,132
Extra Will 3,133
Extra Strength 2,134
Extra Strength 3,135
Enhanced Toughness 2,136
Enhanced Toughness 3,137
Loyal 2,138
Loyal 3,139
Gifted 2,140
Gifted 3,141
Enhanced Damage 2,142
Enhanced Damage 3,143
Naturally Spirited 2,144
Naturally Spirited 3,145
Naturally Tough 2,146
Naturally Tough 3,147
Naturally Strong 2,148
Naturally Strong 3,149
Naturally Gifted 2,150
Naturally Gifted 3,151
Extra Gutsy 2,152
Extra Gutsy 3,153
Extra Guile 2,154
Extra Guile 3,155
Extra Gritty 2,156
Extra Gritty 3,157
Naturally Agile 2,158
Naturally Agile 3,159
Grants Turn the Tide,160
Grants Pirate,161
Grants Elusive,162
Grants Hold the Line,163
Relentless 1.,164
Relentless 2.,165
Slippery,166
Grants Mojo Echo,167
Grants Mojo Rising,168
Grants Readied Spell,169
"""

# Build dictionary
talents = {}
for line in talent_data.strip().splitlines():
    name, number = line.strip().rsplit(',', 1)
    talents[name.strip().lower()] = number.strip()

# Search loop
def search_talents():
    while True:
        user_input = input("Enter talent name (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            break

        if user_input == "grants":
            print("All talents that start with 'Grants':")
            for name, number in talents.items():
                if name.startswith("grants"):
                    print(f"{name.title()}: {number}")
        else:
            result = talents.get(user_input)
            if result:
                print(f"Talent '{user_input.title()}' has number: {result}")
            else:
                # Fallback: fuzzy match for suggestions
                suggestions = [name.title() for name in talents if user_input in name]
                if suggestions:
                    print("Did you mean:")
                    for suggestion in suggestions:
                        print(f"  - {suggestion}")
                else:
                    print("Talent not found.")

# Run the script
if __name__ == "__main__":
    search_talents()
