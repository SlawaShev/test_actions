#!/usr/bin/python3

dict1 = {"aa": "bb", "cc": "dd"}
dict2 = {"ee": "ff"}

dict1.update(dict2)
dict3 = dict1

print(dict3)
print(dict3["aa"])
print(dict3["cc"])
print(dict3["ee"])
print(dict3["ee"])
