import cv2
import glob
import re
import os

"""Resize the images and save them as the preprocessed images

"""

# files = glob.glob('./imgs/*/*.jpg')
files = glob.glob('./imgs/*/*.jpg')
if not os.path.exists("imgs/akb_pre"):
    os.mkdir("imgs/akb_pre")
if not os.path.exists("imgs/saka_pre"):
    os.mkdir("imgs/saka_pre")
print(files[0])

print(len(files))

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

# files = ['./imgs/saka/000002.jpg', './imgs/akb/000067.jpg']

for file in files:
    split = file.split('/')
    split[2] = split[2] + '_pre'
    file_new = '/'.join(split)

    img = cv2.imread(file)
    img = crop_squre(img)

    IMG_SIZE = 128
    img = cv2.resize(img, dsize=(IMG_SIZE, IMG_SIZE))

    cv2.imwrite(file_new, img)

# for file in files:
#     img = cv2.imread(file)
#     img = crop_squre(img)

#     cv2.imwrite(f'{file[:-4]}_cropped{file[-4:]}', img)

#     IMG_SIZE = 64
#     img = cv2.resize(img, dsize=(IMG_SIZE, IMG_SIZE))

#     cv2.imwrite(f'{file[:-4]}_resized{file[-4:]}', img)
#     cv2.imwrite(file, img)
