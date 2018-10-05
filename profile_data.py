# This is a sample pipeline file to make a prediction on the image 22_handgeometry_dataset
import sys
import os
import pprint
import json
from d3m.container.dataset import D3MDatasetLoader, Dataset, CSVLoader
from dsbox.datapreprocessing.cleaner.denormalize import Denormalize, DenormalizeHyperparams as hyper_DE
from common_primitives.dataset_to_dataframe import DatasetToDataFramePrimitive, Hyperparams as hyper_DD
from common_primitives.extract_columns_semantic_types import ExtractColumnsBySemanticTypesPrimitive, Hyperparams as hyper_EX

from dsbox.datapreprocessing.cleaner.data_profile import Profiler, Hyperparams as hyper_PR

h1 = hyper_DE.defaults()
h2 =hyper_DD.defaults()
h8 = {'semantic_types': ('https://metadata.datadrivendiscovery.org/types/Attribute',),'use_columns': (), 'exclude_columns': ()}
h6 = {'semantic_types': ('https://metadata.datadrivendiscovery.org/types/Target','https://metadata.datadrivendiscovery.org/types/SuggestedTarget',), 'use_columns': (), 'exclude_columns': ()}

primitive_0 = Denormalize(hyperparams = h1)
primitive_1 = DatasetToDataFramePrimitive(hyperparams = h2)

primitive_3 = ExtractColumnsBySemanticTypesPrimitive(hyperparams = h6)
primitive_4 = ExtractColumnsBySemanticTypesPrimitive(hyperparams = h8)

for dataset in os.listdir(sys.argv[1]):
    if dataset.endswith("dataset"):
        print("==========", dataset)
        dataset_file_path = os.path.join(sys.argv[1], dataset, "datasetDoc.json".format(dataset))
        out_file_path = os.path.join(sys.argv[1], dataset, "profiled_metadata.json")
        dataset = D3MDatasetLoader()
        dataset = dataset.load('file://{dataset_doc_path}'.format(dataset_doc_path=os.path.abspath(dataset_file_path)))

        result0 = primitive_0.produce(inputs = dataset)
        result1 = primitive_1.produce(inputs = result0.value) # this should be the input to this primitive
        result_X = primitive_4.produce(inputs = result1.value)
        result_Y = primitive_3.produce(inputs = result1.value)

        pr = Profiler(hyperparams=hyper_PR.defaults())
        df = pr.produce(inputs=result_X.value).value
        metadata = df.metadata.to_json_structure()

        with open(out_file_path, "w") as f:
            json.dump(metadata, f, indent=2)
