import gzip
import json


# Task 1 / needs to be improve, take types from #menu__departamento-1,2,3,4 etc
def parse_categories():
    categories = []
    file_path = 'categories.json.gz'
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        json_str = file.read()
        categories_dict = json.loads(json_str)
        for key in categories_dict.keys():

            if categories_dict[key].get('props') and categories_dict[key]['props'].get('items'):
                items = categories_dict[key]['props']['items']
                categories_list = items[0]['itemProps']['href'].split('/')[1:]
                categories_list = [name.replace('-', ' ') for name in categories_list]

                # if len(categories_list) == 2 and categories_dict[key]['props']['props'].get('label'):
                #     categories_list.append(categories_dict[key]['props']['props']['label'])

                word_list_final = list()
                for word in categories_list:

                    word_list = word.split()
                    word_list[0] = word_list[0].capitalize()
                    word_final = ' '.join(word_list)
                    word_list_final.append(word_final)

                categories.append(word_list_final)

    return categories


print(parse_categories())

# Task 2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
import csv
import time


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


def run_woolworths():
    with WebDriver() as driver:
        uri = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"
        driver.get(uri)

        print(driver.title)
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


# Task 3
def run_edeka24():
    with WebDriver() as driver:

        uri = "https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel/"
        driver.get(uri)

        time.sleep(5)

        # Accept all cookies button is inside the shadow dom
        shadow_root = driver.find_element(By.CSS_SELECTOR, "#usercentrics-root").shadow_root
        shadow_root.find_element(By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]').click()

        # Locate the element containing the image
        elements = driver.find_elements(By.CLASS_NAME, 'product-item')
        titles = list()
        for element_object in elements:
            title = element_object.text.split('\n')
            if len(title) == 3:
                titles.append(title[0])
            else:
                titles.append(title[1])

        return {'site_title': driver.title, 'products': titles}
