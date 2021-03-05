import pandas as pd
#read the log file no header
http_df = pd.read_csv("resources/http.log",
                      sep="\t", header=None,
                      names=['ts', 'uid', 'id_orig_h', 'id_orig_p', 'id_resp_h', 'id_resp_p',
                             'trans_depth', 'method', 'host', 'uri', 'referrer', 'user_agent',
                             'request_body_len', 'response_body_len', 'status_code', 'status_msg',
                             'info_code', 'info_msg', 'filename', 'tags', 'username',
                             'password', 'proxied', 'orig_fuids', 'orig_mime_types', 'resp_fuids',
                             'resp_mime_types', 'sample'])
print(http_df.info())
print(http_df.head())

from datetime import datetime
http_df['ts'] = [
    datetime.fromtimestamp(float(date))
    for date in http_df['ts'].values
]

print(http_df)
print(http_df.info())

http_df = http_df.set_index('ts')
http_df.index = pd.to_datetime(http_df.index)
http_df = http_df.sort_index()
print(http_df)


print(http_df['2012-01-01'])

print(http_df['2012-01':'2012-02'])

print(http_df["2012-01"].request_body_len.mean())

import matplotlib.pyplot as plt
http_df.request_body_len.resample('M').mean().plot()
plt.show()

http_df.request_body_len.resample('Q').mean().plot(kind='bar')
plt.show()

from datetime import date
ts_dthr1 = pd.Timestamp(date(2012,1,1))
ts_dthr2= pd.Timestamp(date(2012,4,1))

values = http_df.loc[(http_df.index>ts_dthr1) &(http_df.index<ts_dthr2)]
print(values[http_df.columns.tolist()[2:7]])

print(http_df.groupby(['resp_mime_types','user_agent']).size())

print(http_df[http_df['user_agent'].isin(['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
                                          'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'])].groupby(['resp_mime_types','user_agent']).size())


executable_types = set(['application/x-dosexec', 'application/octet-stream', 'binary', 'application/vnd.ms-cab-compressed'])
common_exploit_types = set(['application/x-java-applet','application/pdf','application/zip','application/jar','application/x-shockwave-flash'])
print(http_df[http_df['resp_mime_types'].isin(executable_types)].groupby(['resp_mime_types','user_agent']).size())

#print business days only + 10 days
#rng = pd.date_range(start='2012-02-01', periods=10, freq='B')
#print(rng)