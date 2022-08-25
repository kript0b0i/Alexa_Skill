from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
from selenium.webdriver.common.keys import Keys 
import time

class demo:
	def __init__(self):
		self.pathofdemo = Service (executable_path=r"C:\Users\lizar\Documents\GMU\Alexa Project\chromedriver.exe") 
		self.optiondemo = webdriver.ChromeOptions()
		'''
		self.optiondemo.add_argument('--headless')
		self.optiondemo.add_argument('--no-sandbox')
		self.optiondemo.add_argument('--disabled-setuid-sandbox')
		'''
		self.browser = webdriver.Chrome(service = self.pathofdemo)#,options= self.optiondemo)

		
	def getinteger(self, strings):
		return re.findall('\d*\.?\d+',strings)

	def webdemo (self,address,stores):
		
		findaddress = f'https://www.google.com/maps'
		self.browser.get(findaddress)
		searchbar = self.browser.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(address)
		self.browser.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(Keys.ENTER)
		time.sleep(2)
		self.browser.find_element(By.XPATH,'//*[@id="sb_cb50"]' ).click()
		time.sleep(2)
		searchbar = self.browser.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(stores)
		self.browser.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(Keys.ENTER)


		#googleinfo = self.browser.find_element(By.CLASS_NAME,'Z0LcW').text
		#self.browser.close()
		
'''
		googleinfoslice = googleinfo.split(', ')

		googlelongitude = ''.join(self.getinteger(googleinfoslice[0]))

		googlelatitude = ''.join(self.getinteger(googleinfoslice[1]))

		print(googlelongitude)
		print(googlelatitude)

		googlemaplink = f'https://www.google.com/maps/search/{stores}/@{googlelongitude},-{googlelatitude}'
		print(googlemaplink)
		self.browser.get(googlemaplink)
		'''



	

address = input('enter address: ')
stores = input('enter store: ')
bobdemo = demo()
bobdemo.webdemo(address, stores)


