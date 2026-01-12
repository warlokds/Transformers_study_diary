'''
##1
from transformers import pipeline##使用预训练最简单的方法是pipeline。transformers提供了现成的接口
classifier= pipeline("sentiment-analysis")##example1:情感分析

results =classifier("I love yoy,but I love myself more")
for result in results:
    print(f"label:{result['label']} ,with score:{round(result['score'],4)}")
'''
##2

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from transformers.modeling_outputs import SequenceClassifierOutput
from torch import nn
### 初始化，加载模型和分词器
model_name="nlptown/bert-base-multilingual-uncased-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier= pipeline('sentiment-analysis',model=model,tokenizer=tokenizer)
input_text= tokenizer("I love yoy,but I love myself more")
print(input_text)


pt_batch =tokenizer(["I love yoy","but I love myself more"],
                    padding=True,
                    truncation=True,
                    max_length=512,
                    return_tensors="pt")
for key, value in pt_batch.items():
    print(f"{key}:{value.numpy().tolist()}")
pt_outputs =model(**pt_batch)
print(pt_outputs)


pt_predictions=nn.Sequential(**pt_batch,labels=torch.tensor([1,0]) )
print(pt_predictions)


