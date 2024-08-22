import time
import os
import datetime
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.headless = True
chrome_options = webdriver.ChromeOptions()

script = "take_planes.py"
realtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe', options=options)

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',options=options)

start_log_file_path = "/home/pier/auto/logs/start.log"
with open(start_log_file_path, "a") as start_log:
  start_log.write(f"{script} is started on {realtime}\n")
log_file_path = "/home/pier/auto/logs/take_planes.log"

#log_file_path = "./take_planes.log"
con = sqlite3.connect("take_planes.db")
cursor = con.cursor()
def createtable():
  cursor.execute("CREATE TABLE IF NOT EXISTS planes (value REAL)")
  con.commit()


def tableadd(value):
  cursor.execute("INSERT INTO planes (value) VALUES (?)", (value,))
  con.commit()


createtable()
driver.get("https://www.958bets10.com/tr/giris")
time.sleep(5)

username = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/obg-m-login-with-dialog/obg-m-dialog-layout/div/obg-m-login-container/obg-m-generic-login-container/form/div[1]/mat-form-field[1]/div/div[1]/div/input')
#bet_user = input("Username ?\n")
bet_user = "erdem.uluta@gmail.com"
username.send_keys(f"{bet_user}")

password = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/obg-m-login-with-dialog/obg-m-dialog-layout/div/obg-m-login-container/obg-m-generic-login-container/form/div[1]/mat-form-field[2]/div/div[1]/div[1]/input')
#bet_pass = input("Password ?\n")
bet_pass = ""
password.send_keys(f"{bet_pass}")

driver.find_element(By.XPATH,'//*[@id="login"]/obg-m-login-with-dialog/obg-m-dialog-layout/div/obg-m-login-container/obg-m-generic-login-container/form/div[2]/button').click()
time.sleep(2)
try: 
  driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/obg-m-dialog-layout/div/obg-m-suspicious-login-container/obg-m-suspicious-login-request-code/div[1]/mat-radio-group/mat-radio-button[2]/label/span[1]/span[1]').click()
  driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/obg-m-dialog-layout/div/obg-m-suspicious-login-container/obg-m-suspicious-login-request-code/div[2]/button').click()
except:
  time.sleep(5)

time.sleep(5)
driver.get("https://aggr-api-prod.reevotech.com/isblauncher/218/51935?lang=tr&cur=TRY&mode=1&background=1&user=1&uid=1927240835&token=a67aee32-e323-41a1-b0b2-daf415e7b927")
time.sleep(5)
just = driver.find_element(By.XPATH, '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]/div/app-bubble-multiplier[1]/div')
old_text = just.text
value = float(old_text[:-1])
tableadd(value)
'''
print(old_text[:-1])
with open(log_file_path,"a") as logs:
  logs.write(old_text[:-1])
  logs.write("\n")
  '''
while True:
    try:
      values = driver.find_element(By.XPATH, '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]/div/app-bubble-multiplier[1]/div')      
      new_text = values.text
      if new_text != old_text:
        print(new_text[:-1])
        value = float(new_text[:-1])
        tableadd(value)
        '''
        with open(log_file_path,"a") as logs:
          logs.write(new_text[:-1])
          logs.write("\n")
          '''
        old_text=new_text

      
      time.sleep(2)
    except:
        driver.get("https://aggr-api-prod.reevotech.com/isblauncher/218/51935?lang=tr&cur=TRY&mode=1&background=1&user=1&uid=1927240835&token=a67aee32-e323-41a1-b0b2-daf415e7b927")
        print("Not found.\n")
        time.sleep(10)

