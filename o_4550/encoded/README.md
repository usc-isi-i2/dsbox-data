...Convert *MouseID* column from text to integer codes.  
...Delete *Genotype* column: object/other category.  
...Insert columns to onehot encode *Genotype*.  
...Delete *Treatment* column: object/other category.  
...Insert columns to onehot encode *Treatment*.  
...Delete *Behavior* column: object/other category.  
...Insert columns to onehot encode *Behavior*.  

```python
from dsbox.datapreprocessing.cleaner import encoder
import pandas as pd

data_path = "dsbox-data/o_4550/original/data/"
data_name = data_path + "trainData.csv"
label_name = data_path + "trainTargets.csv"

encoded_data = encoder.encode(data_name)
encoded_label = encoder.encode(label_name,label='class')

encoded_data.to_csv("dsbox-data/o_4550/encoded/trainData_encoded.csv", index=False)
encoded_label.to_csv("dsbox-data/o_4550/encoded/trainTargets_encoded.csv", index=False)
```
