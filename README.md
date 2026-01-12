# Transformer学习日记
## 第一天

### 1.pipeline结果

```python
No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f (https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
C:\Users\lenovo\PycharmProjects\PythonProject\.venv\Lib\site-packages\huggingface_hub\file_download.py:143: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in C:\Users\lenovo\.cache\huggingface\hub\models--distilbert--distilbert-base-uncased-finetuned-sst-2-english. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development ###以上的都是正常的警告
  warnings.warn(message)
Device set to use cpu
label:POSITIVE ,with score:0.9996
###第一段（已注释部分1）

### 第二段结果
{'input_ids': [101, 151, 11157, 13195, 10158, 117, 10502, 151, 11157, 51875, 10772, 102], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
input_ids:[[101, 151, 11157, 13195, 10158, 102, 0], [101, 10502, 151, 11157, 51875, 10772, 102]]
token_type_ids:[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
attention_mask:[[1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1]]
SequenceClassifierOutput(loss=None, logits=tensor([[-1.8475, -1.8961, -0.4648,  1.0456,  2.5861],
        [-1.7631, -1.0044,  0.4824,  0.9380,  1.0541]],
       grad_fn=<AddmmBackward0>), hidden_states=None, attentions=None)

```

#### tips:（1）logits是什么？

