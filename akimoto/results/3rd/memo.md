### 12/31-

!ls akb | wc
!ls saka_pre | wc
4557    4557   50135
5048    5048   55536

### setup
- image_sizeを128に変更
    - より詳細に輪郭見れるかな？
    - いうほど結果は改善せず
- ネットワークを変更
    - [参考(顔識別行ってる記事)](https://towardsdatascience.com/building-face-recognition-model-under-30-minutes-2d1b0ef72fda)
    - Total params: 373,122 -> 2,332,226
    - val_accuracy が全く上がっていかない
        - つまり、、、？

batch_size = 128
epochs = 50

augumentation なし


### log
写真抜粋作業用のscriptを作成した

