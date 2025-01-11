
import entity
import util
import gmap
import view
import world

from status import Status


if __name__ == "__main__":

    game_map = gmap.Gmap(10, 10, -10, -10)

    game_world = world.World("Disc World", gmap=game_map)
    print(f"Hello, {game_world.name}!")

    bob = entity.Entity(
        race="human",
        gender="male",
        first_name="Bob",
        last_name="the Butcher",
        loc=(1, 2),
        id=27
    )
    status, msg = game_world.add_entity(bob)
    print(f"Hello, {bob.first_name} ({bob.id})!")

    tim = entity.Entity(
        race="human",
        gender="male",
        first_name="Tim",
        last_name="the Tosser",
        loc=(2, 2)
    )
    status, msg = game_world.add_entity(tim)
    if status != Status.SUCCESS:
        print(f"ERROR: {msg}")
    else:
        print(f"Hello, {tim.first_name} ({tim.id})!")

    status, msg = game_world.add_entity(tim)
    if status != Status.SUCCESS:
        print(f"ERROR: {msg}")
    else:
        print(f"Hello, {tim.first_name} ({tim.id})!")

    first_name, last_name = util.generate_name("female", "elf", last_name=None)
    print(f"Hello, {first_name} {last_name}!")

    for i in range(10):
        ent = entity.generate_entity(game_world)
        status, msg = game_world.add_entity(ent)
        if status != Status.SUCCESS:
            print(f"ERROR: {msg}")
            continue
        print(f"{ent.first_name} {ent.last_name} ({ent.id}), {ent.gender}, {ent.race}")

    print(game_world.entities)

    print(f"Adding Bob to ({bob.loc})")
    status, msg = game_map.add_entity(bob)
    if status != Status.SUCCESS:
        print(f"ERROR: {msg}")
    else:
        print(f"Added {bob.first_name} to ({bob.loc})!")

    new_loc = (22, 3)
    print(f"Moving Tim to ({new_loc})")
    tim.loc = new_loc
    status, msg = game_map.add_entity(tim)
    print(f"Adding Tim to ({tim.loc})")
    if status != Status.SUCCESS:
        print(f"ERROR: {msg}")
    else:
        print(f"Added {tim.first_name} to ({tim.loc})!")

    view.display_map(game_map, 5, 5, (-5, 5))
