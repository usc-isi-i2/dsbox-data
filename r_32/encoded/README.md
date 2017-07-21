...Convert *QuestionFilename* column from text to integer codes.
...Convert *SentenceFilename* column from text to integer codes.

```python
from dsbox.datapreprocessing.cleaner import encoder
import pandas as pd

data_path = "dsbox-data/r_32/original/data/"
data_name = data_path + "trainData.csv"

encoded_data = encoder.encode(data_name)

encoded_data.to_csv("dsbox-data/r_32/encoded/trainData_encoded.csv", index=False)
```
