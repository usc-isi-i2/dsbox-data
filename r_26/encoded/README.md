...Delete *radonFile* column: object/other category.  
...Insert columns to onehot encode *radonFile*.  

```python
from dsbox.datapreprocessing.cleaner import encoder
import pandas as pd

data_path = "dsbox-data/r_26/original/data/"
data_name = data_path + "trainData.csv"


encoded_data = encoder.encode(data_name)

encoded_data.to_csv("dsbox-data/r_26/encoded/trainData_encoded.csv", index=False)
```
