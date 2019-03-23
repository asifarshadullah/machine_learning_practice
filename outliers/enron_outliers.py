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
cnt = 0
for point in data_dict:
    print(point,'  ',data_dict[point],' cnt - ',cnt)
    cnt+=1
#print(data_dict)
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)
#print(data)
#print(len(data))
### your code below
data = np.reshape(np.array(data),(len(data),2))
#print(data)

for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter(salary, bonus)

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
