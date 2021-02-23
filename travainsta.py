from config import message, repeat, chrome_driver, link, bin_location
from login import user, password
from selenium import webdriver
from random import randint
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class TravaInsta:
    opt = Options()
    opt.binary_location = bin_location
    driver = webdriver.Chrome(options=opt, executable_path=chrome_driver)
    wait_a_min_or = WebDriverWait(driver, 60)

    def start(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()

        # Type login and password
        self.wait_a_min_or.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

        # Submit
        self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')))
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

        self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        
        # Close push notification pop-up

        self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]')))
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]').click()

        self.driver.get(link)
        self.send(message, repeat)

    
    def send(self, message, repeat):
        count = 0
        errors = 0
        while(True):
            for j in range(5):
                try:                        
                    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')))
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').click()
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(self.get_comment(count))
                    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')))
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]').click()
                    count+=1
                    print(self.get_comment(count))
                except:
                    print("Pause for comment limit")
                    sleep(600)
                    self.driver.refresh()
                    errors+=1
                if(errors>2):
                    break
            if(errors>2):
                    print("Stoped by dially comment limit")
                    break
            sleep(300)
        print("fim")
    def get_comment(self, count):
        return message[count]
        
        




