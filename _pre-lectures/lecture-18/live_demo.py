from CSE8AImage import *

print("loading image...")
santa_img = load_img("santa.png")

#img_str_to_file(santa_img, "santa_readable.txt")

print("saving image...")
save_img(santa_img, "santa_new.png")

