from typing import SupportsBytes
import pandas as pd
from pymongo import MongoClient
import numpy as np
import pprint

# connect to MongoDB
client = MongoClient("mongodb://read-shark:msr2021shark@research.cassee.dev:27017/")
database = client['smartshark_2_1']

pull_request = database.pull_request
pull_request_comment = database.pull_request_comment
pull_request_commit = database.pull_request_commit
pull_request_event = database.pull_request_event
pull_request_review = database.pull_request_review
pull_request_review_comment = database.pull_request_review_comment
pull_request_system = database.pull_request_system

# convert to dataframe in pandas
df_pull_request = pd.DataFrame(list(pull_request.find()))
df_pull_request_comment = pd.DataFrame(list(pull_request_comment.find()))
df_pull_request_commit = pd.DataFrame(list(pull_request_commit.find()))
df_pull_request_event = pd.DataFrame(list(pull_request_event.find()))
df_pull_request_review = pd.DataFrame(list(pull_request_review.find()))
df_pull_request_review_comment = pd.DataFrame(list(pull_request_review_comment.find()))
df_pull_request_system = pd.DataFrame(list(pull_request_system.find()))


result = pd.merge(df_pull_request, df_pull_request_comment, left_on=['_id'], right_on=['pull_request_id'], how='inner')
pprint.pprint(result['pull_request_id'].nunique())


# ex. inner join tables pull_request_comment and pull_request_commit on 'pull_request_id'
# PRs that have commented
#pr_commit_comment = pd.merge(df_pull_request_comment[['pull_request_id','created_at','updated_at']], df_pull_request_commit[['pull_request_id']], on=['pull_request_id'], how='inner')
#pprint.pprint(result[['pull_request_id','created_at','updated_at']])

#pr_event_commit_comment = pd.merge(pr_commit_comment, df_pull_request_event[['created_at','pull_request_id','event_type']], on=['pull_request_id'], how='inner')
#pprint.pprint(pr_event_commit_comment[['pull_request_id','created_at','updated_at','event_type']])
#pprint.pprint(pr_event_commit_comment[['pull_request_id', 'created_at_x', 'event_type' == "closed"]])

