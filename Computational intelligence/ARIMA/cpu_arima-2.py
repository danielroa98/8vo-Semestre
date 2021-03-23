
#import pyflux as pf
import matplotlib.pyplot as plt


#read data and split and test and training set
import pandas as pd
data = pd.read_csv('cpu-full-a.csv',parse_dates=[0], infer_datetime_format=True)

import arima_utils
arima_utils.adfuller_test(data['cpu'])
arima_utils.plot_series(data['cpu'],'Original Series')

data['Value First Difference'] = data['cpu'] - data['cpu'].shift(1)
arima_utils.adfuller_test(data['Value First Difference'].dropna())
arima_utils.plot_series(data['Value First Difference'],'Value First Difference')

data['Value 12 Difference'] = data['cpu'] - data['cpu'].shift(12)
arima_utils.adfuller_test(data['Value 12 Difference'].dropna())
arima_utils.plot_series(data['Value 12 Difference'],'Value 12 Difference')

arima_utils.plot_pacf(data['cpu'])

arima_utils.plot_acf(data['cpu'])

# Define the model
model = pd.ARIMA(data=data,
                   ar=2, ma=20, integ=0, target='cpu')
x = model.fit("PML")
#x = model.fit("M-H")

#https://pyflux.readthedocs.io/en/latest/bayes.html
print(x.summary())

print(x.scores)


model.plot_fit()
plt.show()

'''
Use the data that you have and see that predictions fit with the values that you have in the dataset.
h = How many steps to forecast ahead
past_values: How many past datapoints to plot
'''
model.plot_predict_is(h=30)
plt.show()

model.plot_predict_is(h=100, past_values=40)
plt.show()

#How many steps to forecast ahead
model.plot_predict(h=200,past_values=40)
plt.show()

#How many steps to forecast ahead
fcast = model.predict(h=200)
print(fcast)



