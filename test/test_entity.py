
import pytest

import entity
import gmap
import world

from status import Status


@pytest.fixture
def game_map():
    return gmap.Gmap(5, 5, -5, -5)


@pytest.fixture
def game_world(game_map):
    return world.World("DiscWorld", game_map)


def test_entity_init():
    tim = entity.Entity(
        race="human",
        gender="male",
        first_name="Tim",
        last_name="the Torturer",
        loc=(1, 2),
        id=2
    )
    assert tim.first_name == "Tim"
    assert tim.loc == (1, 2)


def test_generate_entity(game_world):
    ent = entity.generate_entity(game_world)
    assert ent.first_name != ""
    assert ent.race != ""
