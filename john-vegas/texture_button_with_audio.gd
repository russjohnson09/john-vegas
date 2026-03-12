extends TextureButton


#https://docs.godotengine.org/en/4.4/getting_started/step_by_step/nodes_and_scenes.html
#@onready var sprite2d = get_node("Sprite2D")


#https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html#custom-signals

#https://docs.godotengine.org/en/stable/getting_started/introduction/introduction_to_godot.html#programming-languages

#https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_languages.html

@export var stream = preload("res://assets/john_vegas_audio/1. The name's john vegas.mp3")


func _on_pressed() -> void:
	$AudioStreamPlayer.stream = stream
	$AudioStreamPlayer.play()
	pass # Replace with function body.
