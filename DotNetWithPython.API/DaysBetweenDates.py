from datetime import datetime
import sys
import requests
import json
import array




class status:
    def __init__(self, up, down, unchanged, up_percentage, down_percentage, unchanged_percentage):
        self.up = up
        self.down = down
        self.unchanged = unchanged
        self.up_percentage = up_percentage
        self.down_percentage = down_percentage
        self.unchanged_percentage = unchanged_percentage


def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return round(percentage, 2)

def get_trade_statistics():
    status_response = requests.get(
        "https://www.amarstock.com/Info/DSE")
    status_response_data = status_response.json()

    total = status_response_data['Advance'] + status_response_data['Decline'] + status_response_data['Unchange']
    stat = status(status_response_data['Advance'], status_response_data['Decline'], status_response_data['Unchange'],
                  percentage(status_response_data['Advance'], total),
                  percentage(status_response_data['Decline'], total),
                  percentage(status_response_data['Unchange'], total))


    return stat.__dict__



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
#a = []
#for x in range(100):
    #a.append(x)
print("Start date: ", start)
print("End date: ", end)
print("Days between: ", days)
#print("array: ", a)
print("Trade Statistics: ", get_trade_statistics())
print("company Statistics: ", get_company_statistics())