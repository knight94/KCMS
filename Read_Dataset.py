# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:11:45 2017

@author: ija5kor
"""
## reading the data from csv

import csv
import numpy as np

############################################### Reading the csv data ###################################

# Output is a dictionary

# By default loading the training data
def read_csv_data():
    
    temp_list = list()
    temp1 = list()
    temp2 = list()
    temp3 = list()
        
    with open('./KitCat_Dataset.csv','r') as csvfile:
        train_labels = csv.reader(csvfile, delimiter=',')
        for row in train_labels:
            temp_list.append(row)
    
    sensor_data_without_label = temp_list[1:len(temp_list)]
    
    for t in sensor_data_without_label:
        if(t[0]==''):
            temp2.append(t[9])
            temp1.append([float(i) for i in t[10:]])
        else:
            temp2.append(t[0])              
            temp1.append([float(i) for i in t[1:8]])    
    sensor_data = np.zeros((len(temp1), len(temp1[0])+1))
    temp3 = np.array([int(i == '192.168.43.159') for i in temp2])
    sensor_data[:,1:] = np.array(temp1)
    sensor_data[:,0] = temp3
# 1 is for ip - 192.168.43.159 and 0 for ip 192.168.43.70
    return sensor_data

sensor_data = read_csv_data()
