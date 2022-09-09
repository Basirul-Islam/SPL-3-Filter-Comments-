from datetime import datetime
import sys
import requests
import json
#import array


class object:
    def __init__(self, trading_code, ltp, closep, change, ycp, ):
        self.trading_code = trading_code
        self.ltp = ltp
        self.closep = closep
        self.change = change
        self.ycp = ycp


def get_company_statistics():
    arr = []
    response = requests.get(
        "https://www.amarstock.com/LatestPrice/34267d8d73dd?fbclid=IwAR3Nnl2tdnlEuJTOlZgH4yBuQR9ngbSg7y70e_kskcaWqwBfdqSkE7E8-II")

    for item in response.json():
        obj = object(item['FullName'], item['LTP'], item['Close'], item['Change'], item['YCP'])
        arr.append(obj.__dict__)

    return arr



dateS = sys.argv[1]
dateE = sys.argv[2]

start = datetime.strptime(dateS, '%Y-%m-%d')
end = datetime.strptime(dateE, '%Y-%m-%d')

days = (end - start).days

#a = array.array("i",(i for i in range(0,100)))
a = []
for x in range(100):
    a.append(x)
print("Start date: ", start)
print("End date: ", end)
print("Days between: ", days)
print("array: ", a)
print("Trade Statistics: ", get_company_statistics())