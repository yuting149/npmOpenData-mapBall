import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import json
import csv


datalat, targetlat = [], []
csv = pd.read_csv("coordict.csv", encoding="utf8")

datalat = csv[['orilat']]  # 'lat': 緯度, 'lng': 經度
datalat = np.array(datalat)
targetlat = csv[['reallat']]
targetlat = np.array(targetlat)
datadic_X_train, datadic_X_test, datadic_y_train, datadic_y_test = train_test_split(
    datalat, targetlat, train_size=0.80, test_size=0.2)  # 前75%是訓練集、後25%當測試集
regrlat = linear_model.LinearRegression()
regrlat.fit(datadic_X_train, datadic_y_train)
datadic_y_pred = regrlat.predict(datadic_X_test)
print('----Linear Regressionlatlatlat----')
print("Mean absolute error:", mean_absolute_error(
    datadic_y_test, datadic_y_pred))
twpre = regrlat.predict(670)
print('----twprelat----')
print(twpre)

# ============================
datalng = csv[['orilng']]  # 'lat': 緯度, 'lng': 經度
datalng = np.array(datalng)
targetlng = csv[['reallng']]
targetlng = np.array(targetlng)
datadic_X_train, datadic_X_test, datadic_y_train, datadic_y_test = train_test_split(
    datalng, targetlng, train_size=0.80, test_size=0.2)  # 前75%是訓練集、後25%當測試集
regrlng = linear_model.LinearRegression()
regrlng.fit(datadic_X_train, datadic_y_train)
datadic_y_pred = regrlng.predict(datadic_X_test)
print('----Linear Regressionlnglnglng----')
print("Mean absolute error:", mean_absolute_error(
    datadic_y_test, datadic_y_pred))
twpre = regrlng.predict(3000)
print('----twprelng----')
print(twpre)

if __name__ == '__main__':
    oricoo = json.loads(
        open('countryNameAndOriCoor.json', encoding='utf8').read())
    for i in oricoo:
        i['reallat'] = regrlat.predict(i['orilat'])[0][0]
        i['reallng'] = regrlng.predict(i['orilng'])[0][0]
    print(oricoo)
    # with open('countryNameCoorResult.json', 'w', encoding="utf8") as outfile:
    #     json.dump(oricoo, outfile)
    # write_csv(oricoo, 'countryNameAndOriCoor.csv')
