from datetime import date

import pytest

from second_part.src import return_date
from second_part.src import make_right_get

# from second_part.src import AccessWebsite
#
#
# def test_access_website():
#     website = AccessWebsite()
#     website.login(username="admin", password="admin")
#     assert website.access_website() == "Success"
#     website2 = AccessWebsite()
#     website2.login(username="test", password="test")
#     with pytest.raises(Exception):
#         website2.access_website()

def test_date():
    assert return_date(2025,3) == '2025-3/31'
    assert return_date(2025, 2) == '2025-2/24'


def test_response():
    assert isinstance(make_right_get(), dict)