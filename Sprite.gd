extends Sprite

var mouse_in = false
var dragging = false
var mouse_to_center


func _input(_event):
    if (Input.is_action_just_pressed("left_click") && mouse_in):
        var mouse_pos = get_viewport().get_mouse_position()
        mouse_to_center = position - mouse_pos
        dragging = true
    if (Input.is_action_just_released("left_click") && dragging):
        var mouse_pos = get_viewport().get_mouse_position()
        dragging = false
        position = (mouse_pos / 64).floor() * 64 + Vector2(32, 32)

func _process(_delta):
    if (dragging):
        var mouse_pos = get_viewport().get_mouse_position()
        position = mouse_pos + mouse_to_center

func _on_Area2D_mouse_entered():
    mouse_in = true

func _on_Area2D_mouse_exited():
    mouse_in = false
