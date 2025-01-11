
import fantasynames
import random


def generate_id(id=None):
    if id:
        return id
    return random.randint(1, 2000)

genders = ["male", "female"]
def generate_gender():
    return random.choices(genders, weights=[.6, .4])[0]


race_distribution = {
    "human": .5,
    "dwarf": .2,
    "elf": .2,
    "hobbit": .1
}


def generate_race():
    return random.choices(
        list(race_distribution.keys()),
        weights=race_distribution.values()
    )[0]


def generate_name(gender, race, last_name=None):
    match race:
        case "human":
            names = fantasynames.human
        case "dwarf":
            names = fantasynames.dwarf
        case "elf":
            names = fantasynames.elf
        case "hobbit":
            names = fantasynames.hobbit
    name = names(gender)
    first_name = name.split(" ")[0]
    if not last_name:
        last_name = " ".join(name.split(" ")[1:])
    return first_name, last_name


def generate_loc(gworld):
    x = random.randint(gworld.gmap.min_x, gworld.gmap.max_x)
    y = random.randint(gworld.gmap.min_y, gworld.gmap.max_y)
    return (x, y)
