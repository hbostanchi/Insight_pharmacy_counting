#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:08:16 2019

@author: halleh
"""


#import os
import sys

def pharmacy_counting(input,output):
    import pandas as pd
    #path=os.getcwd()
    #drugs=pd.read_table(path+'/input/de_cc_data.txt',  skiprows=1, delimiter=',', names=('id', 'Last_Name', 'First_Name','Drug_Name','Drug_Cost')) #load actual file
    drugs=pd.read_csv(input, skiprows=1, names=('id', 'Last_Name', 'First_Name','Drug_Name','Drug_Cost')) #load actual file
    del drugs['id']
    #drugs.info(memory_usage='deep')
    drugs['full_name'] = drugs.apply(lambda row: row.First_Name +'_' + row.Last_Name, axis=1)
    drug_pivot=drugs.pivot(index='Drug_Name', columns='full_name', values='Drug_Cost')
    result = pd.concat([drug_pivot.count(axis=1),drug_pivot.sum(axis=1)], axis=1, sort=False)
    result=result.reset_index()
    result.columns = ['drug_name','num_prescriber','total_cost']
    result=result.sort_values(['total_cost','drug_name'], ascending=[False,True])
    result.to_csv(output, index=False)

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    pharmacy_counting(*sys.argv[1:])