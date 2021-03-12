from datetime import date, datetime
import matplotlib.pyplot as plt
import pandas as pd

logFile = './resources/http.log'

httpLog = pd.read_csv(logFile,
                      sep='\t',
                      header=None,
                      names=['ts', 'uid', 'id_orig_h', 'id_orig_p', 'id_resp_h', 'id_resp_p',
                             'trans_depth', 'method', 'host', 'uri', 'referrer', 'user_agent',
                             'request_body_len', 'response_body_len', 'status_code', 'status_msg',
                             'info_code', 'info_msg', 'filename', 'tags', 'username',
                             'password', 'proxied', 'orig_fuids', 'orig_mime_types', 'resp_fuids',
                             'resp_mime_types', 'sample'])

httpLog['ts'] = [
    datetime.fromtimestamp(float(date))
    for date in httpLog['ts'].values
]

httpLog = httpLog.set_index('ts')
httpLog.index = pd.to_datetime(httpLog.index)
httpLog = httpLog.sort_index()

httpLogPorts = httpLog.where(
    (httpLog.id_resp_p != 80) & (httpLog.id_resp_p != 8080))

print(httpLogPorts)

httpLog.request_body_len.resample('Q').mean().plot(kind='line')
plt.show()

httpLogPorts.request_body_len.resample('Q').mean().plot(kind='line')
plt.show()

executable_types = set(['application/x-dosexec', 'application/octet-stream',
                        'binary', 'application/vnd.ms-cab-compressed'])

common_exploits = set(['application/x-java-applet', 'application/pdf',
                       'application/zip', 'application/jar', 'application/x-shockwave-flash'])

print(executable_types, '\n', common_exploits)

# httpLog.info()
# httpLog.head()
