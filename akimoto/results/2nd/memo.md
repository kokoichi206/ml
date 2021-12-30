### 12/30-
22:39-24:00 : 坂道の写真、不要部分削除開始
24:00-25:05 : AKBの写真、不要部分削除開始
-25:30 : 学習の準備

!ls akb | wc
!ls saka_pre | wc
4557    4557   50135
5048    5048   55536

### setup
model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

batch_size = 128
epochs = 50

augumentation なし


### log
写真抜粋作業

``` sh
# IMG_SIZE = 64 で 
python resize.py

# 不要にできるかも
cd imgs
zip -r archive akb_pre > /dev/null
mv archive.zip ../akb.zip
zip -r archive saka_pre > /dev/null
mv archive.zip ../saka.zip
cd ..

git add saka.zip akb.zip
git commit -m 'make dataset'
git push
```
