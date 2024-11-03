
import entity
import util
import world

from status import Status


if __name__ == "__main__":

    game_world = world.World("Disc World")
    print(f"Hello, {game_world.name}!")

    bob = entity.Entity(
        race="human",
        gender="male",
        first_name="Bob",
        last_name="the Butcher"
    )
    status, msg = game_world.add_entity(bob)
    print(f"Hello, {bob.first_name} ({bob.id})!")

    tim = entity.Entity(
        race="human",
        gender="male",
        first_name="Tim",
        last_name="the Tosser",
        id=27
    )
    status, msg = game_world.add_entity(tim)
    print(f"Hello, {tim.first_name} ({tim.id})!")

    status, msg = game_world.add_entity(tim)
    if status != Status.SUCCESS:
        print(f"ERROR: {msg}")
    else:
        print(f"Hello, {tim.first_name} ({tim.id})!")

    first_name, last_name = util.generate_name("female", "elf", last_name=None)
    print(f"Hello, {first_name} {last_name}!")

    for i in range(10):
        ent = entity.generate_entity()
        status, msg = game_world.add_entity(ent)
        if status != Status.SUCCESS:
            print(f"ERROR: {msg}")
            continue
        print(f"{ent.first_name} {ent.last_name} ({ent.id}), {ent.gender}, {ent.race}")

    print(game_world.entities)
