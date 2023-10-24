def calc_base(length, width):
    return length * width


def calc_pyramid_volume(length, width, height):
    return calc_base(length, width) * height * (1 / 3)


print(calc_pyramid_volume(4.5, 2.1, 3.0))
