from CSE8AImage import *

# Version #1
##def checker_pattern(img, start_row, start_col, length):
##    end_row = start_row + length
##    end_col = start_col + length
##
##    for r in range(start_row, end_row):
##        for c in range(start_col, end_col):
##            img[r][c] = (255, 255, 255)
##    return img

# Version #2
def checker_pattern(img, start_row, start_col, length):
    if start_row >= height(img) or start_col > width(img) or start_row < 0 or start_col < 0:
        print("Start row/col values are invalid!")
        return None

    if start_row + length > height(img):
        end_row = height(img)
    else:
        end_row = start_row + length

    if start_col + length > width(img):
        end_col = width(img)
    else:
        end_col = start_col + length

    mid_row = start_row + (end_row - start_row) / 2
    mid_col = start_col + (end_col - start_col) / 2

    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            pix = img[r][c]
            
            #Color the top-left and bottom-right quadrants as red
            if (r < mid_row and c < mid_col) or (r >= mid_row and c >= mid_col):
                img[r][c] = (pix[0], 0, 0)
            else:
                img[r][c] = (0, pix[1], 0)
                
    return img


img = load_img("cat.jpg")
print("height = " + str(height(img)))
print("width = " + str(width(img)))
checker_pattern(img, 0, 0, max(height(img), width(img)))
save_img(img, "output.jpg")


