from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # 添加这行
# 初始化浏览器
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 无头模式
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("你的目标网页URL")

    # 使用稳定特征定位输入框
    input_locator = (By.XPATH, '''
        //input[
            @type='text' 
            and contains(@class, 'MuiInputBase-input') 
            and contains(@class, 'MuiOutlinedInput-input')
        ]
    ''')

    # 等待输入框可交互
    input_element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(input_locator)
    )

    # 清空现有内容（如果需要）
    input_element.clear()
    
    # 输入新文本
    input_element.send_keys("ul0dkS7G99v8S9AVjTyVD")
    
    # 验证输入（可选）
    print("当前输入框内容：", input_element.get_attribute('value'))

except Exception as e:
    print("操作失败:", str(e))
    driver.save_screenshot('error.png')  # 保存错误截图

finally:
    driver.quit()