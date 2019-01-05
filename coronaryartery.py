# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:15:30 2018

@author: User
"""

class Testingcoronatryartery():
    
    def __init__(self, patient_id):
        self.patient_id = patient_id
        
        
    def compute_coa_test(self):
        try:
            chest_type = ['typical', 'atypical', 'non-anginal']
            disease_absence_status = 'negative'
            disease_name = 'Coronatry Artery Disease'
            diagnosis_result = 'positive'
            systolic_blood_pressure = int(input('\n Enter the systolic blood pressure: '))
            diastolic_blood_pressure = int(input('Enter the diastolic blood pressure: '))
            chest_pain = input('Enter the chest pain type(typical, atypical, non-anginal): \n')
            if chest_pain in chest_type and systolic_blood_pressure > 140 and diastolic_blood_pressure > 90:
                print("Test has determined patient with", diagnosis_result, disease_name)
                return disease_name, diagnosis_result               
            else:
                print("Test has determined patient with", disease_absence_status, disease_name)
                return disease_name, disease_absence_status
        except:
                print("Error, please enter data accordingly.")
                
# Validation using test cases
if __name__ == "__main__":
    
    artery = Testingcoronatryartery(1)
    artery.compute_coa_test()

    
    