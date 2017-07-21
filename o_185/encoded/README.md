...Convert *Player* column from text to integer codes.  
...Delete *Position* column: object/other category.  
...Insert columns to onehot encode *Position*.  

```python
from dsbox.datapreprocessing.cleaner import encoder
import pandas as pd

data_path = "dsbox-data/o_185/original/data/"
data_name = data_path + "trainData.csv"

encoded_data = encoder.encode(data_name)

encoded_data.to_csv("dsbox-data/o_185/encoded/trainData_encoded.csv", index=False)

```

