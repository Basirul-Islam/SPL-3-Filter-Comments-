from datetime import datetime
import sys
import requests
import json
import array

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def predict(comment):
    df = pd.read_csv("YoutubeSpamMergedData.csv")
    #print(df.head())
    df_data = df[["CONTENT", "CLASS"]]
    # Features and Labels
    df_x = df_data['CONTENT']
    df_y = df_data.CLASS
    # Extract Feature With CountVectorizer
    corpus = df_x
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)  # Fit the Data

    X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
    # Naive Bayes Classifier

    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    # clf.score(X_test, y_test)
    for item in df.head():
        data = [item]
        vect = cv.transform(data).toarray()
        prediction = clf.predict(vect)
        print(prediction)
    data = [comment]
    vect = cv.transform(data).toarray()
    my_prediction = clf.predict(vect)

    return my_prediction


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


comment = sys.argv[1]
# dateS = sys.argv[1]
# dateE = sys.argv[2]

# start = datetime.strptime(dateS, '%Y-%m-%d')
# end = datetime.strptime(dateE, '%Y-%m-%d')

# days = (end - start).days

# a = array.array("i",(i for i in range(0,100)))
# a = []
# for x in range(100):
# a.append(x)
# print("Start date: ", start)
# print("End date: ", end)
# print("Days between: ", days)
# print("array: ", a)
# print("Trade Statistics: ", get_trade_statistics())
# print("comment: ", comment)
if predict(comment) == 1:
    print("Spam Comment")
else:
    print("not Spam")
# print("company Statistics: ", get_company_statistics())
