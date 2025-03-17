import requests
from bs4 import BeautifulSoup

def parse_value(value_str):
    """解析字符串数值，转换为整数"""
    value_str = value_str.strip()
    if not value_str or value_str == '-':
        return 0
    try:
        return int(float(value_str.replace('万', '')) * 10000)
    except ValueError:
        print(f"解析失败: {value_str}")
        return 0

# 目标URL
url = "https://www.resonance-columba.com/route"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# 发送请求
response = requests.get(url, headers=headers)
print(f"请求状态码: {response.status_code}")

if response.status_code != 200:
    print("请求失败！")
    exit()

# 解析HTML
soup = BeautifulSoup(response.text, "html.parser")

# 查找表格
table = soup.find("table")
if not table:
    print("错误: 页面中未找到表格！")
    exit()

# 获取所有行数据
rows = table.find_all("tr")

# 提取起点城市名
# 假设第二列是起点城市，表格的第一行包含起点城市的标签
start_cities = [rows[i].find_all("td")[0].get_text(strip=True) for i in range(1, len(rows))]  # 获取每行的第一列
print(f"提取的起点城市：{start_cities}")

# 提取终点城市名
# 假设第二行是终点城市，表格的第二行包含终点城市的标签
end_cities = [td.get_text(strip=True) for td in rows[2].find_all("td")]
print(f"提取的终点城市：{end_cities}")

# 存储数据点
data_points = []

# 解析表格中的数据
for i, row in enumerate(rows[3:]):  # 跳过前两行标题和城市名
    cells = row.find_all("td")
    if i >= len(start_cities):
        print(f"警告: 起点城市数与行数不匹配，第 {i+3} 行超出起点城市的范围。")
        break  # 如果行数超出了起点城市的数量，提前退出
    start = start_cities[i]  # 起点城市
    for j, cell in enumerate(cells[1:]):  # 跳过第一列（起点城市列）
        if j >= len(end_cities):
            print(f"警告: 终点城市数与列数不匹配，第 {j+1} 列超出终点城市的范围。")
            break  # 如果列数超出了终点城市的数量，提前退出
        end = end_cities[j]  # 终点城市
        value = parse_value(cell.get_text(strip=True))  # 解析利润数据

        if value > 0 and start != end:  # 过滤无效值和自身到自身的情况
            print(f"添加路线: {start} → {end} : {value}")
            data_points.append((value, start, end))

# 将数据写入文件 prices.txt
with open("prices.txt", "w", encoding="utf-8") as file:
    if data_points:
        file.write("起点站 → 终点站 : 价格（单位：万）\n")
        for value, start, end in data_points:
            file.write(f"{start} → {end} : {value // 10000}万 (原始值: {value})\n")
        print("数据已保存到 prices.txt 文件中！")
    else:
        file.write("未找到任何有效数据！\n")
        print("未找到任何有效数据！")
