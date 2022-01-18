# -*- coding: utf-8 -*-

import cv2
import os
import time

if __name__ == '__main__':

    cap = cv2.VideoCapture('./test.mp4')

    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter('detect_face.mp4',fourcc, fps, (cap_width, cap_height))

    cascade_base_path = "cascade"

    face_cascade = cv2.CascadeClassifier(os.path.join(cascade_base_path, 'haarcascade_frontalface_alt_tree.xml'))
    right_eye_cascade = cv2.CascadeClassifier(os.path.join(cascade_base_path, 'haarcascade_righteye_2splits.xml'))
    left_eye_cascade = cv2.CascadeClassifier(os.path.join(cascade_base_path, 'haarcascade_lefteye_2splits.xml'))

    start = time.time()

    try :
        while True:

            if not cap.isOpened():
                break

            ret, frame = cap.read()

            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 顔検出
            face_points = face_cascade.detectMultiScale(img_gray)

            for (fx,fy,fw,fh) in face_points:
                # print((fx,fy,fw,fh))
                
                # ROI(Region of Interest:対象領域)となる画像を切り出す
                width_center = fx + int(fw * 0.5)
                face_right_gray = img_gray[fy:fy+fh, fx:width_center]
                face_left_gray = img_gray[fy:fy+fh, width_center:fx+fw]
                # 3. 右目と左目の両方が写っているか判定
                right_eye_points = right_eye_cascade.detectMultiScale(face_right_gray)
                left_eye_points = left_eye_cascade.detectMultiScale(face_left_gray)

                if 0 < len(right_eye_points) and 0 < len(left_eye_points):
                    (rx,ry,rw,rh) = right_eye_points[0]
                    (lx,ly,lw,lh) = left_eye_points[0]

                    # 顔と目を囲む
                    cv2.rectangle(frame,(fx+rx,fy+ry),(fx+rx+rw,fy+ry+rh),(0,255,255),2)
                    cv2.rectangle(frame,(width_center+lx,fy+ly),(width_center+lx+lw,fy+ly+lh),(0,0,255),2)
                    cv2.rectangle(frame,(fx,fy),(fx+fw,fy+fh),(0,255,0),2)

            writer.write(frame)
    except cv2.error as e:
        print(e)

    print("処理時間 {} 秒".format(time.time() - start))
    writer.release()
    cap.release()
