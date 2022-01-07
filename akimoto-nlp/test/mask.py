from transformers import (
    AlbertForMaskedLM, AlbertTokenizerFast
)
import torch


"""
モデル
https://huggingface.co/ken11/albert-base-japanese-v1
"""

tokenizer = AlbertTokenizerFast.from_pretrained("ken11/albert-base-japanese-v1")
model = AlbertForMaskedLM.from_pretrained("ken11/albert-base-japanese-v1")

text = "日本の首都は[MASK]です"
tokenized_text = tokenizer.tokenize(text)
print(tokenized_text)
del tokenized_text[tokenized_text.index(tokenizer.mask_token) + 1]
print(tokenized_text)

input_ids = [tokenizer.cls_token_id]
input_ids.extend(tokenizer.convert_tokens_to_ids(tokenized_text))
input_ids.append(tokenizer.sep_token_id)

inputs = {"input_ids": [input_ids], "token_type_ids": [[0]*len(input_ids)], "attention_mask": [[1]*len(input_ids)]}
batch = {k: torch.tensor(v, dtype=torch.int64) for k, v in inputs.items()}
output = model(**batch)[0]
_, result = output[0, input_ids.index(tokenizer.mask_token_id)].topk(5)

print(tokenizer.convert_ids_to_tokens(result.tolist()))
