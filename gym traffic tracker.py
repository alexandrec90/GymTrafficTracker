from selenium import webdriver
from datetime import datetime
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
#wait for the occupancy to be loaded
#driver.implicitly_wait(2)
#get the occupancy
occupancy = driver.find_element_by_css_selector('div.spinner-gym-occupation>strong').text
#print it
#print(occupancy)
#get timestamp
ts = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#write result to csv file
outPath = r"C:\Users\Alexandre\Documents\Programming\chromedriver_win32\Gym Traffic.csv"
with open(outPath, "a") as outFile:
    outCsv = csv.writer(outFile, lineterminator = '\n', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    outCsv.writerow([ts, occupancy])
#close the driver
driver.close()
driver.quit()
