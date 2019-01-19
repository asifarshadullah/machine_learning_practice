#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import pandas

#enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
enron_data = pandas.read_pickle("../final_project/final_project_dataset_unix.pkl")
cnt = 0
total = 0
validSalaryCnt = 0
validEmailCnt = 0
validPaymentCnt = 0
validPoiPaymentCnt = 0
for ob in enron_data:
    total += 1
    if enron_data[ob]["poi"]==1:
        #print(ob," -> ",enron_data[ob])
        if enron_data[ob]["total_payments"]!="NaN":
            validPoiPaymentCnt += 1
        cnt += 1
    if enron_data[ob]["salary"]!='NaN':
        validSalaryCnt += 1
    if enron_data[ob]["email_address"]!="NaN":
        validEmailCnt += 1
    if enron_data[ob]["total_payments"]!="NaN":
        validPaymentCnt += 1

print("Total POI amount =",cnt)
"""
print(len(enron_data))
print(len(enron_data['METTS MARK']))
print("James parentice stock =",enron_data["PRENTICE JAMES"]["total_stock_value"])
print("Wesley Colwell messages to POI =",enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])
print("Jeff Skilling's exercised stock option =",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print("Jeffrey Skilling =",enron_data["SKILLING JEFFREY K"]["total_payments"])
print("Kenneth Lay =",enron_data["LAY KENNETH L"]["total_payments"])
print("Andrew Fastow =",enron_data["FASTOW ANDREW S"]["total_payments"])
"""

print("Valid Salary amount =",validSalaryCnt)
print("Valid Email amount =",validEmailCnt)
print("Total suspect amount =",total)
print("Valid Payment amount =",validPaymentCnt)
print("Valid POI Payment amount =",validPoiPaymentCnt)
