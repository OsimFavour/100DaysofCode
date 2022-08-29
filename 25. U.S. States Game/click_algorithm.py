"""an algorithm that shows us the coordinate in an image by
	just clicking on the image"""

import turtle


def get_mouse_click_coor(x, y):
	print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()  # an alternative to keep our screen open
