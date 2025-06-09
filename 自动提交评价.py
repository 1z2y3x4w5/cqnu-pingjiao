a=int(input("请输入需要评价的课程数量：") )  # 输入需要评价的课程数量
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # 最大化启动Chrome浏览器
chrome_options.binary_location = r"D:\chromium\chrome.exe"  # 替换为你的chrome.exe实际路径

# 指定chromedriver路径
service = Service('D:/chromedriver/chromedriver.exe')  # 替换为你的chromedriver.exe实际路径

# 创建WebDriver对象
web = webdriver.Chrome(service=service, options=chrome_options)

# 添加这一行，设置等待对象
wait = WebDriverWait(web, 20)  # 20秒超时，可根据需要调整

# 打开“重庆师范大学校园门户”
web.get('https://csxmh.cqnu.edu.cn/PersonalApplications/viewPage?active_nav_num=1')
# 等待页面加载完成
time.sleep(12)  # 根据实际情况调整等待时间，最好使用企业微信扫码登录

# 打开“教务系统”
web.get('https://csxrz.cqnu.edu.cn/cas/login?service=https%3a%2f%2fjwglxt.cqnu.edu.cn%2fsso%2fzllogin')
# 等待页面加载完成
time.sleep(3)  # 根据实际情况调整等待时间

# 打开“学生评价”
web.get('https://jwglxt.cqnu.edu.cn/jwglxt/xspjgl/xspj_cxXspjIndex.html?doType=details&gnmkdm=N401605&layout=default')
# 等待页面加载完成
time.sleep(5)  # 根据实际情况调整等待时间

label = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/div[1]/div/div[2]/div[2]/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[8]/select')
label.click()
time.sleep(1)  # 等待下拉菜单加载

label = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/div[1]/div/div[2]/div[2]/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[8]/select/option[16]')
label.click()
time.sleep(5)  # 等待选择完成


try:    
    while True:  # 进入一个无限循环，直到遇到异常
                for i in range(1, a+1):  # 遍历第1至第a项评价条目
                    code = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="{i}"]/td[8]'))).text  # 查找并获取评价状态文本
                    print(f"评价{i} 状态：{code}")  # 打印出当前评价的状态
                    if code == '提交':
                        continue  # 如果评价状态为“提交”，则跳过评价
                    else:
                        # 如果评价状态不是“提交”，则点击该评价条目
                        wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="{i}"]/td[8]'))).click()
                        all_table = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="ajaxForm1"]/div[2]/div[1]/div[2]/table')))
                        # 先填写评语
                        textarea = web.find_element(By.ID, '3600F32EB5E33709E065000000000001_py')
                        textarea.clear()
                        textarea.send_keys("老师教得很好！")
                        time.sleep(1)
                        # 再点击评分项
                        for table in all_table:
                            all_line = table.find_elements(By.XPATH, './tbody/tr')
                            for line in all_line:
                                input_elem = line.find_elements(By.TAG_NAME, 'input')[0]
                                web.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_elem)
                                time.sleep(0.2)
                                if not input_elem.is_selected():
                                    input_elem.click()
                        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ajaxForm1"]/div[2]/div[1]/div[2]/table[1]/tbody/tr[19]/td[2]/div/div[2]/label/input'))).click()
                        wait.until(EC.element_to_be_clickable((By.ID, 'btn_xspj_tj'))).click()
                        wait.until(EC.element_to_be_clickable((By.ID, 'btn_ok'))).click()
                        time.sleep(1)  
                        print(f"评价{i} 状态：已评价")  # 打印出当前评价的状态变化
                        continue  # 跳过当前循环，继续下一个评价条目
            
except Exception as e:  # 捕获任何异常
    print("异常信息：",e)  # 打印异常信息
finally:
    web.quit()  # 关闭浏览器


