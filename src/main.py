
import entity
import util
import world


if __name__ == "__main__":

    game_world = world.World("Disc World")
    print(f"Hello, {game_world.name}!")

    bob = entity.Entity(
        race="human",
        gender="male",
        first_name="Bob",
        last_name="the Butcher"
    )
    print(f"Hello, {bob.first_name} ({bob.id})!")

    tim = entity.Entity(
        race="human",
        gender="male",
        first_name="Tim",
        last_name="the Tosser",
        id=27
    )
    print(f"Hello, {tim.first_name} ({tim.id})!")

    first_name, last_name = util.generate_name("female", "elf", last_name=None)
    print(f"Hello, {first_name} {last_name}!")

    for i in range(10):
        ent = entity.generate_entity()
        print(f"{ent.first_name} {ent.last_name} ({ent.id}), {ent.gender}, {ent.race}")

