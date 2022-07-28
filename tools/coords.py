# this part of Emotions project
# github.com/justxd22
#
# this file is used to generate pixel
# coordinates off the feelings circle
# that later is used to paste highlights
#
# this was designed to run on linux
# on mouse click it copies coordinates
# to clipboard so it uses xclip
# modfiy it to meet your needs
#
# matplotlip and pillow libaries are required

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os 

def mouse_move(event):
    x, y = event.xdata, event.ydata 
    m = f"{round(x,2)}, {round(y,2)}"
    c = f"echo '{m}' | xclip -selection clipboard -r"
    print(m)
    os.system(c)
    
image = "./feel.jpg"
#plt.rcParams['figure.figsize'] = [90,90]
#fig.set_dpi(900)
fig = plt.figure()
fig.patch.set_facecolor('black')
plt.rcParams['figure.facecolor'] = 'black'
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.imshow(Image.open(image))
plt.connect('button_press_event', mouse_move)
plt.show()
