'''
FRAME CALCULATOR

This calculates the length and width of planks of wood
required for making picture frames based on the canvas size.
'''


def varCatcher(dimension, item):
    valid = False
    while valid is not True:
        try:
            intValue = input(f"What is the {dimension} of the {item} (in mm)?")
            intValue = int(intValue)
            valid = True
        except ValueError:
            print("Please enter an integer")
    return intValue


height_canvas_value = varCatcher("height", "canvas")
width_canvas_value = varCatcher("width", "canvas")
width_woodplank_value = varCatcher("width", "wood_plank")

plank1_length = width_canvas_value
plank2_length = height_canvas_value - (2 * width_woodplank_value)

print(f"This needs 2 planks of {plank1_length}mm length, and 2 planks of {plank2_length}mm.")
