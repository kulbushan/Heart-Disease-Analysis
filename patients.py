# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:13:18 2018

@author: User
"""

class Patient():
    
 def __init__(self, patient_list):
        self.patient_list = patient_list[:]
        
 def get_patient_details(self):
     print("Patient_ID     Name       Age Gender Blood_Group  Disease_Name  Test_Result")
     for patient in self.patient_list:
           print(patient[0] , ' ' , patient[1] , ' ' , patient[2] , ' ' , patient[3] , ' ' , patient[4] , ' ' , 
                 patient[5] , ' ' , patient[6] )
     
# Validation using test casess
if __name__ == "__main__":
    #Test Account class
    patient_list1 = [[1,'dhanush', 15, 'male', 'A+', 'arryh','negative'], 
                     [2,'ramya', 30, 'female', 'A+','cad','positive']]

    patient_test_1 = Patient(patient_list1)
    patient_test_1.get_patient_details()