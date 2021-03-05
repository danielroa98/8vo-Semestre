import pandas as pd

logFile = './resources/conn.log'

convLog = pd.read_csv(logFile, sep='\t', header=None, names=[
    'ts', 'uid', 'id_orig_h', 'id_orig_p', 'id_resp_h', 'id.resp_p', 'proto', 'service', 
    'duration', 'orig_bytes', 'resp_bytes', 'conn_state', 'local_orig', 'missed_bytes', 
    'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'tunnel_parents', 
    'threat', 'sample'
])

print(convLog.head())

convLog.DataFrame.sample(n=None, frac=0.1, replace=False, weights=None, random_state=None, axis=None)
