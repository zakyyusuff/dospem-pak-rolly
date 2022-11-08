from selenium import webdriver
import pytest

driver = webdriver.Chrome()
driver.minimize_window()

Url = [
    ("https://www.google.com","Google"),
    ("https://www.instagram.com/accounts/login/","Login • Instagram")
]

@pytest.mark.parametrize('address,result',Url)
def test_Youtube(address,result):
    driver.get(address)
    Title = driver.title

    assert Title == result

