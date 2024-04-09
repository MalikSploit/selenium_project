from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--kiosk")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=chrome_options)


def load_urls_from_file(file_path):
    """Load URLs from a file and return as a list."""
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls


urls_file_path = "C:/Users/malik/Desktop/urls.txt"

while True:
    # Reload URLs from the file at the beginning of each loop
    urls = load_urls_from_file(urls_file_path)

    if not urls:
        urls = ['https://google.com']

    for url in urls:
        driver.get(url)
        try:
            select_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl02_ctl00')))
            select = Select(select_element)
            select.select_by_visible_text('Whole Page')
        except Exception as e:
            print(f"Error loading URL {url}: {e}")
        time.sleep(30)
