# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:03:50 2018

@author: User
"""

class Testarrhythmias():    
   
    def __init__(self, patient_id):
        self.patient_id = patient_id
     
    def compute_arhy_test(self):
        try:
            chest_type = ['typical', 'atypical', 'non-anginal']
            disease_absence_status = 'negative'
            disease_name = 'Arrhythmia'
            diagnosis_result = 'positive'
            chest_pain = input('Enter the chest pain type(typical, atypical, non-anginal): \n')
            if chest_pain in chest_type:
                print("Test has determined patient with", diagnosis_result, disease_name)
                return disease_name, diagnosis_result               
            else:
                print("Test has determined patient with", disease_absence_status, disease_name)
                return disease_name, disease_absence_status
        except:
                print("Error, please enter data accordingly.")

# Validation using test cases
if __name__ == "__main__":
    
    arrhym = Testarrhythmias(1)
    arrhym.compute_arhy_test()

    
    