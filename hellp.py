from selenium import webdriver
import time
import json
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 虚拟出Chrome界面
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# action  linux服务器驱动地址
service = Service(executable_path='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)    # Chrome浏览器  
# driver = webdriver.Chrome(service='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver')    # Chrome浏览器  

# windows 系统驱动路径
# driver = webdriver.Chrome(executable_path='D:\Downloads\chromedriver_win32\chromedriver.exe')    # Chrome浏览器


# 环境变量中读取数据，包含账号密码，和登陆页面测试
u = os.environ["USERNAME"]
p = os.environ["PASSWORD"]

print('u',u)
print('p',p)
driver.get("https://neworld.tv/auth/login") 
#  获取cookies 
time.sleep(50)
# 账号密码登录版本
driver.find_element(By.ID, 'email').clear()
driver.find_element(By.ID, "email").send_keys(u)

driver.find_element(By.ID, 'passwd').clear()
driver.find_element(By.ID, "passwd").send_keys(p)

time.sleep(2)
driver.find_element(By.ID, "login-dashboard").click()

driver.refresh()#刷新页面 


driver.refresh()#刷新页面 

time.sleep(50)

# buttons = driver.find_element_by_xpath("//button[@id='checkin']")
# print('buttons',buttons)

driver.find_element(By.ID, "check-in").click() # 点击元素

time.sleep(10)

# 获取页面源代码
page_source = driver.page_source
print("page_source:\n " + page_source)
