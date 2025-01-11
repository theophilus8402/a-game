
import pytest

import entity
import gmap

from status import Status


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
def jim():
    return entity.Entity(
        race="human",
        gender="male",
        first_name="Jim",
        last_name="the Juggler",
        loc=(1, 3),
        id=2
    )


@pytest.fixture
def game_map():
    return gmap.Gmap(5, 5, -5, -5)


def test_in_bounds(tim):
    status, msg = gmap.in_bounds(tim, 5, 5, 0, 0)
    assert status == Status.SUCCESS

    status, msg = gmap.in_bounds(tim, 1, 1, 0, 0)
    assert status == Status.OUT_OF_BOUNDS


def test_can_fit(tim, game_map):
    new_loc = (4, 4)
    status, msg = gmap.can_fit(tim, new_loc, game_map)
    assert status == Status.SUCCESS

    tim.loc = new_loc
    status, msg = game_map.add_entity(tim)
    assert status == Status.SUCCESS

    status, msg = gmap.can_fit(tim, new_loc, game_map)
    assert status == Status.CANT_FIT


def test_gmap_add_entity(tim, jim, game_map):
    status, msg = game_map.add_entity(tim)
    assert status == Status.SUCCESS

    status, msg = game_map.add_entity(jim)
    assert status == Status.SUCCESS

    assert len(game_map.entities) == 2
