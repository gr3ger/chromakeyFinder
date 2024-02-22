import os

from PIL import Image

colors = set()


def populate_colors():
    print("generating color set")
    for i in range(16777216):
        colors.add('#{0:06x}'.format(i))


if __name__ == '__main__':
    populate_colors()

    files = [f for f in os.listdir("input/")]
    for f in files:
        print("Usable chromakeys: " + str(len(colors)))
        print("Processing " + f)
        with Image.open("input/" + f) as img:
            width, height = img.size
            pixel_map = img.load()
            for x in range(width):
                for y in range(height):
                    # We are ignoring alpha channels
                    r, g, b, *rest = pixel_map[x, y]
                    color = '#%02x%02x%02x' % (r, g, b)
                    colors.discard(color)
    print(sorted(colors))
