<div align="center">
    <h1 align="center">cqnu-pingjiao</h1>
    <p align="center">重庆师范大学正方教务系统一键学生评教</p>
</div>


# 概述
又到了期末，恶心的评教又来了，每次看着二三十个课程需要评教，就很无语，老老实实评教，又要花费不少时间，因此，写了它

# 软件依赖
1.python软件，官网为  https://www.python.org/  ，最好下载3.11以上版本

2.chrome游览器，官网为  https://www.google.com/intl/zh-CN/chrome/   
  也可以下载chromium游览器，官网为  https://www.chromium.org/getting-involved/download-chromium/  
  二选一

3.chromedriver，官网为  https://googlechromelabs.github.io/chrome-for-testing/

# 克隆项目到本地
```ruby
git clone https://github.com/1z2y3x4w5/cqnu-pingjiao
```

# 使用pip安装项目依赖
```ruby
pip install -r requirements.txt
```
# 使用过程
自动保存评价.py和自动提交评价.py，二选一，若选择自动保存评价.py还需自动保存提交.py文件由保存变成提交

下面以运行自动保存评价.py文件为示例（运行自动提交评价.py文件与其无异）：

1.更改chrome或chromium的绝对地址（3个py文件都要更改）

其中“D:\chromium\chrome.exe”是绝对地址
```ruby
chrome_options.binary_location = r"D:\chromium\chrome.exe"
```

2.更改chromedriver的绝对地址（3个py文件都要更改）

其中“D:/chromedriver/chromedriver.exe”是绝对地址
```ruby
service = Service('D:/chromedriver/chromedriver.exe')
```

3.检查文字框的ID是否正确

把鼠标指针停在文字框上，右击点击“检查”，打开开发者工具界面

其HTML格式为
```ruby
<input type="text" id="evalComment" class="form-control" name="comment">
```

检查evalComment是否和“3600F32EB5E33709E065000000000001_py”相同

若不同，则替换文件中的"3600F32EB5E33709E065000000000001_py"
```ruby
textarea = web.find_element(By.ID, '3600F32EB5E33709E065000000000001_py')
```

4.更改评语

**注：**
括号里的引号不能丢
```ruby
textarea.send_keys("老师教得很好！")
```

5.选择哪个评价项目选择“符合”
```ruby
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ajaxForm1"]/div[2]/div[1]/div[2]/table[1]/tbody/tr[19]/td[2]/div/div[2]/label/input'))).click()
```
py文件中选的是第19个

若想要选择其他的（如X），就把

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ajaxForm1"]/div[2]/div[1]/div[2]/table[1]/tbody/tr[19]/td[2]/div/div[2]/label/input'))).click()

中的“tr[19]”替换为“tr{X}”

# 启动项目
当一切准备就绪。使用python运行自动保存评价.py
```ruby
python 自动保存评价.py
```
当所有的评价都保存了，其显示“已评完”，且评价没有问题后，使用python运行自动保存提交.py
```ruby
python 自动保存提交.py
```
**或**

当一切准备就绪。使用python运行自动提交评价.py
```ruby
python 自动提交评价.py
```
# **注：登入时最好用企业微信扫码登入！**
若12秒都来不及扫码登入，就提高等待时间，将time.sleep(12)更改为time.sleep(20)，当然，也可以减少等待时间
```ruby
# 打开“重庆师范大学校园门户”
web.get('https://csxmh.cqnu.edu.cn/PersonalApplications/viewPage?active_nav_num=1')
# 等待页面加载完成
time.sleep(12)  # 根据实际情况调整等待时间，最好使用企业微信扫码登录

```
# **注：最好不要直接运行自动提交评价.py文件，若出了问题，本人一概不负！！！**
