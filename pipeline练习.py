'''
from transformers import pipeline##使用预训练最简单的方法是pipeline。transformers提供了现成的接口
classifier= pipeline("sentiment-analysis")##example1:情感分析

results =classifier("I love yoy,but I love myself more")
for result in results:
    print(f"label:{result['label']} ,with score:{round(result['score'],4)}")
'''
