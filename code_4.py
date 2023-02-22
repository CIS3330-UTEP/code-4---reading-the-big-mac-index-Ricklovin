
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)

    query = f"year = {year}, and iso_a3 =='{country_code}'"
    big_mac_price_by_year = df.query(query)

    return big_mac_price_by_year 
     # Number round 2
def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)

    query = f"iso_a3 == '{country_code}'"

    big_mac_price_by_country = df.query(query)

    return big_mac_price_by_country 
    # number round 2
def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)

    query = f""

    the_cheapest_big_mac_price_by_year =df.query(query)

    return the_cheapest_big_mac_price_by_year 
    # message
def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query = f""
    the_most_expensive_big_mac_price_by_year = df.query(query)

    return the_most_expensive_big_mac_price_by_year
    # mess
if __name__ == "__main__":
    print(get_big_mac_price_by_year)