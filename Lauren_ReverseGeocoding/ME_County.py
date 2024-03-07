from uszipcode import SearchEngine

def get_county(address):
    search = SearchEngine(simple_zipcode=True)
    result = search.by_address(address)
    
    if result:
        county = result[0].county
        return county
    else:
        return None

address = "333 Western Ave, South Portland, ME 04106"
county = get_county(address)

if county:
    print(f"The address is in {county} County.")
else:
    print("County information not found.")
