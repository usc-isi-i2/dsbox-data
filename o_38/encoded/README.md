...Delete *sex* column: object/other category.  
...Insert columns to onehot encode *sex*.  
...Delete *on_thyroxine* column: object/other category.  
...Insert columns to onehot encode *on_thyroxine*.  
...Delete *query_on_thyroxine* column: object/other category.  
...Insert columns to onehot encode *query_on_thyroxine*.  
...Delete *on_antithyroid_medication* column: object/other category.  
...Insert columns to onehot encode *on_antithyroid_medication*.  
...Delete *sick* column: object/other category.  
...Insert columns to onehot encode *sick*.  
...Delete *pregnant* column: object/other category.  
...Insert columns to onehot encode *pregnant*.  
...Delete *thyroid_surgery* column: object/other category.  
...Insert columns to onehot encode *thyroid_surgery*.  
...Delete *I131_treatment* column: object/other category.  
...Insert columns to onehot encode *I131_treatment*.  
...Delete *query_hypothyroid* column: object/other category.  
...Insert columns to onehot encode *query_hypothyroid*.  
...Delete *query_hyperthyroid* column: object/other category.  
...Insert columns to onehot encode *query_hyperthyroid*.  
...Delete *lithium* column: object/other category.  
...Insert columns to onehot encode *lithium*.  
...Delete *goitre* column: object/other category.  
...Insert columns to onehot encode *goitre*.  
...Delete *tumor* column: object/other category.  
...Insert columns to onehot encode *tumor*.  
...Delete *hypopituitary* column: object/other category.  
...Insert columns to onehot encode *hypopituitary*.  
...Delete *psych* column: object/other category.  
...Insert columns to onehot encode *psych*.  
...Delete *TSH_measured* column: object/other category.  
...Insert columns to onehot encode *TSH_measured*.  
...Delete *T3_measured* column: object/other category.  
...Insert columns to onehot encode *T3_measured*.  
...Delete *TT4_measured* column: object/other category.  
...Insert columns to onehot encode *TT4_measured*.  
...Delete *T4U_measured* column: object/other category.  
...Insert columns to onehot encode *T4U_measured*.  
...Delete *FTI_measured* column: object/other category.  
...Insert columns to onehot encode *FTI_measured*.  
...Delete *TBG_measured* column: object/other category.  
...Insert columns to onehot encode *TBG_measured*.  
...Delete *TBG* column: empty column.  
...Delete *referral_source* column: object/other category.  
...Insert columns to onehot encode *referral_source*.  

```python
from dsbox.datapreprocessing.cleaner import encoder
import pandas as pd

data_path = "dsbox-data/o_38/original/data/"
data_name = data_path + "trainData.csv"
label_name = data_path + "trainTargets.csv"

encoded_data = encoder.encode(data_name)
encoded_label = encoder.encode(label_name,label='Class')

encoded_data.to_csv("dsbox-data/o_38/encoded/trainData_encoded.csv", index=False)
encoded_label.to_csv("dsbox-data/o_38/encoded/trainTargets_encoded.csv", index=False)
```
