import requests
import time

quandl_api_key = "xxxxxxx"

def get_quandl_commodity_codes(page_limit=100):
    base_url = "https://www.quandl.com/api/v3/datasets.json?api_key=" + quandl_api_key + "&database_code=COM&per_page=100&page="
    oil_related_codes = []
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
            name = dataset['name'].lower()
            if 'oil' in name or 'crude' in name or 'brent' in name or 'wti' in name:
                oil_related_codes.append(dataset['database_code'] + '/' + dataset['dataset_code'])

        print(f"Fetched page {page}")
        page += 1
        time.sleep(1)  # To avoid hitting the API rate limit

        if page > page_limit:  # Stop after a certain number of pages
            break

    return oil_related_codes

oil_commodity_codes = get_quandl_commodity_codes()
print(oil_commodity_codes)
