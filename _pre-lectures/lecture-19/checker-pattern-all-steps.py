from CSE8AImage import *

######################
# Step 1: start with a black out of the region, check in text file
def checker_pattern(img, start_row, start_col, length):
    end_row = start_row + length
    end_col = start_col + length
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            img[r][c] = (0, 0, 0)

img = create_img(8,8, (255,255,255))
checker_pattern(img,2,3,4)
img_str_to_file(img, "output.txt")


######################
# Step 2: do checker pattern, check in text file
def checker_pattern(img, start_row, start_col, length):
    end_row = start_row + length
    end_col = start_col + length
    mid_r = start_row + (end_row - start_row)/2
    mid_c = start_col + (end_col - start_col)/2
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            pix = img[r][c]
            if (r < mid_r and c < mid_c) or (r >= mid_r and c >= mid_c):
                new_pix = (pix[0],0,0)
            else:
                new_pix = (0,pix[1],0)
            img[r][c] = new_pix

img = create_img(8,8, (255,255,255))
checker_pattern(img,2,3,4)
img_str_to_file(img, "output.txt")


######################
# Step 3: how big is the cat?

img = load_img("cat.jpg")
print("cat height: " + str(height(img)))
print("cat width: " + str(width(img)))


######################
# Step 4: try checker pattern on cat!

img = load_img("cat.jpg")
checker_pattern(img,100,200,200)
save_img(img, "output.png")


######################
# Step 5: what happens when out of bounds?

img = load_img("cat.jpg")
checker_pattern(img,500,500,1000)
save_img(img, "output.png")


######################
# Step 6: handle out of bounds

def checker_pattern(img, start_row, start_col, length):
    end_row = start_row + length
    if end_row > height(img):
        end_row = height(img)
    end_col = start_col + length
    if end_col > width(img):
        end_col = width(img)
    mid_r = start_row + (end_row - start_row)/2
    mid_c = start_col + (end_col - start_col)/2
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            pix = img[r][c]
            if (r < mid_r and c < mid_c) or (r >= mid_r and c >= mid_c):
                new_pix = (pix[0],0,0)
            else:
                new_pix = (0,pix[1],0)
            img[r][c] = new_pix

img = load_img("cat.jpg")
checker_pattern(img,500,500,1000)
save_img(img, "output.jpg")


########################
# Step 7: draw a 4 colored checker pattern
# Solution to Homework Coding Challenge

def checker_pattern(img, start_row, start_col, length):
    end_row = start_row + length
    if end_row > height(img):
        end_row = height(img)
    end_col = start_col + length
    if end_col > width(img):
        end_col = width(img)
    mid_r = start_row + (end_row - start_row)/2
    mid_c = start_col + (end_col - start_col)/2
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            pix = img[r][c]
            if (r < mid_r and c < mid_c):
                new_pix = (pix[0],0,0)
            elif (r >= mid_r and c < mid_c):
                new_pix = (0,pix[1],0)
            elif (r < mid_r and c >= mid_c):
                new_pix = (0,0,pix[2])
            else:
                new_pix = (pix[0],pix[1],0)
            img[r][c] = new_pix

img = load_img("cat.jpg")
checker_pattern(img,0,0,width(img))
save_img(img, "output.jpg")
            
