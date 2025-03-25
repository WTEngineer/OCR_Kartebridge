from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver
# chromedriver_path = './chromedriver'  # Update this path

# Initialize the Chrome driver
# driver = webdriver.Chrome(chromedriver_path)

def google_search(search_query):
        
    service = Service()
    # options = webdriver.ChromeOptions()
    chrome_options = Options()
