#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:08:16 2019

@author: halleh
"""

#import packages sys and pandas
#import os
import sys
import pandas as pd

def pharmacy_counting(input,output):
    print("reading csv file...")
    drugs=pd.read_csv(input, skiprows=1, names=('id', 'Last_Name', 'First_Name','Drug_Name','Drug_Cost')) #load actual file
    del drugs['id'] #delete unused columns to open up memory
    #drugs.info(memory_usage='deep')
    
    #adding a column for unique full names
    print("creating full names...")
    drugs['full_name'] = drugs['First_Name']+'-'+drugs['Last_Name'] 

    #delete unused columns to open up memory
    print("deleting unused columns...")
    del drugs['First_Name']
    del drugs['Last_Name']
    
    #Grouping the data by Drug_name column
    print("gouping...")
    grouper = drugs.groupby('Drug_Name')
    print("calculating total cost...")
    total_costs = grouper.sum()['Drug_Cost']
    print("calculating unique users...")
    unique_names = grouper.nunique()['full_name']
    # print(total_costs)
    # print(unique_names)
    
    print("merge and sort...")
    result = pd.merge(unique_names.to_frame(), total_costs.to_frame(), on='Drug_Name', how='outer').sort_values(['Drug_Cost', 'Drug_Name'], ascending=[False, True])  
    # print(result)

    print("saving...")  
    result=result.reset_index()
    result.columns = ['drug_name','num_prescriber','total_cost']
    result.to_csv(output, index=False)

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    pharmacy_counting(*sys.argv[1:])