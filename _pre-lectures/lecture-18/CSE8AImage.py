import numpy as np
from PIL import Image

def load_img(filename):
    pil_img = Image.open(filename)
    arr = np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)
    img = [ [ (p[0],p[1],p[2]) for p in row ] for row in arr ]
    return img

def save_img(img, filename):
    arr = np.asarray(img, dtype=np.uint8)
    pil_img = Image.fromarray(arr)
    pil_img.save(filename, format='jpeg')

def create_img(height, width, color):
    result = [None] * height
    for i in range(len(result)):
        result[i] = [color] * width
    return result

def height(img):
    return len(img)

def width(img):
    return len(img[0])

def img_str_to_file(img, filename):  
    # Calculating max length 
    max_length = len(str((255.0,255.0,255.0)))

    # Limiting the number of rows and columns to be printed
    r_limit = min(20, height(img))
    c_limit = min(20, width(img))
    
    with open(filename, 'w') as file:
        pix_str = ""
        for y in range(r_limit):
            for x in range(c_limit):
                # Rounding to one decimal place
                temp_str = ("(" + str(round(img[y][x][0], 1))
                           + "," + str(round(img[y][x][1], 1))
                           + "," + str(round(img[y][x][2], 1)) + ")")
                pix_str += temp_str
                # Added appropriate number of spaces to make it visually clear
                pix_str += " " * (max_length-len(temp_str))
            pix_str += "\n"
        file.write(pix_str)

    return pix_str
            
    
    
