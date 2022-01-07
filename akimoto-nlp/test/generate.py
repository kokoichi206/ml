from transformers import T5Tokenizer, AutoModelForCausalLM


"""
LSTM (RNN)では「MeCabは使えねー」 -> sentencepiece

python -m pip install --upgrade pip setuptools
pip install sentencepiece
"""

# 接頭辞（Prefix） 
PREFIX_TEXT = "人工知能を勉強することは、"
# トークナイザーとモデルの準備 
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium") 
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium") 
# 推論 
input = tokenizer.encode(PREFIX_TEXT, return_tensors="pt") 
output = model.generate(input, do_sample=True, max_length=150, num_return_sequences=3) 
print(tokenizer.batch_decode(output))
