# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:44:38 2017

@author: PCN1HC
"""

import pandas as pd

class WorkOnCsvFile(object):
    
    def __init__(self):
        self.Data_file = pd.read_csv('Data.csv')
        self.Get_WI_Already_Add_To_Prime = self.Data_file['Id'].values
        self.Get_WI_Last_Week = []
        self.Task_Not_Add_To_Prime = pd.DataFrame()
        
    def SaveData(self):       
        self.Data_Last_Week = pd.read_csv('empty.csv')
        self.Get_WI_Last_Week = self.Data_Last_Week['Id'].values
#        print(self.Data.columns.values)
        
    def Compare(self): 
        self.SaveData()
        self.save_index = []
        for first in self.Get_WI_Already_Add_To_Prime:
            i = 0
            for second in self.Get_WI_Last_Week:
                if (first == second):
                    self.save_index.append(i)
                i += 1
        self.DeleteAddedTask()
        self.Task_Not_Add_To_Prime.to_csv('Task.csv', index=False, header=self.Data_Last_Week.columns.values)
        data = pd.read_csv('Data.csv')
#        data = data.append(pd.read_csv('a.csv'))
        data = data.append(self.Task_Not_Add_To_Prime)
        data.to_csv('Data.csv', index=False)
#        data.to_csv('b.csv', index=False)
#        data = pd.read_csv('b.csv')
        print(data)
        
    def DeleteAddedTask(self):
        index = ([ i for i in range (0,len(self.Get_WI_Last_Week ))])
        OrgianlDF = pd.DataFrame(self.Data_Last_Week , index)
        self.Task_Not_Add_To_Prime = OrgianlDF.drop(self.save_index)
#        print (self.Task_Not_Add_To_Prime)
        
WorkOnCsvFile().Compare()
print ('done')
