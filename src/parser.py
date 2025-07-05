import math

import requests

headers = {
    'User-Agent': 'Mozilla/5.0'  # mimic a regular browser
}

url_price = 'https://www.marktplaats.nl/lrp/api/search?attributeRanges[]=PriceCents%3A10000%3A80000&attributesById[]=0&l1CategoryId=728&l2CategoryId=748&limit=30&offset=0&sortBy=OPTIMIZED&sortOrder=DECREASING&viewOptions=list-view'

def getItems(offset):
    url = f'https://www.marktplaats.nl/lrp/api/search?l1CategoryId=728&l2CategoryId=748&limit=30&offset={offset}&sortBy=OPTIMIZED&sortOrder=DECREASING&viewOptions=list-view'
    response = requests.get(url, headers=headers)
    items = []
    if response.ok:
        data = response.json()
        # print(data['listings'][0].keys())
        # print(data['listings'][0]['priceInfo'])

        for item in data['listings']:
            print(item)
            if item['priceInfo']['priceCents'] > 0 and 'imageUrls' in item:
                dict = {'title': item['title'], 'price': math.ceil(item['priceInfo']['priceCents']/100), 'img': "https:" + item['imageUrls'][0], 'url': "https://www.marktplaats.nl" + item['vipUrl']}
                items.append(dict)

        print(items)
    else:
        print("Failed to fetch data")
    return items

# getItems()