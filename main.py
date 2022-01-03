from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException

path="C:/Users/123/Desktop/chromedriver/chromedriver.exe"

theyknowitsme=Service(executable_path=path)
itpours=webdriver.ChromeOptions()
astro=webdriver.Chrome(service=theyknowitsme,options=itpours)
astro.get("https://tinder.com/")
time.sleep(20)
makeshoure=astro.find_element(By.XPATH,'//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(5)
ye=astro.find_element(By.XPATH,'//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[3]/button').click()
time.sleep(60)
piano=astro.find_element(By.NAME,"phone_number")
piano.send_keys("0941183372")
piano.send_keys(Keys.ENTER)

time.sleep(180)

for n in range(0,100):
    time.sleep(5)
    try:

        lacing=astro.find_element(By.XPATH,'//*[@id="o-1335420887"]/div/div/div[3]/button[2]')
        lacing.click()
        print("send the request")
        time.sleep(5)
    except NoSuchElementException:
        imbillionare=astro.find_element(By.XPATH,'//*[@id="o-1556761323"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button')    
        imbillionare.click()
        print("didn't finm it the firdst time")
        time.sleep(5)
    except NoSuchElementException:
        lookinstupid=astro.find_element(By.XPATH,'//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        lookinstupid.click()
        print("third time")    
    except ElementClickInterceptedException:
        try:
            match_popup = astro.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            myflowsinister=astro.find_element(By.XPATH,'//*[@id="o-2100293516"]/div/div/div[1]/div/div[3]/button')
            myflowsinister.click()
        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
    # try:
    #     crown=astro.find_element(By.XPATH,'//*[@id="o-2100293516"]/div/div/div[1]/div/div[3]/button').click()
    # except NoSuchElementException:
    #    pass    
# ye=astro.find_element(By.XPATH,'//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
# time.sleep(10)
# dududu=astro.find_element(By.XPATH,'//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[1]/div/button').click()
# mother=astro.find_element(By.NAME,"email")
# mother.send_keys("dagmabebe00@gmail.com")
# pride=astro.find_element(By.NAME,"pass")
# pride.send_keys("23$sSae$%^Ssdfa")
# rediculus=astro.find_element(By.NAME,"login").click()

# mymind=astro.find_element(By.XPATH,'//*[@id="o-1556761323"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]').click()
# feelinonme=astro.find_element(By.CSS_SELECTOR,".H(40px) a")
# print(feelinonme.text)
# rari=astro.find_element(By.XPATH,'//*[@id="o-1556761323"]/div/div[2]/div/div/div[1]/button').click()
# inthenighttime=astro.find_elements(By.CSS_SELECTOR,".W(100%) button")
# for i in range(0,len(inthenighttime)):
#     inthenighttime[1].click()
# isyours=astro.find_element(By.XPATH,'//*[@id="o-1556761323"]/div/div[2]/div/div/div[1]/button').click()
# istight=astro.find_element(By.XPATH,'//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
# ironman=astro.find_element(By.XPATH,'//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[1]/div/button').click()

time.sleep(3600)
astro.quit()
# /html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span