### 12/30-21:00
!ls akb | wc
!ls saka_pre | wc
6065    6065   66723
6481    6481   71299

### setup
model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

batch_size = 128
epochs = 50

from keras.preprocessing.image import ImageDataGenerator
generator = ImageDataGenerator(
           rotation_range=0.2,
           width_shift_range=0.2,
           height_shift_range=0.2,
           shear_range=1,
           zoom_range=0.2,
           horizontal_flip=False)
generator.fit(X_train)