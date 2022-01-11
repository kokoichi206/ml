## memo
2019 brazil traveler to usa need a visa（2019年 アメリカへのブラジル旅行者はビザが必要）

### BERT
- Bidirectional Encoder Representations from Transformers
- BERTはモデルの構造を修正せずとも、様々なタスクに応用できる
- 既存のタスク処理モデルの前に接続（転移学習）するだけで、自然言語処理の精度を向上可能
- げきおも
    - BERTの軽量版ALBERT（A Lite BERT）
- Transformers は PyTorch を前提とする

```
pip3 install torch torchvision
pip install transformers
```

#### Transformer
Transformerは、ニューラルネットワーク・アーキテクチャの一種だ。そして、ニューラルネットとは、画像、動画、音声、テキストなどの複雑なデータを分析するのに非常に有効なモデルである。

こうしたなか2012年頃から、画像の中のオブジェクトを識別したり、顔を認識したり、手書きの数字を読み取ったりするような視覚的問題をCNNで解決することにかなり成功してきた。しかし、（翻訳、テキスト要約、テキスト生成、固有表現抽出（※訳註2）などの）言語的問題については、長い間、CNNの汎用性に匹敵するようなモデルが存在しなかった。言語は人間の主要なコミュニケーション手段であるため、汎用的モデルの不在は残念なことであった。

2017年にTransformerが登場する前は、ディープラーニングを使ってテキストを理解する方法として、リカレントニューラルネットワーク（Recurrent Neural Network：RNN）と呼ばれる、以下のようなタイプのモデルを使っていた。

##### RNN の問題点
- 長いパラグラフやエッセイなどのような大きなテキストの列を扱うのが苦手
- RNNは、段落の最後まで行くと、最初に起こったことを忘れてしまう
- 例えば、RNNベースの翻訳モデルは、長いパラグラフの主語の性別を覚えておこうとすると問題が生じる
- RNNを訓練するのは大変だった。
    - いわゆる「勾配消失問題」の影響を受けやすいこと
    - RNNは単語を順に処理するため、並列化が困難

#### bert, transformer
bert, attention

- BERT っていうモデルの中に、transformer, attention がある。transformer がいろんなところで使える。
- ImageNet を使ってるか、mobileNet を使っているか？

#### AIcia: Transformer

##### Transformer
- どんなタスクにも応用か
    - BERT
        - 将棋のAI？
    - GPT-n
        - ブロガーと同じ文章を書く
    - ViT
    - DALL-E

