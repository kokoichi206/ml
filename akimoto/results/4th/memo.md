### 12/31-
start
!ls akb | wc
!ls saka_pre | wc
4557    4557   50135
5048    5048   55536

- 16:41-17:24 akb 写真削除開始
- 17:33-17:24 saka 写真削除開始
    - 顔が小さいものを削除する
    - マイクが顔まわりにあるものも削除

to
!ls akb | wc
!ls saka_pre | wc
3847    3847   42325
3928    3928   43216


### setup
- image_size: 128
- batch_size = 256
- epochs = 100
- ネットワークを変更
    - [参考(顔識別行ってる記事)](https://towardsdatascience.com/building-face-recognition-model-under-30-minutes-2d1b0ef72fda)
    - Total params: 373,122 -> 2,332,226
    - val_accuracy が全く上がっていかない
        - つまり、、、？

batch_size = 128
epochs = 50

augumentation なし


### log

