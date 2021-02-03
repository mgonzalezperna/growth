extends TextureButton

export var type = ""

func _pressed():
    $"/root/Game".selected = type
