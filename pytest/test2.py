import requests
#动态数据

# url="https://www.resonance-columba.com/api/get-prices"
# prices = requests.get(url).text
# print(prices)

url="https://www.resonance-columba.com/_next/static/chunks/e712e954-d8470a30e1cc2437.js"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
requests.get(url, headers=headers)

prices1 = requests.get(url).text
print(prices1)

# import requests

# url = "https://www.resonance-columba.com/api/get-prices"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     print(response.text)  # 查看返回的 JSON 数据
# else:
#     print(f"请求失败，状态码: {response.status_code}")


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# # 设置 ChromeDriver 路径
# service = Service("chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 无头模式，不打开浏览器

# # 启动 WebDriver
# driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://www.resonance-columba.com/route")

# # 等待数据加载并抓取
# import time
# time.sleep(5)  # 等待 JavaScript 加载

# # 提取价格数据
# page_source = driver.page_source
# print(page_source)  # 查看 HTML 是否包含价格数据

# driver.quit()
