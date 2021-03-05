import pandas as pd

logfile_header = 'resources/conn_sample_header.log'
#read the log file with header
conn_df_header = pd.read_csv(logfile_header,
                      sep=",")

#read the log file no header
logfile_no_header = 'resources/conn_sample_noheader.log'
conn_df_no_header = pd.read_csv(logfile_no_header,
                      sep=",", header=None,
                      names=['ts','uid','id_orig_h','id_orig_p',
                             'id_resp_h','id.resp_p',
                             'proto','service','duration','orig_bytes','resp_bytes',
                             'conn_state','local_orig','missed_bytes',
                             'history','orig_pkts','orig_ip_bytes','resp_pkts','resp_ip_bytes',
                             'tunnel_parents','threat','sample'])


######## ANALYSIZING DATASET #########################

#basic check of input,(values = head or  tail)
print(conn_df_no_header.head())

#basic info of structure of dataset
print(conn_df_no_header.info())
""" 
#shape of file
print(conn_df_header.shape)

#data sumarization
print(conn_df_header.describe())
 """
#data types
print(conn_df_no_header.dtypes)
'''

#Return with the unique values of ‘id_orig_h' attribute.
print(conn_df_header.id_orig_h.unique())
# or using this sintaxe -> print(conn_df_header['id_orig_h'].unique())

#count the instances
print(conn_df_header.id_orig_h.value_counts())

#remove a column
print(conn_df_header.head())
conn_df_header.drop('threat', axis=1, inplace=True)
print(conn_df_header.head())

#drop two lines (0 and 2)
print(conn_df_header.head())
conn_df_header.drop([0,2], axis=0,inplace=True)
print(conn_df_header.head())

#get the lines where the service is ssl
#step 1 -> create a variable with TRUE where the condition is applied
ssl_lines = conn_df_header.service=='ssl'
#step 2 -> select in the frames, the lines where variables is true
print(conn_df_header[ssl_lines])

############################ ILOC Ops ########################

#get the  first line
print(conn_df_header.iloc[0])

#get a specific field in the first line
srv = conn_df_header.iloc[0].service
id_orig_h =conn_df_header.iloc[0].id_orig_h
print(srv, id_orig_h)

#print all lines with field 2 (id_orig_h)
print(conn_df_header.iloc[:,2])

#print the first three lines of field 2
print(conn_df_header.iloc[:3,2])

#'get line 1 to 3 (excluded line 1 and 3) of field 2
print(conn_df_header.iloc[1:3,2])

#'get line 1, 2 3  of field 2')
print(conn_df_header.iloc[[1,2,3],2])

#get line 1, 2 3  of field 0 and 2 => ts  & id_orig_p)
print('\nThe first and second columns\n')
print(conn_df_header.iloc[[1,2,3],[0,3]])

#('get the 5th last line')
print(conn_df_header.iloc[-5]) #

########### loc ################
#'get the id_orig_h in the first line ')
print(conn_df_header.loc[:0,'id_orig_h'])

#'get all information from the fields above')
print(conn_df_header.loc[:, ['ts','uid','id_orig_h','id_orig_p']])


print('return the values with  complex condition assessment')
values = conn_df_header.loc[(conn_df_header.service=='http') & (conn_df_header.id_orig_h=='192.168.202.79')]
print(values.iloc[:,[0,3,5]]) # only the fields [ts  id_orig_p  id_resp_p]


print('return the values when the condition is true')
print(conn_df_header.loc[conn_df_header.service=='http'])


print('return the values inside the set')
blacklist = set(['192.168.202.79', '192.168.202.85'])
blacklist_values = conn_df_header.id_orig_h.isin(blacklist)
print(conn_df_header[blacklist_values])
'''