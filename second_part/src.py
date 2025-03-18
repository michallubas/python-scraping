# Your code here
import requests


# task 1
def make_right_get():
    headers = {
        'Accept': 'application/json'
    }
    url = 'https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1'
    r = requests.get(url, headers=headers)
    return r.json()


# task 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap

# task 5

class LoginMetaClass(type):
    pass


class AccessWebsite(metaclass=LoginMetaClass):
    logged_in = False

    def login(self, username, password):
        if username == "admin" and password == "admin":
            self.logged_in = True

    def access_website(self):
        return "Success"
