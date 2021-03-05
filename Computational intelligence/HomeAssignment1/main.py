'''
Code meant to solve the first home assignment, specifically the first excercise.

Daniel Roa - A01021960
05/03/2021
'''
#Imported libraries
import pandas as pd
import random
from datetime import datetime

#conn.log file is located in the resource folder
logFile = './resources/conn.log'

#Size of the sample will be the equivalent to the 10% of the total sample.
sampleSize = 0.1 

#Reading the conn.log file and using the total amount of the sample as well
convLog = pd.read_csv(logFile, sep='\t', header=None, skiprows=lambda i: i > 0 and random.random() > sampleSize, names=[
    'ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto', 'service', 
    'duration', 'orig_bytes', 'resp_bytes', 'conn_state', 'local_orig', 'missed_bytes', 
    'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'tunnel_parents', 
    'threat', 'sample'
])

""" #Used to check the overall size of the sample
print('Sample information\n', convLog.info())
#Used to check the sample's column heads.
print('Sample heads\n', convLog.head()) """

#Convert the timestamp to datetime and sort the sample
convLog['ts'] = [
    datetime.fromtimestamp(float(date))
    for date in convLog['ts'].values
]

convLog = convLog.set_index('ts')
convLog.index = pd.to_datetime(convLog.index)
convLog = convLog.sort_index()

print(convLog)