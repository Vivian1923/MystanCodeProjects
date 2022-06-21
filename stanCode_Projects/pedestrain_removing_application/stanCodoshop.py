"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    for i in range(len(pixels)):
        each_pixel = pixels[i]
        pixel_red = each_pixel.red
        red_sum += pixel_red
        pixel_green = each_pixel.green
        green_sum += pixel_green
        pixel_blue = each_pixel.blue
        blue_sum += pixel_blue
    rgb_lst = [int(red_sum/len(pixels)), int(green_sum/len(pixels)), int(blue_sum/len(pixels))]
    return rgb_lst


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    best_distance = float('inf')
    best = pixels[0]
    average = get_average(pixels)
    for pixel in pixels:
        col_dist = get_pixel_dist(pixel, average[0], average[1], average[2])
        if col_dist < best_distance:
            best_distance = col_dist
            best = pixel
    return best
    # d = {}
    # for i in range(len(pixels)):
    #     each_pixel = pixels[i]
    #     col_dist = get_pixel_dist(each_pixel, get_average(pixels)[0],
    #                               get_average(pixels)[1],  get_average(pixels)[2])
    #     d[col_dist] = each_pixel
    # # for color_distance, best_pixel in sorted(d.items(), key=lambda t: t[0]):
    # #     return best_pixel
    # best_distance = min(d)
    # best = d[best_distance]
    # return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            result_p = result.get_pixel(x, y)
            images_pixels = []
            for i in range(len(images)):
                images_pixels.append(images[i].get_pixel(x, y))
                result_p.red = get_best_pixel(images_pixels).red
                result_p.green = get_best_pixel(images_pixels).green
                result_p.blue = get_best_pixel(images_pixels).blue
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
