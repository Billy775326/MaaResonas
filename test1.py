import requests
from bs4 import BeautifulSoup

def parse_value(value_str):
    """将带'万'的字符串转换为整数"""
    if value_str == '-' or not value_str:
        return 0
    return int(float(value_str.replace('万', '')) * 10000)


url = 'https://www.resonance-columba.com/route'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    
    if table:
        # 提取列标题(终点站)
        headers = [th.get_text(strip=True) for th in table.find('tr').find_all('th')][1:]
        
        # 收集所有数据点
        data_points = []
        
        # 遍历数据行
        for row in table.find_all('tr')[1:]:
            cells = row.find_all(['th', 'td'])
            if len(cells) < 2:
                continue
            
            start = cells[0].get_text(strip=True)  # 起点站
            values = cells[1:]  # 对应的各终点站值
            
            for i, cell in enumerate(values):
                end = headers[i] if i < len(headers) else f'Unknown_{i}'  # 终点站
                value = parse_value(cell.get_text(strip=True))
                
                if value > 0 and start != end:  # 排除无效值和自身到自身的情况
                    data_points.append((value, start, end))
        
        # 按数值降序排序并取前三个
        top3 = sorted(data_points, key=lambda x: x[0], reverse=True)[:3]
        
        # 打印结果
        print("数值最大的三个运输路线:")
        for idx, (value, start, end) in enumerate(top3, 1):
            print(f"{idx}. {start} → {end} : {value//10000}万 (原始值: {value})")
            
    else:
        print("未找到数据表格")
else:
    print(f"请求失败，状态码: {response.status_code}")