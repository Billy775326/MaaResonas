import requests
from bs4 import BeautifulSoup

# 发送 GET 请求获取网页内容
url = 'https://www.resonance-columba.com/route'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 查找包含价格数据的表格
    table = soup.find('table')  # 假设页面中有一个表格包含价格数据
    
    if table:
        # 遍历表格的每一行
        for row in table.find_all('tr'):
            # 获取所有单元格
            cells = row.find_all('td')
            if len(cells) > 1:
                # 假设第一列是商品名称，第二列是价格
                product_name = cells[0].get_text(strip=True)
                price = cells[1].get_text(strip=True)
                print(f'商品名称: {product_name}, 价格: {price}')
    else:
        print('未找到包含价格数据的表格。')
else:
    print(f'请求失败，状态码: {response.status_code}')
