import cv2
import glob
import re
import os
import sys

"""
顔を検知し、指定したサイズにリサイズする
"""

class Preprocesser(object):
    def __init__(self, 
        data_dir="/Users/kokoichi/Documents/imgs", save_dir="imgs/pre",
        img_size=64, extentions="png", face_ration=1.2):
        self.data_dir = data_dir
        self.save_dir = save_dir
        self.img_size = img_size
        self.extentions = extentions
        self.ratio = face_ration # 検出した顔から何倍まで切り取るか
        self.files = self.file_paths(dir=self.data_dir)
        self.initialize()

    def file_paths(self, dir):
        if self.extentions == 'png':
            return glob.glob(os.path.join(dir, "*.png"))
        elif self.extentions == 'jpg':
            return glob.glob(os.path.join(dir, "*.jpg"))
        else:
            return

    # 
    def initialize(self):
        if not self.files:
            print(f"NO images found in {self.data_dir}. Please check data_dir.")
            sys.exit(1)
        os.makedirs(self.save_dir, exist_ok=True)
        if glob.glob(self.save_dir):
            print(f"Images found in {self.save_dir}. Please delete or change save_dir.")
            sys.exit(1)

    def main(self):
        cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")

        found = 0
        for idx, path in enumerate(self.files):
            # path の方は、先頭の./を除く
            file_name = "{:04d}".format(idx)

            img = cv2.imread(path)

            # グレースケール変換
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # face detect
            face = cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
            if len(face) > 0:
                found += 1

            img_h, img_w, _ = img.shape
            cnt = 0
            for (x, y, w, h) in face:
                length = min(w, h)
                w, h = length, length

                rt = self.ratio - 1

                # THE顔面の中心から見ると、より頭の方が出っ張ってるので、そこを調整する割合
                top_diff = 3
                bottom_diff = 1

                # スタートとゴール地点を計算
                start_x = round(max(0, x-rt*w/2))
                start_y = round(max(0, y-rt*h*top_diff/(top_diff+bottom_diff)))
                end_x = round(min(img_w, x+w + rt*w/2))
                end_y = round(min(img_h, y+h + rt*h*bottom_diff/(top_diff+bottom_diff)))

                cropped = img[start_y:end_y, start_x:end_x, :]
                save_name = f"{file_name}_{cnt}.jpg"

                resized = cv2.resize(cropped, dsize=(64, 64))

                cv2.imwrite(os.path.join(self.save_dir, save_name), resized)

                cnt += 1

        print(f"Faces could not be detected in {idx-found} images.")

    def crop_squre(self, img):
        h, w, c = img.shape
        x = min(h, w)
        y = x

        top = 0
        bottom = top + y
        left = int((w - x) / 2)
        right = left + x

        img = img[top:bottom, left:right]
        return img


if __name__ == "__main__":
    processer = Preprocesser()
    processer.main()
