import random
'''import json


with open('data102.jsonl', 'r') as json_file:
    data = list(json_file)

random.shuffle(data)

train_data = data[:50]
test_data = data[50:]

print(data)'''

import jsonlines

data = []
with jsonlines.open('data102.jsonl') as reader:
    for obj in reader:
        data.append(obj)

random.shuffle(data)

data_size = len(data)
train_split = int(data_size  * 0.7)
test_split = int(data_size  * 0.15)

train_data = data[:train_split]
test_data = data[train_split:train_split+test_split]
eval_data = data[train_split+test_split:]

with jsonlines.open('train_data.jsonl', mode='w') as writer:
    for item in train_data:
       writer.write(item)

with jsonlines.open('test_data.jsonl', mode='w') as writer:
    for item in test_data:
       writer.write(item)

with jsonlines.open('eval_data.jsonl', mode='w') as writer:
    for item in eval_data:
       writer.write(item)

with jsonlines.open('data.jsonl', mode='w') as writer:
    for item in data:
       writer.write(item)