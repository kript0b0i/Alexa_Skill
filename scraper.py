from email.headerregistry import Address
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time
import logging 

logging.basicConfig(level =logging.DEBUG,filename="Scraper.log",filemode='w', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

class ScraperLogic:

    def __init__(self, address, store):
        """
        The function takes in an address and a store name, and returns the distance from the address to
        the store
        """
        self.PATH = Service("/Users/luis_mendoza/Alexa_Skill/chromedriver")
        self.ChromeOptions =webdriver.ChromeOptions()
        self.ChromeOptions.add_argument('--headless')
        self.ChromeOptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service = self.PATH ,options= self.ChromeOptions)
        #self.address = input("Enter your address: ")
       # self.store = input("Enter name of the store: ")
        self.address = address
        self.store = store
        self.info = []
        self.firstStore = ' '
        self.secondStore = ' '
        self.thirdStore = ' '
        self.direction = []
        self.Maps(self.address, self.store)
    
    def Maps(self, address, stores):
        """
        The function takes in an address and a store name and returns the top 3 possible addresses of the
        store
        
        :param address: The address of the city you want to search for stores in
        :param stores: the name of the store you want to search for
        """
        print("[!]crawler in progress....")
        googleMaps = 'https://www.google.com/maps'
        self.driver.get(googleMaps)
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(address)
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(Keys.ENTER)
        time.sleep(6)
        self.driver.find_element(By.XPATH,'//*[@id="sb_cb50"]' ).click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(stores)
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(Keys.ENTER)
        time.sleep(6)
        self.info=self.driver.find_elements(By.CLASS_NAME,'W4Efsd')
        self.firstStore =self.info[2].text
        self.secondStore=self.info[2+5].text
        self.thirdStore=self.info[7+5].text
        print(f'[!]Possible address: {self.firstStore}')
        print(f'[!]Anohter possible address: {self.secondStore}')
        print(f'[!]Anohter possible address: {self.thirdStore}')
        choice = []
        choice.append(self.firstStore)
        choice.append(self.secondStore)
        choice.append(self.thirdStore)
        get_links = self.driver.find_elements(By.CLASS_NAME, 'hfpxzc')
        get_links[0].click()
        time.sleep(6)
        print(self.driver.find_element(By.CLASS_NAME,  'CsEnBe').get_attribute('href'))
        print('[*]Chromedriver terminated')
        #self.driver.quit()
        return choice



    
    
    


