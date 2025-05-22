from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import pyperclip


def slow_type(element,text,delay=0.1):
   for character in text: 
      element.send_keys(character)
      time.sleep(delay)
   

class GoogleTranslator:
     def open_google_translate(self):
      options = Options()
      options.set_preference('intl.accept_languages','en-US')
      self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options = options)
      self.wait = WebDriverWait(self.driver,10)
      self.driver.set_page_load_timeout(15)
      self.driver.implicitly_wait(15)
      self.actions = webdriver.ActionChains(self.driver)


      self.driver.get('https://translate.google.com/')

#Método que escolhe a linguagem de origem
     def set_resouce_language(self,source_language):
        self.driver.find_elements(By.XPATH,'//button[@aria-label="More source languages"]')[0].click()
        slow_type(self.driver.find_elements(By.XPATH,('//input[@aria-label="Search languages"]'))[0],source_language)
        self.actions.send_keys(Keys.RETURN)
        self.actions.perform()

#Método que escolhe a linguagem de destiono
     def target_language(self,target_language):
        button = self.driver.find_elements(By.XPATH,'//button[@aria-label="More target languages"]')[0]
        self.actions.move_to_element(button).perform()
        button.click()
        slow_type(self.driver.find_elements(By.XPATH,('//input[@aria-label="Search languages"]'))[1],target_language)
        self.actions.send_keys(Keys.RETURN)
        self.actions.perform()

#Método traduzir
     def translate(self,text):
        self.driver.find_element(By.XPATH,('//textarea[@aria-label="Source text"]')).send_keys(text)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@aria-label="Copy translation"]')))
        self.driver.find_element(By.XPATH,('//button[@aria-label="Copy translation"]')).click()
        self.driver.find_element(By.XPATH,('//button[@aria-label="Clear source text"]')).click()
        return pyperclip.paste()
            
     def close_google_translate(self):
        self.driver.quit()
     

translator = GoogleTranslator()  
translator.open_google_translate()
translator.set_resouce_language('English')
translator.target_language('Portuguese')


input_file_path = 'D:/Python_estudo/Estudos/WEB/History.txt'
output_file_path = 'D:/Python_estudo/Estudos/WEB/History_translated_.txt'
def translate_file(input_filepath, output_filepath, translator_instance):
    
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            with open(output_filepath, 'w', encoding='utf-8') as outfile:
                print(f"\nIniciando tradução do arquivo: {input_filepath} (linha por linha)")
                line_number = 0
                for line in infile: # Itera linha por linha
                    line_number += 1
                    cleaned_line = line.strip() # Remove espaços em branco e quebras de linha das extremidades

                    if cleaned_line: # Se a linha não estiver vazia após o strip
                        print(f"  Traduzindo linha {line_number}: {cleaned_line[:70]}...") # Mostra o início da linha
                        try:
                            translated_line = translator_instance.translate(cleaned_line)
                            outfile.write(translated_line + '\n')
                        except Exception as e:
                            print(f"  Erro ao traduzir linha {line_number}: '{cleaned_line[:50]}...'. Erro: {e}")
                            outfile.write(f"[ERRO TRADUCAO] {cleaned_line}\n") # Escreve o original com marcador
                    else:
                        outfile.write('\n') # Mantém linhas vazias para formatar a saída

        print(f"Tradução concluída. Saída salva em: {output_filepath}")

    except FileNotFoundError:
        print(f"Erro: O arquivo de entrada '{input_filepath}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")

translated = open('History_translated.txt','w', encoding='utf8')

translate_file(input_file_path, output_file_path, translator)

translated.close()

translator.close_google_translate()