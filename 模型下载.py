
from transformers import AutoTokenizer, AutoModelForMaskedLM

model_name = "bert-base-Chinese"

tokenizer = AutoTokenizer.from_pretrained(model_name, mirror="tuna")
model = AutoModelForMaskedLM.from_pretrained(model_name, mirror="tuna")
print(tokenizer)

inputs=tokenizer("我喜欢你")
print(inputs)

