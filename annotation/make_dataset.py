import cv2
import glob
import json
import os
from pathlib import Path
import shutil


"""
データセットとして公開するために必要な情報の記載と
zipファイルの作成を行うクラス
"""
class Dataset(object):
    def __init__(self, dir, output_dir='data', output_img_dir='img'):
        self.dir = dir
        self.files = self.get_files(dir)
        self.output_dir = output_dir
        self.output_img_dir = os.path.join(output_dir, output_img_dir)
        self.min_shape, self.max_shape \
            = self.get_min_max_img_size(self.files)
        self.setup()

    def setup(self):
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.output_img_dir, exist_ok=True)

    @staticmethod
    def get_files(dir, extention="png"):
        """
        渡されたフォルダ内に含まれる png ファイル名を再帰的に取得する。
        :param dir: 写真が保存されているフォルダ名
        :return: パスのリスト
        """
        # rglob は generator を返す
        if extention == "png":
            files = Path(dir).rglob('*.png')
        elif extention == "jpg":
            files = Path(dir).rglob('*.jpg')
        else:
            files = Path(dir).rglob('*')
        # それを文字列のリストにして返す
        file_list = []
        for f in files:
            file_list.append(str(f))
        return file_list

    @staticmethod
    def get_min_max_img_size(paths):
        """
        渡されたパス内に含まれる png 画像ファイル名の、
        最小サイズと最大サイズの画像サイズを取得する。
        :param paths: 写真が保存されているパスの集まり
        :return: 最小と最大のサイズの２つのタプル
        """
        im = cv2.imread(paths[0])

        min_shape = im.shape
        min_val = min(im.shape[0], im.shape[1])
        max_shape = im.shape
        max_val = max(im.shape[0], im.shape[1])
        for path in paths:
            im = cv2.imread(path)
            x, y = im.shape[0], im.shape[1]
            if x < min_val or y < min_val:
                min_val = min(x, y)
                min_shape = im.shape
            if x > max_val or y > max_val:
                max_val = min(x, y)
                max_shape = im.shape
        print(f"min_val: {min_val}")
        print(f"min_shape: {min_shape}")
        print(f"max_val: {max_val}")
        print(f"max_shape: {max_shape}")
        print(type(max_shape))
        return min_shape, max_shape

    def create_dataset(self):
        """
        データセットを作成する。
        1. データセットの情報を config ファイルに保存
        2. データセットを zip ファイルに圧縮する
        """
        self.write_info()
        self.archive_imgs()

    def write_info(self):
        info = self.get_info()
        file_path = os.path.join(self.output_dir, 'config.json')
        with open(file_path, 'w') as f:
            json.dump(info, f, indent=4)

    def get_info(self):
        info = {}
        info['size'] = len(self.files)
        info['min_img_size'] = f"{self.min_shape}"
        info['max_img_size'] = f"{self.max_shape}"
        return info

    def archive_imgs(self):
        shutil.make_archive(self.output_img_dir, 'zip', self.dir)


if __name__ == '__main__':
    img_dir = '/Users/kokoichi/Documents/imgs'
    dataset = Dataset(img_dir)
    print(dataset.create_dataset())
