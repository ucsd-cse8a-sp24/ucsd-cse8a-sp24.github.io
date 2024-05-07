from CSE8AImage import *

def red_filt(img):
    for r in range(height(img)):
        for c in range(width(img)):
            pix = img[r][c]
            new_pix = (pix[0], 0, 0)
            img[r][c] = new_pix

r = (255, 0, 0)
y = (255, 255, 0)

glob_img = [[r, y, r], [y, r, y]]

red_filt(glob_img)
