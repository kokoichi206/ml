# 秋元先生グループ識別器

## 概要
写真を入力すると、「AKBぽさ」と「坂道グループぽさ」をパーセンテージで出力する

## 流れ

### Dataset 作成
1. HPから名前一覧を取得する ([code](./get_names.py))
2. Google の画像検索から各メンバー100枚弱クローリングする ([code](./google_img_search.py))
3. 以下の画像については可能な限り削除する
    * 複数人が映り込んでるもの
    * 記事の一部など、顔以外の要素（文字等）が多いもの
    * 顔が写真の極端に端によってるもの

### 前処理
1. 取得した画像に前処理をかける ([code](./resize.py))
    1. 正方形に crop
    2. リサイズ

### 学習
1. akbのグループのフォルダを0,坂道のグループのフォルダを1として正解ラベルを作る
1. バリデーション用に分割する
1. 訓練する ([code](./akimoto.ipynb))

### 予測
1. 予想する ([code](./akimoto_predict.ipynb))


## 説明
- tensorflow
    - [dropout + data augmentation](akimoto_v1.ipynb)
- [pytorch(resnet50)](results/7th/resnet50.ipynb)
