import quandl
import requests
import time


quandl.ApiConfig.api_key = "xxxxxx"


quandl.Dataset.all()


# For WTI Crude Oil Prices
#wti_oil = quandl.get('EIA/PET_RWTC_D')


# For Brent Crude Oil Prices
#brent_oil = quandl.get('EIA/PET_RBRTE_D')

def get_quandl_commodity_codes(page_limit=100):
    base_url = "https://www.quandl.com/api/v3/datasets.json?database_code=COM&per_page=100&page="
    commodity_codes = []
    page = 1

    while True:
        response = requests.get(base_url + str(page))
        if response.status_code != 200:
            print("Error fetching data, stopping at page", page)
            break

        data = response.json()
        datasets = data['datasets']
        if not datasets:
            break

        for dataset in datasets:
            commodity_codes.append(dataset['dataset_code'])

        print(f"Fetched page {page}")
        page += 1
        time.sleep(1)  # To avoid hitting the API rate limit

        if page > page_limit:  # Stop after a certain number of pages
            break

    return commodity_codes

commodity_codes = get_quandl_commodity_codes()
print(commodity_codes)