# this part of Emoutions project
# github.com/justxd22
#
# this file is used to generate small 25x25
# circles to be used as highlight


from PIL import Image, ImageDraw

im = Image.new('RGBA', (25, 25), (0, 0, 0,0))
draw = ImageDraw.Draw(im)

color = input("Color? (hex format only) ")
output = input("Output file name (e.g Lightred) ")

draw.ellipse((0, 0, 25, 25), fill=color, outline=(0, 0, 0), width=3)

im.save(output + '.png',quality=100)
