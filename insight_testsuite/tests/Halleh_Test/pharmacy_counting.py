#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:08:16 2019

@author: halleh
"""


#import os
import sys
import pandas as pd

def pharmacy_counting(input,output):
    #path=os.getcwd()
    #drugs=pd.read_table(path+'/input/de_cc_data.txt',  skiprows=1, delimiter=',', names=('id', 'Last_Name', 'First_Name','Drug_Name','Drug_Cost')) #load actual file
    print("reading csv file")
    drugs=pd.read_csv(input, skiprows=1, names=('id', 'Last_Name', 'First_Name','Drug_Name','Drug_Cost')) #load actual file
    # del drugs['id']
    #drugs.info(memory_usage='deep')
    print("creating full name")
    drugs['full_name'] = drugs['First_Name']+'-'+drugs['Last_Name']
    print("deleting unused columns")
    del drugs['id']
    del drugs['First_Name']
    del drugs['Last_Name']
    
    # print(drugs)

    print("gouping")
    grouper = drugs.groupby('Drug_Name')
    print("total cost")
    total_costs = grouper.sum()['Drug_Cost']
    print("unique users")
    unique_names = grouper.nunique()['full_name']
    # print(total_costs)
    # print(unique_names)
    # print(pd.merge(total_costs.to_frame(), unique_names.to_frame(), on='Drug_Name', how='outer'))
    
    print("merge and sort")
    result = pd.merge(unique_names.to_frame(), total_costs.to_frame(), on='Drug_Name', how='outer').sort_values(['Drug_Cost', 'Drug_Name'], ascending=[False, True])
    
    # print(result)
    
    # drugs['full_name'] = drugs.apply(lambda row: row.First_Name +'_' + row.Last_Name, axis=1)
    # drug_pivot=drugs.pivot(index='Drug_Name', columns='full_name', values='Drug_Cost')
    # result = pd.concat([drug_pivot.count(axis=1),drug_pivot.sum(axis=1)], axis=1, sort=False)
    result=result.reset_index()
    result.columns = ['drug_name','num_prescriber','total_cost']
    # result=result.sort_values(['total_cost','drug_name'], ascending=[False,True])
    print("save")
    result.to_csv(output, index=False)

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    pharmacy_counting(*sys.argv[1:])