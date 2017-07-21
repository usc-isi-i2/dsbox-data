...Convert *text_fileName* column from text to integer codes.
...Delete *text_language* column: object/other category.
...Insert columns to onehot encode *text_language*.
...Delete *author_gender* column: object/other category.
...Insert columns to onehot encode *author_gender*.
...Delete *author_language* column: object/other category.
...Insert columns to onehot encode *author_language*.
...Delete *author_region* column: object/other category.
...Insert columns to onehot encode *author_region*.

```python
from dsbox.datapreprocessing.cleaner import encoder
import pandas as pd

data_path = "dsbox-data/r_30/original/data/"
data_name = data_path + "trainData.csv"
label_name = data_path + "trainTargets.csv"

encoded_data = encoder.encode(data_name)
encoded_label = encoder.encode(label_name,label='personality')

encoded_data.to_csv("dsbox-data/r_30/encoded/trainData_encoded.csv", index=False)
encoded_label.to_csv("dsbox-data/r_30/encoded/trainTargets_encoded.csv", index=False)
```
