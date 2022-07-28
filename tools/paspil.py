from PIL import Image

p = Image.open('feel.jpg')
c = Image.open('lightred.png')
b = Image.open('red.png')


p.paste(c, (801-10, 637-10), c)
p.paste(b, (956-10, 437-10), b)
p.paste(b, (985-10, 486-10), b)
p.paste(b, (995-10, 542-10), b)
p.paste(b, (1010-10, 598-10), b)
p.paste(b, (1015-10, 655-10), b)
p.paste(b, (1012-10, 711-10), b)
p.paste(b, (986-10, 761-10), b)
p.paste(b, (966-10, 814-10), b)
p.paste(b, (1125-10, 298-10), b)
p.save('prototype.jpg', quality=100)
