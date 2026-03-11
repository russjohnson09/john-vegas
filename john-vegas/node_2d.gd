extends Node2D


func _on_texture_button_pressed() -> void:
	print("pressed")
	
	$AudioStreamPlayer.play()
	pass # Replace with function body.
