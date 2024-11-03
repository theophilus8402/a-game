
from status import Status

class World():

    def __init__(self, name):
        self.name = name
        self.entities = []

    def add_entity(self, entity):
        if not unique_name(entity, self):
            return Status.NAME_EXISTS, f"{entity.first_name} {entity.last_name} already exists in {self.name}."
        self.entities.append(entity)
        return Status.SUCCESS, ""


def unique_name(entity, world):
    for ent in world.entities:
        if ((ent.first_name.lower() == entity.first_name.lower()) and
            (ent.last_name.lower() == entity.last_name.lower())):
            return False
    return True
