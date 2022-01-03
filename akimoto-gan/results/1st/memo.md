## colab

### 使用されているGPUを表示
```
gpu_info = !nvidia-smi
gpu_info = '\n'.join(gpu_info)
if gpu_info.find('failed') >= 0:
  print('Not connected to a GPU')
else:
  print(gpu_info)
```

### 使用可能なメモリ量
```
from psutil import virtual_memory
ram_gb = virtual_memory().total / 1e9
print('Your runtime has {:.1f} gigabytes of available RAM\n'.format(ram_gb))

if ram_gb < 20:
  print('Not using a high-RAM runtime')
else:
  print('You are using a high-RAM runtime!')
```


## GAN
- [Code Sample (Keras Document)](https://keras.io/examples/generative/dcgan_overriding_train_step/)

### どうしよう
- 2000 step までやったが、途中から改善が見られ無くなってきた
- そもそも枚数少なくて過学習になる？
- 過学習になるとしても、元画像と全く同じのが生成できるまでは進むはず？
  - 1000枚、ゼロベースから、5000epochとかで学習させてたのを見たので、5000までやってみる
  - そのあとは少数で学習を学習させる方法で試したい（2nd）
  - fine tuning or transfer learning?
