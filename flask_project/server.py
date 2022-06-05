# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:36:14 2022

@author: hakan
"""
import psycopg2
import psycopg2.extras

def connectToDB():
    connectionString='dbname=hkflaskapp user=hkpostgres password=postgres host=localhost'
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Can't connect to database")
        
    