code:

```python
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import f1_score, make_scorer,mean_squared_error
from sklearn import tree

from dsbox.datapreprocessing.cleaner import Imputation, helper_func, encoder

# STEP 1: get data
data_path = "../dsbox-data/o_196/original/data/"
data_name = data_path + "trainData.csv"
label_name = data_path + "trainTargets.csv" # make sure your label target is in the second column of this file

data = encoder.encode(data_name)
label = encoder.encode(label_name,label="class")["class"]

data.drop("d3mIndex",axis=1)    # drop because id, useless

# STEP 2: define your machine learning model and scorer
clf = LinearRegression()
scorer = make_scorer(mean_squared_error, greater_is_better=False) # score will be * -1, if greater_is_better is set to False

# STEP 3: go to use the Imputer !
# method: greedy search
imputer = Imputation(model=clf, scorer=scorer, strategy="greedy")
imputer.fit(data, label)
data_clean = imputer.transform(data)
print imputer.best_imputation

# method: regression
# imputer = Imputation(model=clf, scorer=scorer, strategy="iteratively_regre")
# imputer.fit(data)
# data_clean = imputer.transform(data, label)

# match the format with original data (round float imputated value to int)
from dsbox.datapreprocessing.cleaner import helper_func
helper_func.format_match(data,data_clean)

data_clean.to_csv("data_clean.csv", index=False)
```