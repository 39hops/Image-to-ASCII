import sys
import cv2
import numpy as np


symbols = [".", "-", "+", "*", "*", "o"]
thresholds = [0, 50, 100, 150, 200]

def print_symbols(array):
    symbols_length = len(symbols)
    for i in array:
        for j in i:
            print(symbols[j % symbols_length], end="")
        print("")
        
        
        
def ascii(img):
    
    height, width = img.shape
    n_height = height // 6
    n_width = width // 3
    
    resized_image = cv2.resize(img, (n_width, n_height))
    
    threshold_img = np.zeros(resized_image.shape)
    
    for i, threshold in enumerate(thresholds):
        threshold_img[resized_image > threshold] = i
        
    return threshold_img.astype(int)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(sys.argv)
        path = sys.argv[1];
    else:
        path ='./assets/image.png'
    
    
    img = cv2.imread(path, 0)
    ascii_art = ascii(img)
    print_symbols(ascii_art)