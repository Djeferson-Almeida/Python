from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import pyperclip


def slow_type(element,text,delay=0.1):
   for character in text: 
      element.send_keys(character)
      time.sleep(delay)
   

class GoogleTranslator:
     def open_google_translate(self):
      self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
      self.wait = WebDriverWait(self.driver,10)
      self.driver.set_page_load_timeout(15)
      self.driver.implicitly_wait(15)
      self.actions = webdriver.ActionChains(self.driver)


      self.driver.get('https://translate.google.com/')
     def set_resouce_language(self,source_language):
        self.driver.find_elements(By.XPATH,'//button[@aria-label="Mais idiomas de origem"]')[0].click()
        slow_type(self.driver.find_elements(By.XPATH,('//input[@aria-label="Pesquisar idiomas"]'))[0],source_language)
        self.actions.send_keys(Keys.RETURN)
        self.actions.perform()


     def target_language(self,target_language):
        time.sleep(0.5)
        self.driver.find_elements(By.XPATH,'//button[@aria-label="Mais idiomas de chegada"]')[0].click()
        slow_type(self.driver.find_elements(By.XPATH,('//input[@aria-label="Pesquisar idiomas"]'))[1],target_language)
        self.actions.send_keys(Keys.RETURN)
        self.actions.perform()

     def translate(self,text):
        self.driver.find_element(By.XPATH,'//textarea[@aria-label="Texto de origem"]').send_keys(text)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@aria-label="Copiar tradução"]')))
        self.driver.find_element(By.XPATH,'//button[@aria-label="Copiar tradução"]').click()
        self.driver.find_element(By.XPATH,'//button[@aria-label="Limpar texto original"]').click()
        return(pyperclip.paste())
            
        
     def close_google_translate(self):
        self.driver.quit()
     

translator = GoogleTranslator()
translator.open_google_translate()
translator.set_resouce_language('Inglês')
translator.target_language('Português')

file = open('History.txt', 'r', encoding='utf8')
lines = file.readlines()
file.close()

history_translated = open('History_translated.txt', 'w', encoding='utf8')

text = False

translator.close_google_translate()