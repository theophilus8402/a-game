
import util

class Entity():

    def __init__(self, race, gender, first_name, last_name, loc, id=None):
        if id:
            self.id = id
        else:
            self.id = util.generate_id()
        self.race = race
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.loc = loc

    def __repr__(self):
        return f"<entity({self.first_name} {self.last_name}, ({self.loc}))>"


def generate_entity(world):
    gender = util.generate_gender()
    race = util.generate_race()
    loc = util.generate_loc(world)
    first_name, last_name = util.generate_name(gender, race, last_name=None)
    return Entity(
        race=race,
        gender=gender,
        first_name=first_name,
        last_name=last_name,
        loc=loc
    )
