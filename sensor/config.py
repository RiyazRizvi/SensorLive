from dataclasses import dataclass
import os
import pymongo

@dataclass

class EnviromentVariable:
    mongo_db_url:str= os.getenv("MONGO_DB_URL")

env_var=EnviromentVariable()

mongo_clint=pymongo.MongoClient(env_var.mongo_db_url)