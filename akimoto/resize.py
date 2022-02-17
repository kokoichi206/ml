import cv2
import glob
import re
import os

def resize_imgs(path):
    """
    Resize the images and save them as the preprocessed images
    """
    # Make folders 
    files = glob.glob(path)
    if not os.path.exists("imgs/akb_pre"):
        os.mkdir("imgs/akb_pre")
    if not os.path.exists("imgs/saka_pre"):
        os.mkdir("imgs/saka_pre")

    for file in files:
        split = file.split('/')
        split[2] = split[2] + '_pre'
        file_new = '/'.join(split)

        img = cv2.imread(file)
        img = crop_squre(img)

        IMG_SIZE = 128
        img = cv2.resize(img, dsize=(IMG_SIZE, IMG_SIZE))

        cv2.imwrite(file_new, img)

def crop_squre(img):
    h, w, c = img.shape
    x = w if h > w else h
    y = x

    # top = int((h - y) / 2)
    top = 0
    bottom = top + y
    left = int((w - x) / 2)
    right = left + x

    img = img[top:bottom, left:right]
    return img


if __name__ == "__main__":
    resize_imgs('./imgs/*/*.jpg')
