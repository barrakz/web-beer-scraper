from requests_html import HTMLSession

url = 'https://www.beerwulf.com/en-gb/c?page=1&style=Lager'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

products = r.html.xpath('//*[@id="product-items-container"]', first=True)

for item in products.absolute_links:
    r = s.get(item)
    name = r.html.find('div.product-detail-info-title', first=True).text
    subtext = r.html.find('div.product-subtext', first=True).text
    price = r.html.find('span.price', first=True).text

    try:
        country = r.html.find('dd.js-beer-country', first=True).text
    except:
        country = 'none'

    if r.html.find('div.add-to-cart-container'):
        stock = 'dostepny'
    else:
        stock = 'niedotepny'

    if r.html.find('div.discount-tab'):
        promo = "IS ON PROMO!!!"
    else:
        promo = "NO PROMO"

    print(name, "-----", subtext, "-----", price, "-----", stock, "-----", country, "-----", promo)
