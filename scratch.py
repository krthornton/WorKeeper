

import json
from assignment import *



class BigDic:
    def __init__(self):
        self.__dict = {"Default" : "BigDic", "Another" : "One"}

    def get_dic(self):
        return self.__dict

def jsonDefault(o):
    return o.__dict__


# create and convert dictionary
stuff = []
big_dict = BigDic()
big_dict2 = BigDic()
stuff.append(big_dict)
stuff.append(big_dict2)
#big_dict = {"name": "Testing", "due": "123",
#            "subject": "Something", "done": True}

# open file to save
write_file = open("testfile.json", "w")
json.dump(stuff, write_file, default = jsonDefault)
write_file.close()

# open file to read
read_file = open("testfile.json", "r")
data = json.load(read_file)
print(data)
