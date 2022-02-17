import cv2
import glob
import os


def main():

    # 検出した顔から何倍まで切り取るか
    RATIO = 1.2
    # RATIO = 1.1

    pre_dir = "pre"
    # target_file = './imgs/*/*/*.jpg'
    target_file = './imgs/extras/*/*.png'
    files = glob.glob(target_file)
    # files = glob.glob('./imgs/*.jpg')
    total = len(files)
    print(total)

    cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")

    found = 0
    
    for path in files:
        # path の方は、先頭の./を除く
        new_dir = os.path.join(pre_dir, os.path.dirname(path)[2:])
        file_name = os.path.basename(path)
        file_name = os.path.splitext(os.path.basename(path))[0]
        os.makedirs(new_dir, exist_ok=True)

        img = cv2.imread(path)

        # グレースケール変換
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # face detect
        face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        if len(face) > 0:
            found += 1

        img_h, img_w, _ = img.shape
        cnt = 0
        for (x, y, w, h) in face:
            length = min(w, h)
            w, h = length, length

            rt = RATIO - 1

            # THE顔面の中心から見ると、より頭の方が出っ張ってるので、そこを調整する割合
            top_diff = 3
            bottom_diff = 1

            start_x = round(max(0, x-rt*w/2))
            start_y = round(max(0, y-rt*h*top_diff/(top_diff+bottom_diff)))
            end_x = round(min(img_w, x+w + rt*w/2))
            end_y = round(min(img_h, y+h + rt*h*bottom_diff/(top_diff+bottom_diff)))

            cropped = img[start_y:end_y, start_x:end_x, :]
            save_name = f"{file_name}_{cnt}.jpg"

            resized = cv2.resize(cropped, dsize=(64, 64))

            cv2.imwrite(os.path.join(new_dir, save_name), resized)

            cnt += 1

    print(f"not found pictures {total-found}")


if __name__ == '__main__':
    main()
