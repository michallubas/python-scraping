import json

from third_part.src import parse_categories


def test_parse_categories():
    categories = parse_categories()
    with open('./expected_categories.json') as f:
        expected_categories = json.load(f)
    assert categories == expected_categories



from third_part.src import WebDriver
def test_drive():

    with WebDriver() as driver:
        uri = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"
        driver.get(uri)
        assert  driver.title == 'Iced Teas | Woolworths'

        uri = "https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel/"
        driver.get(uri)
        assert 'EDEKA24 | Schokoriegel' in driver.title

        driver.quit()


