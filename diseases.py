# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:44:00 2018

@author: Kulbushan
"""

import sqlite3
from arrhythmiastest import Testarrhythmias
from coronaryartery import Testingcoronatryartery

class Disease(object):
    def demo(self):
        """ A simple demo function to show how to use bank and account classes """
    
        # create a database 
        #conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('heart_disease_database.db')
        
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists patient(
                     patient_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                     name   text,
                     age integer,
                     gender text,
                     blood_group text,
                     disease_name text,
                     test_result text
                     )""")      
        
        conn.commit()
        # create Patient object
        #patient = Patient()
        c.execute("""CREATE TABLE if not exists arrhythmia(
                     test_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                     patient_id   INTEGER,
                     disease_name integer,
                     test_result text
                     )""") 
        conn.commit()
        
        c.execute("""CREATE TABLE if not exists coronatryartery(
                     test_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                     patient_id   INTEGER,
                     disease_name integer,
                     test_result text
                     )""") 
        conn.commit()
        
        # Open Account
        patient_name = input("Enter the patient name: ")
        
        c.execute("SELECT name FROM patient WHERE name=:patient_name", 
                  {'patient_name': patient_name})
        specific_patient_name = c.fetchall()
        if specific_patient_name == []:
            specific_patient_name = ['no']
        
        conn.commit()
        
        if patient_name == specific_patient_name[0][0]:
            print("Patient :", patient_name, "exists")
        else:
            patient_age = int(input("\n Enter the patient age: "))
            patient_gender = input("\n Enter the patient gender: ")
            patient_blood_group = input("\n Enter the patient bloodgroup: ")
            disease_name = ""
            test_result = ""
            
            c.execute("""INSERT INTO patient (name, age, gender, blood_group, disease_name, test_result)
                        VALUES(?,?,?,?,?,?)""", (patient_name, patient_age, patient_gender, patient_blood_group, disease_name,test_result, ))
            conn.commit()
         
            c.execute("SELECT patient_id FROM patient WHERE name=:patient_name", 
                  {'patient_name': patient_name})
           
            conn.commit()
            specific_patient_id = c.fetchall()
            
            patient_id = specific_patient_id[0][0]
           
            print("Enter the option: \n1. Test_Arrhythmias \n2. Test_Coronatry_Artery")
                
            option_test = int(input())
            if option_test == 1:
                arrh = Testarrhythmias(patient_id)
                disease_name,  test_result = arrh.compute_arhy_test()
                c.execute("UPDATE patient set disease_name=:disease_name, test_result=:test_result WHERE patient_id =:patient_id",
                              {'disease_name':disease_name, 'test_result':test_result, 'patient_id':patient_id})
                conn.commit()
                c.execute("""INSERT INTO arrhythmia (patient_id, disease_name, test_result)
                        VALUES(?,?,?)""", (patient_id, disease_name, test_result, ))
                conn.commit()
                
            else:
                cao = Testingcoronatryartery(patient_id)
                disease_name,  test_result = cao.compute_coa_test()
                c.execute("UPDATE patient set disease_name=:disease_name, test_result=:test_result WHERE patient_id =:patient_id",
                              {'disease_name':disease_name, 'test_result':test_result, 'patient_id':patient_id})
                conn.commit()
                c.execute("""INSERT INTO coronatryartery (patient_id, disease_name, test_result)
                        VALUES(?,?,?)""", (patient_id, disease_name, test_result, ))
                conn.commit()
        conn.close()
        
if __name__ == "__main__":
    disease_object = Disease()
    disease_object.demo()

    