code:

```python

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import f1_score, make_scorer


from dsbox.datapreprocessing.cleaner import Imputation, encoder

# STEP 1: get data
data_path = "../dsbox-data/o_38/original/data/"
data_name = data_path + "trainData.csv"
label_name = data_path + "trainTargets.csv" # make sure your label target is in the second column of this file

data = encoder.encode(data_name)
label = encoder.encode(label_name,label="Class")["Class"]

data.drop("TBG_measured",axis=1)    # drop because all same value, useless
data.drop("d3mIndex",axis=1)    # drop because all same value, useless

# STEP 2: define your machine learning model and scorer
clf = LogisticRegression()
scorer = make_scorer(f1_score, average="macro") # score will be * -1, if greater_is_better is set to False

# STEP 3: go to use the Imputer !
imputer = Imputation(model=clf, scorer=scorer)
# method: greedy search
# imputer.fit(data, label, strategy="greedy")
# data_clean = imputer.transform(data)
# print imputer.best_imputation

# method: regression
data_clean = imputer.complete(data,spec_strategy="iteratively_regre")
data_clean.to_csv("data_clean.csv", index=False)

```