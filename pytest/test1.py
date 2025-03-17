import requests
from lxml import etree
url="https://www.resonance-columba.com/route"
html_str = requests.get(url)
html_str.encoding = "utf-8"
xpath_str = etree.HTML(html_str.text)
data_price = xpath_str.xpath('//table')
print(data_price)