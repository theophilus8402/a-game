
import pytest

import gmap
import util
import world


@pytest.fixture
def game_map():
    return gmap.Gmap(5, 5, -5, -5)


@pytest.fixture
def game_world(game_map):
    return world.World("DiscWorld", game_map)


def test_generate_id():
    assert util.generate_id(7) == 7
    assert 1 <= util.generate_id() <= 2000


def test_generate_gender():
    assert util.generate_gender() in util.genders
    assert util.generate_gender() in util.genders


def test_generate_race():
    assert util.generate_race() in util.race_distribution.keys()
    assert util.generate_race() in util.race_distribution.keys()


def test_generate_name():
    first_name, last_name = util.generate_name("male", "dwarf", last_name=None)
    assert first_name != ""
    assert last_name != ""

    tfirst_name, tlast_name = util.generate_name("female", "dwarf", last_name=last_name)
    assert tlast_name == last_name


def test_generate_loc(game_map, game_world):
    x, y = util.generate_loc(game_world)
    assert game_map.min_x <= x <= game_map.max_x
    assert game_map.min_y <= y <= game_map.max_y
