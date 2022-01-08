from keras.models import model_from_json
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image


class Gan():
    def __init__(self, n_cols=5, n_rows=5, model_folder="functions/models"):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.img_size = 64
        self.generator = self.create_generator(model_folder)
        self.imgs = self.generate_images(self.generator)

    def create_generator(self, folder):
        json_string = open(f"{folder}/gen_model.json").read()
        generator = model_from_json(json_string)

        # generator.summary()
        generator.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

        generator.load_weights(f"{folder}/gen_weights.hdf5")

        return generator

    # 実行速度を上げたい
    def generate_images(self, generator):

        random_latent_vectors = tf.random.normal(shape = (self.n_cols*self.n_rows, self.img_size*2))
        fake = generator(random_latent_vectors)

        #  生成された画像を並べて一枚の画像にする
        matrix_image = np.zeros((self.img_size*self.n_rows, self.img_size*self.n_cols, 3))
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                # img = keras.preprocessing.image.array_to_img(fake[r*n_rows+c])
                matrix_image[r*self.img_size:(r+1)*self.img_size, c*self.img_size: (c+1)*self.img_size] = fake[r*self.n_rows+c]

        # PILオブジェクトにする
        # 各ピクセル [0, 1]:float32 -> [0, 255]:uint8
        matrix_image = (matrix_image*255.0).astype(np.uint8)
        image = Image.fromarray(matrix_image)
        return image

    def get_images(self):
        return self.imgs
