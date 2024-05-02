#import CSE8AImage
from CSE8AImage import *

star_img = load_img("star.png")
img_str_to_file(star_img, "star_readable.txt")

print("height = "+ str(height(star_img)))
print("width = "+ str(width(star_img)))
