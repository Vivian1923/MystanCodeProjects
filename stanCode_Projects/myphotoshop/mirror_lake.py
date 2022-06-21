"""
File: mirror_lake.py
Name: Vivian
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: the filepath of the image that is going to be flipped
    :return: the image is flipped
    """
    original_mt = SimpleImage(filename)
    reflected_img = SimpleImage.blank(original_mt.width, original_mt.height * 2)
    for x in range(original_mt.width):
        for y in range(original_mt.height):
            original_p = original_mt.get_pixel(x, y)
            reflected_p = reflected_img.get_pixel(x, y)
            reflected_p2 = reflected_img.get_pixel(x, reflected_img.height - 1 - y)
            reflected_p.red = original_p.red
            reflected_p.green = original_p.green
            reflected_p.blue = original_p.blue
            reflected_p2.red = original_p.red
            reflected_p2.green = original_p.green
    return reflected_img


def main():
    """
    User need to make a new image that creates a mirror lake vibe by placing an inverse image of below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect(original_mt)
    reflected.show()



if __name__ == '__main__':
    main()
