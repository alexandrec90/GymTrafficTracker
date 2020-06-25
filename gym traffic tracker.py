from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import csv

#specify path of chromedriver
driverPath = r'C:\Users\Alexandre\Documents\Programming\chromedriver_win32\chromedriver.exe'
#make driver headless so browser doesn't show
options = webdriver.ChromeOptions()
options.add_argument('headless')
#launch driver
driver = webdriver.Chrome(executable_path = driverPath, chrome_options=options)
#navigate to gym webpage
gymUrl = 'https://www.nautilusplus.com/fr/succursale/berri-uqam/'
driver.get(gymUrl)
#css to get element that contains occupancy
occCss = 'div.spinner-gym-occupation>strong'
#wait for the occupancy to be loaded
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, occCss)))
driver.implicitly_wait(1000)
#element that contains occupancy 
occElem =  driver.find_element_by_css_selector(occCss)
#get the occupancy
occupancy = occElem.text
#print it
#print(occupancy)
#get timestamp
ts = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#write result to csv file
outPath = r"C:\Users\Alexandre\Documents\Programming\python\Gym Traffic.csv"
with open(outPath, "a") as outFile:
    outCsv = csv.writer(outFile, lineterminator = '\n', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    outCsv.writerow([ts, occupancy])
#close the driver
driver.close()
driver.quit()
