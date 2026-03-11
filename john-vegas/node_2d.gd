extends Node2D


#https://godotengine.org/asset-library/asset/3356
# I'll clip the audio to mp3 using python scripts
func _on_texture_button_pressed() -> void:
	print("pressed")
	
	$AudioStreamPlayer.play(12.0)
	pass # Replace with function body.
