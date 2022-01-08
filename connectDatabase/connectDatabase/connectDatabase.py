from typing import SupportsBytes
import pandas as pd
from pymongo import MongoClient
import numpy as np
import pprint



# connect to MongoDB
client = MongoClient("mongodb://read-shark:msr2021shark@research.cassee.dev:27017/")
database = client['smartshark_2_1']

# example: find and print all failed travis_ci builds
#for target in db.travis_build.find({'state': "failed"}):
#    pprint.pprint(target)

# collections = tables 
collection1 = database.travis_build
collection2 = database.commit

query = ""

dataframe1 = pd.DataFrame(list(collection1.find()))
dataframe1.info()



# by column (field)
subset_column = dataframe1[['number', 'tr_id', 'duration']]
pprint.pprint(subset_column)

# by row
subset_row = dataframe1.loc[0]
pprint.pprint(subset_row)