[Atten is all you need](https://arxiv.org/abs/1706.03762)

RNN を使わずに Attention のみ使用


##### model
目的：機械翻訳
入力：英語
出力：独文の次単語予測
-> BEAM search で独文を出力

Encoder-Decoder モデル GNNT? Google net

Encoder: 文を意味にする
Decoder: 意味を文にする

Multi-Head Attention
FeedForwardNetwork

Embedding -> 単語をいい感じにベクトルにする
単語ではなく、サブアドを使っている

Multi-Head Attention だと、元の位置の情報などが消えてしまう。
Positional Encoding で、何文字目かに応じたベクトルが存在する

DecoderのEmbeddingの方は、１つ前までのドクたんごれつを入力させる

シンプルな構造。CNNとかでは１００回とか繰り返している。ここでは６回

**Transformerの論文では、ベクトルを横ベクトルで表す！**


##### Multi-Head Attention
どの情報に注目すべきか判断して情報を処理する。
距離に関係なく。どんな遠くでも、

Scaled Dot-Product Attention

$$
Attention(Q, K, V) = softmax(QtK/root d)V
$$

Nこののデータのバッチ処理の数式

query: 入力、nこの入力
k: key
v: value

次元の高いベクトルは長いので、ルートdで割って補正する

横方向に対して softmax

k, v の学習が超重要。ここの部分の学習をよしなにやってくれるのが、Multi-Head Attention

類似度を様々な角度で測って・・・


#### memo
- 次に見たい動画
    - CNN
    - Encoder, Decoder
    - BERT


#### memo
GPT-3


#### Bert
高精度で誰でも使える → 大流行
LEGAL BERT

- 高精度
    - Transformer はすごい
    - 双方向（bidirectional）がすごい
- 誰でも使える
    - pre-training & fine-tuning
        - 事前学習と個別タスクの習熟
    - 個別のタスクに習熟
        - fine-tuning
        - 小データ。少数資源で ok
        - 1000件、2000件のオーダーで行けるようになった
        - 統計的言語処理？
- model
    - Transformer の Encoder
    - 文章を２つ入力する
        - 問題文と正解ぶん、などのタスクに対応するため
            - token, subad,
        - CLS t1,,tN SEP t1',,,tM' SEP
            - Classifier
    - segment embedding
    - 出力：ベクトルがたくさん
- pre-training
    - 言語の基礎理解を目指す
    - Masked Language Model (Cloze Test)
        - 入力の 15% をマスクし、その単語を予測する
        - **文法、単語意味を get**
    - Next Sentence Prediction
        - BERTへの入力を、50%は連続する2文、50%はランダムにつなげた2文として
            - どっちだったかを予測
            - CLS由来のベクトルCを用いて予測
        - **文意、文脈を get**
- 使い方
    - BERT: 文を入れると大量のベクトルを出す
    - 文章単位のタスク（分類など）
        - CLS 文 SEP SEP
        - C T1 ... TN TSEP TSEP
        - C を使ってタスクを解く
        - 文章の意味をベクトル
    - 単語単位のタスク（NER: 固有表現抽出）
        - CLS 文 SEP SEP
        - C T1 ... TN TSEP TSEP
        - T1 ... TN を使う
        - 単語の意味をベクトル
- GPT は Decoder 部分を使う


#### Encoder Decoder
- Encoder: 入力を意味ベクトルへ
    - GRUを利用
- Decoder:
    - Begin Of Sentence
    - BEAM search

##### GNMT
Google翻訳、Google's Neural Machine Translation, 2016
SMT, PBMT, NMT
統計的、フレーズベース、ニューラル

- NMT の欠点を改善
    - 推論遅い
    - 未知言語に弱い
        - subword
    - 薬師もれ
        - coverage penalty
    - BLEU スコア！
- model
    - 8層のLSTMのEncoder-Decoder
    - +Attention+Residual Connection

##### Attention
- Attention: Transformer の元ネタ
    - BERT
    - GPT-3
    - ViT
- Attention: 2014
    - AlexNet, word2vec
    - 当時：統計的機械翻訳
- NN: Encoder-Decoder
    - 入力の文章をベクトルに変化して、ベクトル出力文にする
    - Encoder-Decoderの限界
        - ベクトルの次元がどんな文章を入れても固定である点
        - ベクトルが固定次元なので長文がくると意味が入りきらない
    - cf: 画像処理では、縦横が同じなので、めっちゃ上手くいった
- 訳文には元となる単語たちがある
    - これを利用するのがAttention!
- Atteinton:
    - 固定次元の意味ベクトル
    - **入力単語への参照！**

##### Attention(RNN search)
- Encoder
    - 固定次元の意味ベクトルではなく、文脈を加味した意味ベクトルを使う
    - BiGRU
    - 前後の文脈を意味した単語ベクトル
        - Annotation

#### GPT
- Generative Pre-trained Transformer
- Transformer の亜種
- GPTがやったこと
    - 多様なタスクを１つのモデルで解いた！
    - NLI, etc
- その後の発展
    - GPT-2, GPT-3, ...
    - モデル大 → ちょーすごい！
- Pre-training & Fine-tuning
    - ラベル付きデータを作るのは大変
    - ラベルなしデータから大量生産できるサブタスクを学習
    - 次の単語予測を大規模データで学習
- Fine-tuning in GPT
    - 最終層のみ取り替えて、教師データを用いて普通に学習する
    - 3 epoch くらいで ok
- model
    - Transformer の decoder の改変
    - encoding, embedding
        - embedding は学習させるパラメーターの方
    - MASKED Multi-Head Attention

#### GPT-2
- Language Models are Unsupervised Multitask Learners
- GPT, BERT「Fine-tuning なら少量でOK」
    - それすらめんどくさい
    - -> GPT-2
- 言語モデルの可能性
    - 次単語予測器
    - Commonsense Reasoning
    - 大データ、大モデルならもっとすごい！
- model & data
    - model: ほとんど GPT
        - 15億のパラメータ
    - data: Web Text という dataset を作った
    - データは超重要
    - 質量幅が大事
    - 質の高いものを集めるのが大事よね。。。
    - Reddit の link 月投稿で 3karma 以上
        - 800万リンク
        - 40GB
- 性能
    - Language Model
    - Children's Book Test
    - Winoward Ssschema Challenge
    - Common Sense Reasoning
        - The trophy doesn't fit to the suitcase beceuse it is too big.

#### GPT-3
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- OpenAI の人々
- 時代背景
    - Scaling Law
        - 大きい Transformaer は強い
    - NLP * DL の流れ
- model
    - GPT-2 + Sparse Transformer
    - 1750 億のパラメータ
    - n_layers = 96
    - BatchSize = 3.2M
    - lr = 6e-4
- data
    - Common Crawl (を cleaning)
    - WebText2
    - Books1
    - Books2
    - wikipedia
    - 300B tokens を用いて学習
- Few Shot, 1S, 0X
    - 自然言語でタスクと例を与え、続きの生成結果を出力する
    - 例の数が、Few, One, Zero nい関係する
- 背景の思想
    - In Context Learning
    - 超巨大データ
    - 様々なスキルに関するデータがあり、うまく学習している
    - そのため、各タスクが解ける
- 性能
    - Translation は良い
    - 比較は苦手 (Super GLUE WiC)
    - Arithmetic
    - News Article Generation

### t5
- Text-to-Text Transfer Transformer
- [Github](https://github.com/sonoisa/t5-japanese)
- [文字列の正規化処理](https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja)
- [t5 hugging face](https://www.subcul-science.com/post/20210701t5/)
- [pytorch lightning](https://github.com/PyTorchLightning/pytorch-lightning)
    - 機械学習の典型的な処理を簡潔に書くことができるフレームワーク


### tf-idf
- tf-idfとは、tfという概念とidfという概念を組み合わせたもの
- レアな単語が何回も出てくるようなら、文書を分類する際にその単語の重要度を上げる
- tf: Term Frequency
    - 各文書においてその単語がどのくらい出現したのか」を意味します。 （
    - よく出現する単語は、その文書の特徴を判別するのに有用！
- idfInverse Document Frequency
    - 「レア」なら高い値を、「色々な文書によく出現する単語」なら低い値を示す
    - レアな単語は、その文書の特徴を判別するのに有用！


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
