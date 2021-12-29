import tensorflow as tf
import tensorflow.keras.layers as layers

IMG_SIZE = 64
inputs = layers.Input((IMG_SIZE,IMG_SIZE,3))
x = layers.Conv2D(IMG_SIZE*2, 3, padding="same")(inputs)
x = layers.BatchNormalization()(x)
x = layers.ReLU()(x)
model = tf.keras.models.Model(inputs, x)
###
model.summary()

### Pooling
inputs = layers.Input((32,32,3))
x = layers.AveragePooling2D(2)(inputs)

model = tf.keras.models.Model(inputs, x)
###
model.summary()

inputs = layers.Input((IMG_SIZE,IMG_SIZE,3))
## １層目
x = layers.Conv2D(IMG_SIZE*2, 3, padding="same")(inputs)
x = layers.BatchNormalization()(x)
x = layers.ReLU()(x)
x = layers.AveragePooling2D(2)(x)
## 2層目
x = layers.Conv2D(IMG_SIZE*2*2, 3, padding="same")(x)
x = layers.BatchNormalization()(x)
x = layers.ReLU()(x)
x = layers.AveragePooling2D(2)(x)
## 3層目
x = layers.Conv2D(IMG_SIZE*2*2*2, 3, padding="same")(x)
x = layers.BatchNormalization()(x)
x = layers.ReLU()(x)

model = tf.keras.models.Model(inputs, x)
###
model.summary()


### Model for cifar-10
inputs = layers.Input((32,32,3))
x = inputs
for ch in [1, 2, 4]:
    for i in range(3):
        x = layers.Conv2D(64*ch, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.ReLU()(x)
    if ch != 4:
        x = layers.AveragePooling2D()(x)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(10, activation="softmax")(x)

model = tf.keras.models.Model(inputs, x)
###
model.summary()
