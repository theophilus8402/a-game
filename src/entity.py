
import util

class Entity():

    def __init__(self, race, gender, first_name, last_name, id=None):
        if id:
            self.id = id
        else:
            self.id = util.generate_id()
        self.race = race
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name


def generate_entity():
    gender = util.generate_gender()
    race = util.generate_race()
    first_name, last_name = util.generate_name(gender, race, last_name=None)
    return Entity(
        race=race,
        gender=gender,
        first_name=first_name,
        last_name=last_name,
    )
