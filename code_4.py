import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)

    querys = f"date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}'"

    big_mac_price_by_year = df.query(querys) 

    mean_price_by_year_and_country_code = big_mac_price_by_year['dollar_price']

    country = df.loc[mean_price_by_year_and_country_code] 

    bmpby = f"{country['dollar_price']}  {country['year']}"   

    return bmpby                       


    return big_mac_price_by_year.round(2)    #number 

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)

    query = f"iso_a3 == '{country_code}'"

    big_mac_price_by_country = df.query(query)

    mean_price = big_mac_price_by_country['dollar_price']

    country = df.loc[mean_price]

    mean_country_price = f"{country['dollar_price'].mean()}"

    return mean_country_price    

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)

    querys = f"date >= '{year}-01-01' and date <= '{year}-12-31'"

    the_expensive_big_mac_price_by_year = df.query(querys)

    min_price = the_expensive_big_mac_price_by_year['dollar_price'].idxmin()

    country_code = df.loc[min_price]

    min_big_mac = f"{country_code['name']}({country_code['iso_a3']}): ${country_code['dollar_price'].round(2)}"
    
    return min_big_mac


def get_the_most_expensive_big_mac_price_by_year(year):

    df = pd.read_csv(big_mac_file)

    querys = f"date >= '{year}-01-01' and date <= '{year}-12-31'"

    the_expensive_big_mac_price_by_year = df.query(querys)

    max_price = the_expensive_big_mac_price_by_year['dollar_price'].idxmax()

    country_code = df.loc[max_price]

    max_big_mac = f"{country_code['name']}({country_code['iso_a3']}): ${country_code['dollar_price'].round(2)}"

    return max_big_mac

if __name__ == "__main__":

    year = input("The year desired:  ")
    country_code = input("Country Code: ").upper


    print(get_the_most_expensive_big_mac_price_by_year(year))

    print(get_the_cheapest_big_mac_price_by_year(year))

    print(get_big_mac_price_by_country(country_code))

    print(get_big_mac_price_by_year(year,country_code))








  



   
    

   