...Delete *cylinders* column: integer category.  
...Insert columns to onehot encode *cylinders*.  
...Delete *origin* column: integer category.  
...Insert columns to onehot encode *origin*.  

```python
from dsbox.datapreprocessing.cleaner import encoder
import pandas as pd

data_path = "dsbox-data/o_196/original/data/"
data_name = data_path + "trainData.csv"

encoded_data = encoder.encode(data_name)

encoded_data.to_csv("dsbox-data/o_196/encoded/trainData_encoded.csv", index=False)
```
