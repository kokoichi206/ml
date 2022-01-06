### 1/5-19:20-
- 各メンバー 200 枚に増やして取得し直し
    - 53001 枚
- **顔周辺のみを crop してからリサイズするようにした！** ([Code](../../detect_face.py))
    - 枚数が減るのと、余計なものが結構入るので、どうなるか微妙
- 間違って crop してしまったものを削除,
    - 1/5-22:20-
    - crop_start: crop_end
    - 162: 73
    - 160: 80
    - 156: 79
    - 161: 85
    - 150: 75
    - 147: 64
    - 151: 97
    - 161: 84
    - 154: 83
    - 165: 109
        - 10 人. 22:46
        - 26 min
    - 164: 63
    - 83 項目終了！
        - 25:26, 3時間
- 削除続き,坂道
    - 1/6-20:14-26:54

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

