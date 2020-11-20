from GraphFunc import *
from Queries import *
import unittest
import datetime
import requests
import json
class TestMethods(unittest.TestCase):
    def test_symbol(self):
        self.assertTrue('userInput1'.isupper())
        self.assertTrue('userInput1'.isalnum())
    def test_chart(self):
        self.assertTrue('userInput2' === 1 || 'userInput2' === 2)
    def test_series(self):
        self.assertTrue('userInput3'.isnum())
        self.assertTrue('userInput3' === 1 || 'userInput3' === 2 || 'userInput3' === 3 || 'userInput3' === 4)
    def test_start(self):
        self.assertTrue(datetime.datetime.strptime('userInput4', '%Y-%m-d'))
    def test_end(self):
        self.assertTrue(datetime.datetime.strptime('userInput5', '%Y-%m-d'))

if __name__ == '__main__':
    unittest.main()
userChoices = queries()

if(userChoices[2] == 1):
    payload = {'function':'TIME_SERIES_INTRADAY','symbol':userChoices[0],'interval':'30min','apikey':'P8HT9FLVF2HF2HZB'}
    nestedName = "Time Series (30min)"
elif(userChoices[2] == 2):
    payload = {'function':'TIME_SERIES_DAILY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}
    nestedName = "Time Series (Daily)"
elif(userChoices[2] == 3):
    payload = {'function':'TIME_SERIES_WEEKLY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}
    nestedName = "Time Series (Weekly)"
else:
    payload = {'function':'TIME_SERIES_MONTHLY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}
    nestedName = "Time Series (Monthly)"

results = requests.get('https://www.alphavantage.co/query', params=payload)

results.json()

while True:
    # Collect dates from user and split into three different fields
    try:
        begin_date = input('Enter a beginning date in YYYY-MM-DD format: ')
        begin_year, begin_month, begin_day = map(int, begin_date.split('-'))
        date1 = datetime.date(begin_year, begin_month, begin_day)

        end_date = input('Enter a end date in YYYY-MM-DD format: ')
        end_year, end_month, end_day = map(int, end_date.split('-'))
        date2 = datetime.date(end_year, end_month, end_day)

        # Compare the dates to make sure they are valid
        if (begin_year > end_year):
            print("Enter valid dates")
            continue
        elif (begin_year == end_year):
            if (begin_month > end_month):
                print("Enter valid dates")
                continue
            elif (end_month > begin_month):
                break
            elif (end_month == begin_month):
                if (begin_day >= end_day):
                    print("Enter valid dates")
                    continue
                else:
                    break
        else:
            break

    # Using Try/Except to easily restart if an error occurs
    except:
        print("Enter valid dates!")
        continue

# Prints out the dates to make sure everything worked the way it's supposed to
print("Start date: " + str(date1))
print("End date: " + str(date2))

date = []
open_value = []
high_value = []
low_value = []
close_value = []
volume_value = []

for results, value in results.json()[nestedName].items():
    
    if(results >= begin_date and results <= end_date):
    
        date.append(results)
        open_value.append(float(value["1. open"]))
        high_value.append(float(value["2. high"]))
        low_value.append(float(value["3. low"]))
        close_value.append(float(value["4. close"]))
        volume_value.append(float(value["5. volume"]))

print(date)

if userChoices[1] == 1:
    printBarGraph(userChoices[0], date, open_value, high_value, close_value, low_value)
else:
    printLineGraph(userChoices[0], date, open_value, high_value, close_value, low_value)

