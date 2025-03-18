import json

# from src import parse_categories


# def test_parse_categories():
#     categories = parse_categories()
#     with open('./expected_categories.json') as f:
#         expected_categories = json.load(f)
#     assert categories == expected_categories

from third_part.src import WebDriver


def test_drive():

    with WebDriver() as driver:
        uri = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"
        driver.get(uri)
        assert 'Woolworths Supermarket - Buy Groceries Online' in driver.title
        driver.quit()

