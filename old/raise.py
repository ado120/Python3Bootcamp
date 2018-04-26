def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "magenta")
	if type(text) is not str:
		raise TypeError("Text Must Be a Str")
	if color not in colors:
		raise ValueError("Color is invalid color")
	print(f"Printed {text} in {color}")

colorize("hello", "red")