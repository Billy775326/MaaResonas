from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# 配置浏览器选项
options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 禁用自动化标志

# 初始化WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    url = "https://www.resonance-columba.com/route"
    driver.get(url)
    
    print(f"正在加载页面: {url}")
    
    # 改进的等待条件：等待表格可见
    wait = WebDriverWait(driver, 15)
    table_locator = (By.CSS_SELECTOR, "table")  # 改为通用表格选择器
    
    # 显式等待表格加载
    table = wait.until(EC.presence_of_element_located(table_locator))
    print("检测到表格结构")
    
    # 附加等待确保数据加载（根据实际情况调整时间）
    time.sleep(2)  # 针对AJAX数据的保守等待
    
    # 获取并解析页面内容
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # 更健壮的表格定位方式
    target_table = soup.find("table")
    
    if not target_table:
        raise ValueError("页面中未找到任何表格")

    # 提取表格数据
    extracted_data = []
    for row in target_table.find_all("tr"):
        cols = [
            col.text.strip().replace('\n', ' ')  # 清理换行符
            for col in row.find_all(["td", "th"])
        ]
        extracted_data.append("\t".join(cols))
    
    # 写入文件
    output_file = "price_data.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(extracted_data))
    
    print(f"成功提取 {len(extracted_data)} 行数据到 {output_file}")
    
    # 打印前3行示例
    print("\n数据示例：")
    print("\n".join(extracted_data[:3]))

except Exception as e:
    print(f"运行出错: {str(e)}")
    # 保存错误时的页面快照
    with open("error_page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("已保存错误页面到 error_page.html")

finally:
    driver.quit()
    print("浏览器已关闭")