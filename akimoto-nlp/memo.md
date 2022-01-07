## memo
2019 brazil traveler to usa need a visa（2019年 アメリカへのブラジル旅行者はビザが必要）

### BERT
- BERTはモデルの構造を修正せずとも、様々なタスクに応用できる
- 既存のタスク処理モデルの前に接続（転移学習）するだけで、自然言語処理の精度を向上可能
- げきおも
    - BERTの軽量版ALBERT（A Lite BERT）
- Transformers は PyTorch を前提とする

```
pip3 install torch torchvision
pip install transformers
```

### 歌詞収集

#### Results
``` sh
ls | xargs -I@ bash -c 'echo @ && cat @ | wc'
櫻坂_lyrics.txt
      53    2429  101273
櫻坂_titles.txt
      53      67    1096
乃木坂_lyrics.txt
     232    7361  342207
日向坂_lyrics.txt
      73    3117  127763
乃木坂_titles.txt
     232     303    5112
日向坂_titles.txt
      73      95    1771
```
