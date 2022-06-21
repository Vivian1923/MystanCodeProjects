"""
File: fire.py
Name: Vivian
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: the filepath of the image that is going to be changing the pixel
    :return: changed the fire part to pixel.red = 255 and other space to grayscale
    """
    highlighted_fire = SimpleImage(filename)
    for pixel in highlighted_fire:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > (avg*HURDLE_FACTOR):
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return highlighted_fire


def main():
    """
    User need to make the highlight_fires which detects the pixels that are recognized as fire
    and highlights them for better observation.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
