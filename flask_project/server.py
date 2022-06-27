# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:36:14 2022

@author: hakan
"""
import psycopg2 as pg
import psycopg2.extras

def connectToDB(dbname,dbuser,dbpassword,dbhost):
    connectionString='dbname={} user={} password={} host={}'.format(dbname,dbuser,dbpassword,dbhost)
    try:
        engine = pg.connect(connectionString)
    except:
        print("Can't connect to database")
    return engine
        
    'dbname=hkflaskapp user=hkpostgres password=postgres host=localhost'