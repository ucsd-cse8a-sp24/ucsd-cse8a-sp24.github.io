from CSE8AImage import *

def red_filt(img):
    h = height(img)
    w = width(img)
    white = (255, 255, 255)
    res = create_img(h, w, white)
    
    for r in range(height(img)):
        for c in range(width(img)):
            pix = img[r][c]
            new_pix = (pix[0], 0, 0)
            res[r][c] = new_pix
    return res

r = (255, 0, 0)
y = (255, 255, 0)

glob_img = [[r, y, r], [y, r, y]]

red_img = red_filt(glob_img)
