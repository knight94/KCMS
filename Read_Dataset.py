# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 11:42:05 2017

@author: ija5kor
"""

## reading the data from csv

import csv
import numpy as np

############################################### Reading the csv data ###################################

# Output is a dictionary

# By default loading the training data
def read_csv_data(data_type='train'):
    
    temp_list = list()
    temp1 = list()
    temp2 = list()    
        
    with open('./KitCat_Dataset.csv','r') as csvfile:
        train_labels = csv.reader(csvfile, delimiter=',')
        for row in train_labels:
            temp_list.append(row)
