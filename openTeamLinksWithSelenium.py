"""
自动打开常用的计划 Links

Version: 0.1
Author: 黄华智
"""
# 参考地址：http://jonathansoma.com/lede/foundations-2017/classes/more-scraping/selenium/
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# ChromePath = '/Applications/Google Chrome.app/Contents/MacOS/'
# 需要打开的 tabs
tabs_list = [
  # Jupiter Release Schedule 
  'https://docs.google.com/spreadsheets/d/1cl10AHmQ1QwZGdQkEe3n0gCwwx8icsu1hMATs0hR93w/edit#gid=540016998',
  # Titan wishlist
  'https://docs.google.com/spreadsheets/d/11UCFueGUcgi4sqaCLmVmRaliLI1Ay2u2MXoywWXlnDs/edit#gid=1508044272',
  # Titan dashboard
  'https://jira.ringcentral.com/secure/Dashboard.jspa?selectPageId=25460'
]

# 记录当前 chrome 的端口
chromePort = '1356'
# 记录当前 chrome 的路径
chromePath = '/Users/lawrence.huang/Applications/Google Chrome.app/Contents/MacOS/Google Chrome.exe'

# 实例化一个启动参数对象
options = Options()
# 禁用浏览器正在被自动化程序控制的提示，好像没用
options.add_argument('--disable-infobars')
# 连接已开启的 chrome 的端口
# options.add_experimental_option("debuggerAddress", "127.0.0.1:" + chromePort)
# 启动浏览器
# driver = webdriver.Chrome(executable_path=chromePath, options=options)
driver = webdriver.Chrome(options=options)
# 最大化窗口
# driver.maximize_window()
# 打开 tabs
for index in range(len(tabs_list)):
  if index == 1:
    driver.get(tabs_list[index])
  else: 
    new_tab_script = "window.open('" + tabs_list[index] + "');"
    driver.execute_script(new_tab_script)

#to refresh the browser
# driver.refresh()
#to close the browser
# driver.close()