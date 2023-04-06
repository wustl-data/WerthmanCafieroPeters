import pandas as pd
import requests
import psycopg2

API_KEY = 'DCKF14084FJK2MEI'
# Alt Keys: DTG5GZLOTFOW62UP

wtiURL = 'https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey='
brentURL = 'https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey='
wheatURL = 'https://www.alphavantage.co/query?function=WHEAT&interval=monthly&apikey='
cornURL = 'https://www.alphavantage.co/query?function=CORN&interval=monthly&apikey='
cottonURL = 'https://www.alphavantage.co/query?function=COTTON&interval=monthly&apikey='


def get_data(url, key, name):
    '''
    function get_data - pulls data from alphaVantage website API

    Args:
    url - takes in the urls listed above to access endpoint
    key - api key
    name = name of commodity you want to save

    returns 2D array of prices data for a commodity dating back ~30 years
    
    '''
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

monthlyWTIPrice = get_data(wtiURL, API_KEY, 'WTI')
monthlyBrentPrice = get_data(brentURL, API_KEY, 'BRENT')
monthlyWheatPrices = get_data(wheatURL, API_KEY,'Wheat')
monthlyCornPrices = get_data(cornURL, API_KEY,'Corn')
monthlyCottonPrices = get_data(cottonURL, API_KEY,'Cotton')



merged_prices = pd.merge(monthlyWheatPrices, monthlyCornPrices, on='Month')
merged_prices = pd.merge(merged_prices, monthlyCottonPrices, on='Month')
merged_prices = pd.merge(merged_prices, monthlyBrentPrice, on='Month')
merged_prices = pd.merge(merged_prices, monthlyWTIPrice, on='Month')


#df[df[“column_name”].str.contains('.')==False]

# Replace '.' values with NaN
merged_prices.replace('.', pd.np.nan, inplace=True)

def convert_to_float(toConvert, columns):
    '''
    function convert_to_float - converts columns in df to float and rounds to two decimal places

    Args - 
    toConvert - dataFrame to convert
    columns - columns in that dataframe that need to be rounded

    returns rounded, to float dataframe
    '''
    for col in columns:
        toConvert[col] = toConvert[col].astype(float).round(2)
    return toConvert

merged_prices = convert_to_float(merged_prices, ['Wheat', 'Corn', 'Cotton', 'BRENT', 'WTI'])


# Print the first few rows
print(merged_prices.head())

print(merged_prices[['Corn', 'Cotton', 'BRENT', 'WTI']].round(2))


#melt prices if needed

def melt(df):
    '''
    function melt - melts data from merged_prices dataset

    Args:
    df - dataframe to take in to melt

    Changes 'Price' colun to numeric
    returns melted dataset with currency, unit all USD, and 
    
    '''
    melted = pd.melt(df, id_vars = ['Month'], var_name = 'Commodity', value_name = 'Price')
    melted['Price'] = pd.to_numeric(melted['Price'], errors='coerce')
    melted['Unit', 'Currency'] = 'USD'
    melted['Symbol'] = '$'
    return melted

meltedCommodityPrices = melt(merged_prices)
print(melt(merged_prices))

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "punkinbunker"
)
curr = conn.cursor()
merged_prices.to_csv('merged_prices.csv', index=False)
meltedCommodityPrices.to_csv('melted_commodity_prices.csv', index=False)


def csv2postgres(pathname):

    conn = psycopg2.connect(database="COMMODITY_DATABASE",
                        user='postgres', password='pass', 
                        host='127.0.0.1', port='5432'
)
  
    conn.autocommit = True
    cursor = conn.cursor()
  
  
    sql = '''CREATE TABLE DETAILS(month date NOT NULL,\
    Commodity char(20),\
    price double precision, currency char(5), symbol char(1));'''
  
    cursor.execute(sql)  


csv2postgres("get_money")