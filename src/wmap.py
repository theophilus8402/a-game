
from status import Status


def in_bounds(entity, max_x, max_y, min_x, min_y):
    x, y = entity.loc

    if x > max_x:
            return Status.OUT_OF_BOUNDS, f"OUT OF BOUNDS: {entity.first_name} x ({x}) > max_x ({max_x})"

    if y > max_y:
            return Status.OUT_OF_BOUNDS, f"OUT OF BOUNDS: {entity.first_name} y ({y}) > max_y ({max_y})"

    if x < min_x:
        return Status.OUT_OF_BOUNDS, f"OUT OF BOUNDS: {entity.first_name} x ({x}) < max_x ({max_x})"

    if y < min_y:
        return Status.OUT_OF_BOUNDS, f"OUT OF BOUNDS: {entity.first_name} y ({y}) < max_y ({max_y})"

    return Status.SUCCESS, ""


class Wmap():

    def __init__(self, max_x, max_y, min_x, min_y):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y

        self.entities = {}

    def add_entity(self, entity):
        status, msg = in_bounds(entity, self.max_x, self.max_y, self.min_x, self.min_y)
        if status != Status.SUCCESS:
            return (status, msg)

        self.entities[entity.loc] = entity
        return Status.SUCCESS, ""
