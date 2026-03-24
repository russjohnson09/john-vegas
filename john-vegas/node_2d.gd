extends Node2D


#https://godotengine.org/asset-library/asset/3356
# I'll clip the audio to mp3 using python scripts
func _on_texture_button_pressed() -> void:
	print("pressed")
	
	
	$AudioStreamPlayer.stream = load("res://assets/john_vegas_audio/1.The name's john vegas.mp3")
	
	$AudioStreamPlayer.play()

	pass # Replace with function body.
