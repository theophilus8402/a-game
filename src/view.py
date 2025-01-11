

def get_view_ranges(radius_x, radius_y, center_coord):
    cx, cy = center_coord
    top_x = cx - radius_x
    top_y = cy + radius_y
    range_x = list(range(top_x, top_x + 2*radius_x+1))
    range_y = list(range(top_y, top_y - (2*radius_y+1), -1))
    return range_x, range_y


def get_symbol(game_map, coord, empty_symbol):
    ent = game_map.entities.get(coord)
    if ent:
        return ent.symbol
    else:
        return empty_symbol


def gather_map_material(game_map, radius_x, radius_y, center_coord, empty_symbol="."):
    range_x, range_y = get_view_ranges(radius_x, radius_y, center_coord)

    material = []
    for y in range_y:
        row = []
        for x in range_x:
            row.append(get_symbol(game_map, (x, y), empty_symbol))
        material.append(row)
    return material
            

def display_map(game_map, radius_x, radius_y, center_coord):
    material = gather_map_material(game_map, radius_x, radius_y, center_coord)
    for row in material:
        print("".join(row))
