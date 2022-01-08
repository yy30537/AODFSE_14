from pymongo import MongoClient
import pprint
# connect to MongoDB
client = MongoClient("mongodb://read-shark:msr2021shark@research.cassee.dev:27017/")
db = client['smartshark_2_1']

# example: find and print all failed travis_ci builds
for target in db.travis_build.find({'state': "failed"}):
    pprint.pprint(target)