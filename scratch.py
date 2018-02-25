

import json
from assignment import *


"""
class BigDic:
    def __init__(self):
        self.__dict = {"Default" : "BigDic"}

    def get_dic(self):
        return self.__dict
"""

# create and convert dictionary
big_dict = Assignment("Testing", "123", "Something", True)
dict_json = json.dumps(big_dict.info())

# open file to save
write_file = open("testfile.json", "w")
json.dump(dict_json, write_file)
write_file.close()

# open file to read
read_file = open("testfile.json", "r")
data = json.load(read_file)
print(data)
print("swag")
