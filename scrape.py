import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()

def clean_html(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

f = open("C:\\Users\\hh\\Desktop\\scrape\\Banesat.csv", "w")
f.write("Metri_katror,Cmimi\n")

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[2]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")  

for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[3]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[4]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")  
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[5]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[6]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")  
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[7]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[8]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")    
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[9]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[10]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[11]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[12]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")  
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[13]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[14]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[15]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")    
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)

driver.get("https://www.devinf.com/")
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/ul/li[1]/select/option[16]").click()
driver.find_element("xpath", "/html/body/div[1]/div[2]/form/div/div/div[1]/div[2]/button").click()
elementet = driver.find_elements("xpath", "/html/body/div/section/div[2]/div[1]/ul/li")   
for element in elementet:
    Metri_katror = clean_html(element.find_element("xpath", "./a/div[2]/span[2]").get_attribute("innerHTML")).replace("m2", "").replace("&amp;", "&").strip()
    Cmimi = clean_html(element.find_element("xpath", "./a/div[2]/span[4]").get_attribute("innerHTML")).replace(",", "").replace("Euro", "").replace("Monthly", "").strip()
    if Cmimi != '0':
        f.write("{},{}\n".format(Metri_katror, Cmimi)) 
time.sleep(2)