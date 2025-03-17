import pytest
from second_part.src import AccessWebsite


def test_access_website():
    website = AccessWebsite()
    website.login(username="admin", password="admin")
    assert website.access_website() == "Success"
    website2 = AccessWebsite()
    website2.login(username="test", password="test")
    with pytest.raises(Exception):
        website2.access_website()

