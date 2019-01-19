#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn import neighbors
from time import time
from sklearn import ensemble

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
"""
clf = neighbors.KNeighborsClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print("K-nearest Training time :",round(time()-t0, 3),"s")
t1 = time()
clf.predict(features_test)
print("K-nearest Prediction time :",round(time() - t1,3),"s")

accuracy = clf.score(features_test, labels_test)

print("K nearest neighbors accuracy",accuracy)
"""

"""
clf = ensemble.AdaBoostClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print("Adaboost Training time :",round(time()-t0, 3),"s")
t1 = time()
clf.predict(features_test)
print("Adaboost Prediction time :",round(time() - t1,3),"s")

accuracy = clf.score(features_test, labels_test)

print("Adaboost accuracy",accuracy)



clf = ensemble.RandomForestClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print("Random Forest Training time :",round(time()-t0, 3),"s")
t1 = time()
clf.predict(features_test)
print("Random Forest Prediction time :",round(time() - t1,3),"s")

accuracy = clf.score(features_test, labels_test)

print("Random Forest Accuracy",accuracy)
"""


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
