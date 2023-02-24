import pandas as pd
import requests
API_KEY = 'DCKF14084FJK2MEI'
# Alt Keys: DTG5GZLOTFOW62UP

wtiURL = 'https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey='
brentURL = 'https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey='
wheatURL = 'https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey='
cornURL = 'https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey='
cottonURL = 'https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey='


def get_data(url, key, name):
    commoditiesURL = url + key
    commoditiesR = requests.get(commoditiesURL)
    commoditiesData = pd.DataFrame(commoditiesR.json())

    prices = []
    dates = []
    for i in range(len(commoditiesData)):
        prices.append(commoditiesData['data'].iloc[i]['value'])
        dates.append(commoditiesData['data'].iloc[i]['date'])

    d = {'Month': dates, name: prices}
    priceArray = pd.DataFrame(d)
    return priceArray

monthlyWTIPrice = get_data(wheatURL, API_KEY, 'WTI')
monthlyBrentPrice = get_data(wheatURL, API_KEY, 'BRENT')
monthlyWheatPrices = get_data(wheatURL, API_KEY,'Wheat')
monthlyCornPrices = get_data(cornURL, API_KEY,'Corn')
monthlyCottonPrices = get_data(cottonURL, API_KEY,'Cotton')



merged_prices = pd.merge(monthlyWheatPrices, monthlyCornPrices, on='Month')
merged_prices = pd.merge(merged_prices, monthlyCottonPrices, on='Month')
merged_prices = pd.merge(merged_prices, monthlyBrentPrice, on='Month')
merged_prices = pd.merge(merged_prices, monthlyWTIPrice, on='Month')


#df[df[“column_name”].str.contains('.')==False]

print(merged_prices.head())
