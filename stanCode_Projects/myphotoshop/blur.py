"""
File: blur.py
Name: Vivian
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: smiley-face.png
    :return: smiley-face-blurred.png
    """
    # Todo: create a new blank img that is as big as the orignial one
    new_img = SimpleImage.blank(img.width, img.height)

    # loop over the picture
    for x in range(new_img.width):
        for y in range(new_img.height):

            new_img_p = new_img.get_pixel(x,y)
            
            # Todo: get pixel of new_img at x,y

            # belows are 9 conditions of pixel filling, depending on pixels' x,y orientation. 
            
            if x == 0 and y == 0:
                # get pixel at the top-left corner of the image.
                pixel_self = img.get_pixel(x, y)
                pixel_down = img.get_pixel(x, y + 1)
                pixel_right = img.get_pixel(x + 1, y)
                pixel_rightdown = img.get_pixel(x + 1, y + 1)
                new_img_p.red = (pixel_self.red + pixel_down.red + pixel_right.red + pixel_rightdown.red) / 4
                new_img_p.green = (pixel_self.green + pixel_down.green + pixel_right.green + pixel_rightdown.green) / 4
                new_img_p.blue = (pixel_self.blue + pixel_down.blue + pixel_right.blue + pixel_rightdown.blue) / 4

            elif x == new_img.width-1 and y == 0:
                # get pixel at the top-right corner of the image.
                pixel_self = img.get_pixel(x, y)
                pixel_down = img.get_pixel(x, y + 1)
                pixel_left = img.get_pixel(x - 1, y)
                pixel_leftdown = img.get_pixel(x - 1, y + 1)
                new_img_p.red = (pixel_self.red + pixel_down.red + pixel_left.red + pixel_leftdown.red) / 4
                new_img_p.green = (pixel_self.green + pixel_down.green + pixel_left.green + pixel_leftdown.green) / 4
                new_img_p.blue = (pixel_self.blue + pixel_down.blue + pixel_left.blue + pixel_leftdown.blue) / 4

            elif x == 0 and y == new_img.height-1:
                # get pixel at the bottom-left corner of the image
                pixel_self = img.get_pixel(x, y)
                pixel_up = img.get_pixel(x, y - 1)
                pixel_right = img.get_pixel(x + 1, y)
                pixel_rightup = img.get_pixel(x + 1, y - 1)
                new_img_p.red = (pixel_self.red + pixel_up.red + pixel_right.red + pixel_rightup.red) / 4
                new_img_p.green = (pixel_self.green + pixel_up.green + pixel_right.green + pixel_rightup.green) / 4
                new_img_p.blue = (pixel_self.blue + pixel_up.blue + pixel_right.blue + pixel_rightup.blue) / 4

            elif x == new_img.width-1 and y == new_img.height-1:
                # get pixel at the bottom-right corner of the image
                pixel_self = img.get_pixel(x, y)
                pixel_up = img.get_pixel(x, y - 1)
                pixel_left = img.get_pixel(x - 1, y)
                pixel_leftup = img.get_pixel(x - 1, y - 1)
                new_img_p.red = (pixel_self.red + pixel_up.red + pixel_left.red + pixel_leftup.red) / 4
                new_img_p.green = (pixel_self.green + pixel_up.green + pixel_left.green + pixel_leftup.green) / 4
                new_img_p.blue = (pixel_self.blue + pixel_up.blue + pixel_left.blue + pixel_leftup.blue) / 4
 
            elif y == 0 and ( 0 < x < new_img.width-1):
                # get top edge's pixels (without two corners)
                pixel_self = img.get_pixel(x, y)
                pixel_down = img.get_pixel(x, y + 1)
                pixel_right = img.get_pixel(x + 1, y)
                pixel_left = img.get_pixel(x - 1, y)
                pixel_rightdown = img.get_pixel(x + 1, y + 1)
                pixel_leftdown = img.get_pixel(x - 1, y + 1)
                new_img_p.red = (pixel_self.red + pixel_down.red + pixel_left.red + pixel_leftdown.red
                                 + pixel_right.red + pixel_rightdown.red) / 6
                new_img_p.green = (pixel_self.green + pixel_down.green + pixel_left.green + pixel_leftdown.green
                                   + pixel_right.green + pixel_rightdown.green) / 6
                new_img_p.blue = (pixel_self.blue + pixel_down.blue + pixel_left.blue + pixel_leftdown.blue
                                  + pixel_right.blue + pixel_rightdown.blue) / 6

            elif y == new_img.height-1 and (0 < x < new_img.width-1):
                # get bottom edge's pixels (without two corners)
                pixel_self = img.get_pixel(x, y)
                pixel_up = img.get_pixel(x, y - 1)
                pixel_right = img.get_pixel(x + 1, y)
                pixel_left = img.get_pixel(x - 1, y)
                pixel_rightup = img.get_pixel(x + 1, y - 1)
                pixel_leftup = img.get_pixel(x - 1, y - 1)
                new_img_p.red = (pixel_self.red + pixel_up.red + pixel_left.red + pixel_leftup.red
                                 + pixel_right.red + pixel_rightup.red) / 6
                new_img_p.green = (pixel_self.green + pixel_up.green + pixel_left.green + pixel_leftup.green
                                   + pixel_right.green + pixel_rightup.green) / 6
                new_img_p.blue = (pixel_self.blue + pixel_up.blue + pixel_left.blue + pixel_leftup.blue
                                  + pixel_right.blue + pixel_rightup.blue) / 6

            elif x == 0 and ( 0 < y < new_img.height-1):
                # get left edge's pixels (without two corners)
                pixel_self = img.get_pixel(x, y)
                pixel_down = img.get_pixel(x, y + 1)
                pixel_up = img.get_pixel(x, y - 1)
                pixel_right = img.get_pixel(x + 1, y)
                pixel_rightup = img.get_pixel(x + 1, y - 1)
                pixel_rightdown = img.get_pixel(x + 1, y + 1)
                new_img_p.red = (pixel_self.red + pixel_up.red + pixel_down.red + pixel_rightup.red
                                 + pixel_right.red + pixel_rightdown.red) / 6
                new_img_p.green = (pixel_self.green + pixel_up.green + pixel_down.green + pixel_rightup.green
                                   + pixel_right.green + pixel_rightdown.green) / 6
                new_img_p.blue = (pixel_self.blue + pixel_up.blue + pixel_down.blue + pixel_rightup.blue
                                  + pixel_right.blue + pixel_rightdown.blue) / 6

            elif x == new_img.width-1 and ( 0 < y < new_img.height-1):
                #  get right edge's pixels (without two corners)
                pixel_self = img.get_pixel(x, y)
                pixel_down = img.get_pixel(x, y + 1)
                pixel_up = img.get_pixel(x, y - 1)
                pixel_left = img.get_pixel(x - 1, y)
                pixel_leftup = img.get_pixel(x - 1, y - 1)
                pixel_leftdown = img.get_pixel(x - 1, y + 1)
                new_img_p.red = (pixel_self.red + pixel_up.red + pixel_down.red + pixel_leftup.red
                                 + pixel_left.red + pixel_leftdown.red) / 6
                new_img_p.green = (pixel_self.green + pixel_up.green + pixel_down.green + pixel_leftup.green
                                   + pixel_left.green + pixel_leftdown.green) / 6
                new_img_p.blue = (pixel_self.blue + pixel_up.blue + pixel_down.blue + pixel_leftup.blue
                                  + pixel_left.blue + pixel_leftdown.blue) / 6

            else:
                # Inner pixels.
                pixel_self = img.get_pixel(x, y)
                pixel_down = img.get_pixel(x, y + 1)
                pixel_up = img.get_pixel(x, y - 1)
                pixel_right = img.get_pixel(x + 1, y)
                pixel_left = img.get_pixel(x - 1, y)
                pixel_rightup = img.get_pixel(x + 1, y - 1)
                pixel_leftup = img.get_pixel(x - 1, y - 1)
                pixel_rightdown = img.get_pixel(x + 1, y + 1)
                pixel_leftdown = img.get_pixel(x - 1, y + 1)
                new_img_p.red = (pixel_self.red + pixel_up.red + pixel_down.red + pixel_leftup.red
                                 + pixel_left.red + pixel_leftdown.red + pixel_rightup.red
                                 + pixel_right.red + pixel_rightdown.red) / 9
                new_img_p.green = (pixel_self.green + pixel_up.green + pixel_down.green + pixel_leftup.green
                                   + pixel_left.green + pixel_leftdown.green + pixel_rightup.green
                                   + pixel_right.green + pixel_rightdown.green) / 9
                new_img_p.blue = (pixel_self.blue + pixel_up.blue + pixel_down.blue + pixel_leftup.blue
                                  + pixel_left.blue + pixel_leftdown.blue + pixel_rightup.blue
                                  + pixel_right.blue + pixel_rightdown.blue) / 9

    return new_img


def main():
    """
    User will make the smiley-face image blurred.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
