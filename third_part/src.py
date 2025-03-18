

def parse_categories():
    categories = []

    def get_categories_recursive():
        # TODO: Your code here
        pass

    get_categories_recursive()
    return categories




# Task 2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
import csv


class WebDriver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.headless = False

        # location for chrome portable
        service = Service('C:\GoogleChromePortable64\chromedriver_97.0.4692.71.exe')
        options.binary_location = "C:\GoogleChromePortable64\App\Chrome-bin\chrome.exe"
        # options.add_argument('--incognito')

        # launch driver, location for driver
        self.driver = webdriver.Chrome(
            service=service,
            options=options)

        # wait for the elements to load DOM
        self.driver.implicitly_wait(20)

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()


with WebDriver() as driver:
    uri = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"
    driver.get(uri)

    # breadcrumb parts
    li_elements = driver.find_elements(By.CLASS_NAME, 'breadcrumbs-link.fs.ng-star-inserted')
    breadcrumb_list = list()
    for li_item in li_elements:
        breadcrumb_list.append(li_item.text)

    # stopper, can be beautifier later with WebDriverWait
    elements_stopper = driver.find_elements(By.XPATH,
                                    '//*[@id="search-content"]/div/shared-grid/div/div[2]/shared-product-tile/shared-web-component-wrapper/wc-product-tile//section/div/div[1]/div/div')

    elements = driver.find_elements(By.CLASS_NAME, 'product-grid-v2--tile')

    titles = list()
    for element_object in elements:
        title = element_object.text.split('\n')[3]
        titles.append(title)

    # write list to CSV file
    filename = str(breadcrumb_list) + '.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(titles)
