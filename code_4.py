
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)

    query = f"year = {year}, and iso_a3 =='{country_code}'"
    big_mac_price_by_year = df.query(query)

    return big_mac_price_by_year.round(2)    #number 
    
def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)

    query = f"iso_a3 == '{country_code}'"
    big_mac_price_by_country = df.query(query)

    return big_mac_price_by_country.round(2)    #number 
    
def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)

    query = f"year == {year}"
    the_cheapest_big_mac_price_by_year =df.query(query)

    return the_cheapest_big_mac_price_by_year.round(2)
    # message
def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query = f""
    the_most_expensive_big_mac_price_by_year = df.query(query)

    return the_most_expensive_big_mac_price_by_year.round(2)
if __name__ == "__main__":

    year = int(input("Year desired: "))
    country_code = input("Enter country code: ")

    big_mac_price_by_year = get_big_mac_price_by_year(year,country_code)
    print(f"{big_mac_price_by_year}")

    big_mac_price_by_country = get_big_mac_price_by_country(country_code)
    print(f"{big_mac_price_by_country}")

  