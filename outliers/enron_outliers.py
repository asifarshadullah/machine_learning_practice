#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
features = ["salary", "bonus"]
#print(data_dict)
#print('********************')
cnt = 0
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)
for point in data:
    print(point," cnt - ",cnt)
    cnt+=1
#print(data)
#print(len(data))
### your code below
data = np.reshape(np.array(data),(len(data),2))
#print(data)

cnt = 0
for point in data:
    salary = point[0]
    bonus = point[1]
    cnt+=1
    if (salary>10000000) and (bonus>50000000):
        print("****************************salary - ",salary," bonus - ",bonus," cnt - ",cnt)
    plt.scatter(salary, bonus)
    print("salary - ",salary," bonus - ",bonus," cnt - ",cnt)

print(cnt)
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
