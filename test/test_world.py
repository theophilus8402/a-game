
import pytest

import entity
import gmap
import world


@pytest.fixture
def tim():
    return entity.Entity(
        race="human",
        gender="male",
        first_name="Tim",
        last_name="the Torturer",
        loc=(1, 2),
        id=2
    )


@pytest.fixture
def timothy():
    return entity.Entity(
        race="human",
        gender="male",
        first_name="Timothy",
        last_name="the Torturer",
        loc=(1, 2),
        id=3
    )


@pytest.fixture
def game_map():
    return gmap.Gmap(5, 5, -5, -5)


@pytest.fixture
def game_world(game_map):
    return world.World("DiscWorld", game_map)


def test_unique_name(tim, timothy, game_world):
    assert world.unique_name(tim, game_world)

    game_world.add_entity(tim)
    assert not world.unique_name(tim, game_world)

    assert world.unique_name(timothy, game_world)


def test_unique_id(tim, timothy, game_world):
    assert world.unique_id(tim, game_world)

    game_world.add_entity(tim)
    assert not world.unique_id(tim, game_world)

    assert world.unique_id(timothy, game_world)
