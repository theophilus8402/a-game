
import enum


class Status(enum.Enum):

    SUCCESS = 0

    # 100 - 199 entity related
    NAME_EXISTS = 100
    ID_EXISTS = 101

    # 200 - 299 map related
    OUT_OF_BOUNDS = 200
