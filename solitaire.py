import enum

@enum.unique
class GAME_MODE(enum.Enum):
    Klondike = 1

_STATS_FILENAME="stats.txt"

def load_stats():
    # Open and read the stats file
    stats_file = open(_STATS_FILENAME, "r")
    print("Stats file contents:")
    print(stats_file.read())
    stats_file.close()

def update_stats():
    # TODO - update stats
    stats_file = open(_STATS_FILENAME, "w")
    stats_file.write("Solitaire Statistics")
    stats_file.close()
    print("Updated statistics successfully")

def solitaire():
    game_mode = GAME_MODE.Klondike
    print("Solitaire")
    print(game_mode.name)

    # TODO - parse stats data into a class
    load_stats()

    # Update and write stats back
    update_stats()

solitaire()