import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)

    query = df.loc[(df['date'] == {year}) & (df.iso_a3 == {country_code}.upper())]





    big_mac_price_by_year = df.query(query)

    return big_mac_price_by_year.round(2)    #number 
    
def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)

    query = df.iso_a3 == {country_code}
    big_mac_price_by_country = df.query(query)





    return big_mac_price_by_country.round(2)    #number 
    



def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    

   # the_cheapest_big_mac_price_by_year = df.query(query)



#
  #  return the_cheapest_big_mac_price_by_year.round(2)
    
    
    
    
    
    # message
def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query = f"date == {year}"
    the_most_expensive_big_mac_price_by_year = df.query(query)

  
  
  
  
  
    return the_most_expensive_big_mac_price_by_year.round(2)



if __name__ == "__main__":
    df = pd.read_csv(big_mac_file)

    print(df.columns)

    print(df.iso_a3)


    year = (input("Year desired: "))
    country_code = str(input("Country Code: ").lower())


    df = pd.read_csv(big_mac_file)

    #query_for_year = df.loc[(df.date == year) & (df.iso_a3 == country_code)]

    query_for_country = f"df.loc[df['iso_a3'] == country_code]"

    #big_mac_price_by_country = df.query(query_for_country)

    print(query_for_country)






   
    

   