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


# task 3
import calendar
calendar.setfirstweekday(0)

def deco_date(func):
    def new_func(year, month):
        day = func(year, month).split(" ")[0]
        return str(year) + '-' + str(month) + '/' + day
    return new_func


@deco_date
def return_date(year, month):
    weeks_list = calendar.monthcalendar(year, month)
    last_week = weeks_list[-1]
    last_week = [day for day in last_week if day > 0]
    first_day = last_week[0]

    return str(first_day) + " " + list(calendar.month_name)[month]

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
