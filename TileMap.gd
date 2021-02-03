extends TileMap

var types = {
    "water": 1,
    "mountain": 2,
    "grass": 3
}

func _input(event: InputEvent):
    if (Input.is_action_pressed("left_click") && get_parent().selected != ""):
        var touched = world_to_map(event.position)
        var tile = types[get_parent().selected]
        set_cellv(touched, tile)
